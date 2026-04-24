import streamlit as st
import pandas as pd
import joblib
import shap
import numpy as np
import matplotlib.pyplot as plt
from lime.lime_tabular import LimeTabularExplainer
from datetime import datetime

# ==============================
# LOAD MODEL
# ==============================
model = joblib.load("ticket_model.pkl")

# ==============================
# LOAD TRAIN DATA (FOR XAI)
# ==============================
X_train = pd.read_csv("cleaned_rtc_data.csv")
X_train = X_train[['waiting_num',
                   'holiday_or_peak_season',
                   'journey_month',
                   'holiday_waiting_interaction']]

# ==============================
# HUMAN READABLE EXPLANATION
# ==============================
def generate_explanation(shap_vals, lime_exp, input_data, prob, adjusted_prob):
    explanation = []
    features = input_data.columns.tolist()

    explanation.append("---- EXPLANATION: ----\n")

    positive_factors = []
    negative_factors = []

    # SHAP reasoning
    for f, val in zip(features, shap_vals):
        if abs(val) < 0.01:
            continue

        if val > 0:
            positive_factors.append(f)
            explanation.append(f"+ {f} contributed positively towards confirmation.")
        else:
            negative_factors.append(f)
            explanation.append(f"- {f} negatively impacted confirmation.")

    # LIME reasoning
    explanation.append("\n---- LOCAL REASONING (LIME): ----")
    for f, weight in lime_exp.as_list():
        if weight > 0:
            explanation.append(f"+ {f} supports confirmation.")
        else:
            explanation.append(f"- {f} reduces confirmation chances.")

    # Final interpretation
    explanation.append("\n---- FINAL INTERPRETATION: ----")

    if adjusted_prob >= 0.6:
        explanation.append("+ Ticket is LIKELY to be CONFIRMED.")

        if positive_factors:
            explanation.append("Main reasons:")
            for f in positive_factors:
                explanation.append(f"   • {f} helped increase probability")
    else:
        explanation.append("- Ticket is UNLIKELY to be CONFIRMED.")

        if negative_factors:
            explanation.append("Main issues:")
            for f in negative_factors:
                explanation.append(f"   • {f} reduced the chances significantly")

    # Time effect
    if adjusted_prob < prob:
        explanation.append("\n- Limited time before journey reduced confirmation chances.")

    # Edge cases
    if input_data['waiting_num'].iloc[0] <= 5:
        explanation.append("\n+ Very low waiting number strongly favors confirmation.")

    if input_data['waiting_num'].iloc[0] > 50:
        explanation.append("\n- High waiting number makes confirmation difficult.")

    return explanation


# ==============================
# UI INPUT
# ==============================
st.title("Railway Ticket Confirmation Predictor")

waiting_num = st.number_input("Waiting Number", min_value=0, step=1)
holiday = st.selectbox("Holiday / Peak Season", ["No", "Yes"])
journey_date = st.date_input("Journey Date")

# ==============================
# PROCESS INPUT
# ==============================
if st.button("Predict"):

    days_left = (journey_date - datetime.today().date()).days

    if days_left < 0:
        st.error("Journey date already passed")
        st.stop()

    journey_month = journey_date.month
    holiday_val = 1 if holiday == "Yes" else 0
    holiday_waiting = holiday_val * waiting_num

    input_data = pd.DataFrame([{
        'waiting_num': waiting_num,
        'holiday_or_peak_season': holiday_val,
        'journey_month': journey_month,
        'holiday_waiting_interaction': holiday_waiting
    }])

    # ==============================
    # PREDICTION
    # ==============================
    prob = model.predict_proba(input_data)[0][1]

    adjusted_prob = prob


    # Waiting impact
    if waiting_num > 80:
        adjusted_prob *= 0.3
    elif waiting_num > 50:
        adjusted_prob *= 0.6
    elif waiting_num > 20:
        adjusted_prob *= 0.85

    # Time impact
    if days_left <= 1:
        adjusted_prob *= 0.2
    elif days_left <= 3:
        adjusted_prob *= 0.5
    elif days_left <= 7:
        adjusted_prob *= 0.8


    adjusted_prob = max(min(adjusted_prob, 0.98), 0.02)

    st.subheader("Prediction")
    st.write(f"Original Probability: {prob*100:.2f}%")
    st.write(f"Adjusted Probability: {adjusted_prob*100:.2f}%")

    # ==============================
    # SHAP
    # ==============================
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(input_data)

    if isinstance(shap_values, list):
        shap_vals = shap_values[1][0]
    else:
        shap_vals = shap_values[0]

    # ==============================
    # LIME
    # ==============================
    lime_explainer = LimeTabularExplainer(
        training_data=X_train.values,
        feature_names=X_train.columns.tolist(),
        class_names=['Not Confirmed', 'Confirmed'],
        mode='classification'
    )

    lime_exp = lime_explainer.explain_instance(
        input_data.values[0],
        model.predict_proba,
        num_features=4
    )

    # ==============================
    # TERMINAL STYLE OUTPUT (YOUR EXACT FORMAT)
    # ==============================
    st.subheader("Detailed Explanation")

    explanations = generate_explanation(
        shap_vals,
        lime_exp,
        input_data,
        prob,
        adjusted_prob
    )

    output_text = ""
    output_text += "\nFINAL RESULT:\n"
    output_text += f"Original Probability: {prob*100:.2f}%\n"
    output_text += f"Adjusted Probability: {adjusted_prob*100:.2f}%\n\n"
    output_text += "\n".join(explanations)

    st.code(output_text)

    # ==============================
    # SHAP vs LIME GRAPH
    # ==============================
    st.subheader("SHAP vs LIME Comparison")

    lime_dict = dict(lime_exp.as_list())
    shap_vals_plot = []
    lime_vals_plot = []

    for f in input_data.columns:
        shap_vals_plot.append(shap_vals[input_data.columns.get_loc(f)])

        matched = 0
        for key in lime_dict:
            if f in key:
                matched = lime_dict[key]
                break
        lime_vals_plot.append(matched)

    x = np.arange(len(input_data.columns))

    fig = plt.figure()
    plt.bar(x - 0.2, shap_vals_plot, width=0.4, label="SHAP")
    plt.bar(x + 0.2, lime_vals_plot, width=0.4, label="LIME")

    plt.xticks(x, input_data.columns, rotation=45)
    plt.title("SHAP vs LIME Feature Contribution")
    plt.legend()

    st.pyplot(fig)