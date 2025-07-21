import pandas as pd

# Read the CSV
df = pd.read_csv('Covid_Trend_By_State_data.csv')

# Convert 'Province State' to lowercase to ensure case-insensitivity
df['Province State'] = df['Province State'].str.lower()

# List of states to include (lowercase for consistency)
states = ['california', 'texas', 'florida']

# Filter for California, Texas, and Florida
filtered = df[df['Province State'].isin(states)]

# Select the relevant columns
filtered = filtered[['RecordDate', 'Max. CovidPositives', 'Province State']]

# Optionally, ensure RecordDate is treated as a date
# filtered['RecordDate'] = pd.to_datetime(filtered['RecordDate'])

# Group by RecordDate and Province State, sum the Covid positives
summed = filtered.groupby(['RecordDate', 'Province State'], as_index=False)['Max. CovidPositives'].sum()

# Save the result to CSV
summed.to_csv('covid_daily_sum_ca_tx_fl.csv', index=False)
