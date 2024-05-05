# Calculate descriptive statistics
print(stops_clean.describe())

# Count unique values to understand the diversity in categorical data
print(stops_clean['stop_name'].value_counts())