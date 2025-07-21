import pandas as pd

# Read the CSV
df = pd.read_csv('Covid_Trend_By_State_data.csv')  # Use your actual CSV filename

# Filter for California (case-insensitive)
filtered = df[df['Province State'].str.lower() == 'florida']

# Select the relevant columns for analysis
filtered = filtered[['Province State', 'Lat', 'Long', 'Max. CovidPositives']]

# Group by Lat/Long and get the maximum CovidPositives at each location
max_per_location = filtered.groupby(['Province State', 'Lat', 'Long'], as_index=False)['Max. CovidPositives'].max()
max_per_location = max_per_location.rename(columns={
    'Province State': 'State',
    'Lat': 'Lat',
    'Long': 'Long',
    'Max. CovidPositives': 'MaxCovid'
})
# Save to a new CSV
max_per_location.to_csv('FlMapCovid.csv', index=False)
