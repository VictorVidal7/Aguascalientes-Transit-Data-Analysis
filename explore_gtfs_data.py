import pandas as pd
import os

def explore_data(directory):
    # List all files in the GTFS directory
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):  # Ensure you are loading text files
            file_path = os.path.join(directory, filename)
            # Load the CSV file
            data = pd.read_csv(file_path)
            
            # Display the filename and its first few rows
            print(f"\n{filename} - First rows:")
            print(data.head())
            
            # Display information about columns, data types, and null values
            print(f"\nInformation about {filename}:")
            print(data.info())
            
            # Display a statistical summary of numeric columns
            print(f"\nStatistical description of {filename}:")
            print(data.describe())
            
            # Count null values in each column
            print(f"\nNull values in {filename}:")
            print(data.isnull().sum())

# Directory where the GTFS files are stored
directory = 'aguascalientes_gtfs'

# Call the function
explore_data(directory)
