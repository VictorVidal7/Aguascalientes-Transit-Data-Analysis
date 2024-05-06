import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def create_visualizations(cleaned_data_path):
    # Load the clean CSV file
    stops_clean = pd.read_csv(cleaned_data_path)

    # Create a histogram of latitudes
    sns.histplot(stops_clean['stop_lat'], kde=True)
    plt.title('Distribución de Latitudes de Paradas')
    plt.xlabel('Latitud')
    plt.ylabel('Frecuencia')
    plt.show()