import folium

# Create a map centered at the mean coordinates of the stops
m = folium.Map(location=[stops_clean['stop_lat'].mean(), stops_clean['stop_lon'].mean()], zoom_start=13)

# Add markers for each stop
for idx, row in stops_clean.iterrows():
    # Create a marker at the stop's coordinates with a tooltip showing the stop's name
    folium.Marker([row['stop_lat'], row['stop_lon']], tooltip=row['stop_name']).add_to(m)

# Save the map to an HTML file
m.save('stops_map.html')
