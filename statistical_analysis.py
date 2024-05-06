import pandas as pd

def perform_statistical_analysis(cleaned_data_path):
    stops_clean = pd.read_csv(cleaned_data_path)
    # Calculate descriptive statistics
    print(stops_clean.describe())

    # Count unique values to understand the diversity in categorical data
    print(stops_clean['stop_name'].value_counts())