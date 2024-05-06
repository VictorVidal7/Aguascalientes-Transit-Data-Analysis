from clean_data import clean_data
from statistical_analysis import perform_statistical_analysis
from visualizations import create_visualizations

def main():
    # Data cleaning
    clean_data('aguascalientes_gtfs/stops.txt')

    # Statistical analysis
    perform_statistical_analysis('aguascalientes_gtfs/stops_clean.csv')

    # Create visualizations
    create_visualizations('aguascalientes_gtfs/stops_clean.csv')

if __name__ == "__main__":
    main()