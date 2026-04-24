import os
os.environ["JOBLIB_START_METHOD"] = "threading"
import multiprocessing
multiprocessing.set_start_method("spawn", force=True)

import pandas as pd
from sklearn.metrics import accuracy_score, roc_auc_score
from lightgbm import LGBMClassifier
from sklearn.model_selection import train_test_split, RandomizedSearchCV
import joblib

# =========================================
# 1. LOAD DATA
# =========================================
df = pd.read_csv("cleaned_rtc_data.csv")

# =========================================
# 2. SELECT FEATURES
# =========================================
df = df[['waiting_num',
         'holiday_or_peak_season',
         'journey_month', 
         'target',
         'holiday_waiting_interaction']]


# =========================================
# 4. SPLIT DATA
# =========================================
X = df.drop(columns=['target'])
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# =========================================
# 5. DEFINE MODEL
# =========================================
lgb = LGBMClassifier(random_state=42)

# =========================================
# 6. HYPERPARAMETER GRID
# =========================================
param_grid = {
    'n_estimators': [100, 200, 300],
    'learning_rate': [0.01, 0.03, 0.05, 0.1],
    'num_leaves': [20, 31, 50, 80],
    'max_depth': [-1, 5, 10, 20]
}

# =========================================
# 7. RANDOMIZED SEARCH
# =========================================

random_search = RandomizedSearchCV(
    lgb,
    param_distributions=param_grid,
    n_iter=30,   # try 30 combinations
    scoring='roc_auc',
    cv=3,
    random_state=42,
    n_jobs=1
)


# =========================================
# 8. TRAIN MODEL
# =========================================
random_search.fit(X_train, y_train)

# =========================================
# 9. BEST MODEL
# =========================================
model = random_search.best_estimator_
print("Best Parameters:", random_search.best_params_)


# =========================================
# 11. SAVE MODEL
# =========================================
joblib.dump(model, "ticket_model.pkl")
print("\nModel trained and saved successfully")