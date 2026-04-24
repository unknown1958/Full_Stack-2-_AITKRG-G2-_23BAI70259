# =========================================
# 1. IMPORT LIBRARIES
# =========================================
import pandas as pd
import numpy as np

# =========================================
# 2. LOAD DATA
# =========================================
df = pd.read_csv("Final_RTC.csv")

# =========================================
# 3. CLEAN COLUMN NAMES
# =========================================
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
print("Columns in dataset:\n", df.columns.tolist())



# =========================================
# 4. DROP IRRELEVANT COLUMNS
# =========================================

drop_cols = [
'unnamed:_0', 'pnr_number', 'train_number', 'class_of_travel', 'quota', 
'source_station', 'destination_station', 'current_status', 
'number_of_passengers', 'age_of_passengers', 'booking_channel',
'travel_distance', 'number_of_stations', 'travel_time', 'train_type', 
'seat_availability', 'special_considerations', 'waitlist_position',
'distance', 'booking_date',
]

df.drop(columns=[col for col in drop_cols if col in df.columns],
        inplace=True, errors='ignore')



# =========================================
# 5. TARGET VARIABLE
# =========================================
#def map_target(x):
#    x = str(x).strip().lower()

#    if 'not' in x:
#        return 0
#    elif 'confirm' in x:
#       return 1
#   else:
#        return np.nan
#df['target'] = df['booking_status'].apply(map_target)





# Remove any unexpected values
#df = df.dropna(subset=['target'])

# Drop booking_status after creating target
df.drop(columns=['booking_status'], inplace=True)

if 'target' not in df.columns:
    if 'final_status' in df.columns:
        df['target'] = df['final_status'].apply(
            lambda x: 1 if str(x).upper() in ['CNF', 'CONFIRMED'] else 0
        )
        df.drop(columns=['final_status'], inplace=True)

# ADDING NOICE
#df['waiting_num'] = df['waiting_num'].clip(lower=0)
mask = np.random.rand(len(df)) < 0.025
df.loc[mask, 'target'] = 1 - df.loc[mask, 'target']

# =========================================
# 8. BASIC DATE FEATURE (ONLY MONTH)
# =========================================
df['journey_month'] = pd.to_datetime(df['date_of_journey'], errors='coerce').dt.month
df.drop(columns=['date_of_journey'], inplace=True)


# =========================================
# 10. HANDLE MISSING VALUES
# =========================================
for col in df.select_dtypes(include=['int64', 'float64']).columns:
    df[col] = df[col].fillna(df[col].median())

# Fill only required columns
df['holiday_or_peak_season'] = df['holiday_or_peak_season'].fillna('No')



# =========================================
# 11. CATEGORICAL CONVERSION
# =========================================
df['holiday_or_peak_season'] = df['holiday_or_peak_season'].map({
    'Yes': 1,
    'No': 0
})
# Drop encoding failures
df = df.dropna(subset=['holiday_or_peak_season'])

# =========================================
# ⭐ NEW: FEATURE BALANCING STRATEGY
# =========================================

# Interaction Features
df['holiday_waiting_interaction'] = df['holiday_or_peak_season'] * df['waiting_num']

# =========================================
# 13. FINAL DATASET
# =========================================
df = df[['waiting_num',
         'holiday_or_peak_season',
         'journey_month', 
         'target',
         'holiday_waiting_interaction']]

X = df.drop(columns=['target'])
y = df['target']

print("\nFinal Features:\n", X.columns.tolist())
print("Dataset Shape:", X.shape)


# =========================================
# 15. SAVE CLEAN DATA
# =========================================
df.to_csv("cleaned_rtc_data.csv", index=False)

# Preview
df.head()
