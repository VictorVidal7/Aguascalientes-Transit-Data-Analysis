import matplotlib.pyplot as plt
import seaborn as sns

# Create a figure with two subplots
plt.figure(figsize=(10, 5))

# Plot the distribution of latitudes
plt.subplot(1, 2, 1)
sns.histplot(stops_clean['stop_lat'], kde=True)
plt.title('Distribution of Latitudes')

# Plot the distribution of longitudes
plt.subplot(1, 2, 2)
sns.histplot(stops_clean['stop_lon'], kde=True)
plt.title('Distribution of Longitudes')

# Display the plot
plt.show()