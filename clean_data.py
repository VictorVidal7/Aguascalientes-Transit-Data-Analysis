import pandas as pd

def clean_data(filepath):
    # Load data from 'stops.txt' file
    stops = pd.read_csv(filepath)

    # Drop columns with too many missing values
    stops_clean = stops.drop(columns=['zone_id', 'stop_url', 'location_type', 'parent_station', 'stop_desc', 'stop_timezone', 'level_id', 'platform_code'])

    # Impute missing values in important columns (if applicable)
    stops_clean['stop_name'] = stops_clean['stop_name'].fillna('Unknown')

    # Save the cleaned data
    stops_clean.to_csv('aguascalientes_gtfs/stops_clean.csv', index=False)
