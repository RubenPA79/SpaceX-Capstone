import folium
import pandas as pd
import os
from folium.plugins import MarkerCluster

def create_folium_map():
    df = pd.read_csv('data/spacex_launch_geo.csv')
    df = df[['Launch Site', 'Lat', 'Long', 'class']]
    launch_sites_df = df.groupby(['Launch Site'], as_index=False).first()
    launch_sites_df = launch_sites_df[['Launch Site', 'Lat', 'Long']]
    
    nasa_coordinate = [29.559684888503615, -95.0830971930759]
    site_map = folium.Map(location=nasa_coordinate, zoom_start=5)
    
    # Add Launch Site markers
    for ix, row in launch_sites_df.iterrows():
        folium.Circle(
            [row['Lat'], row['Long']], 
            radius=1000, 
            color='#d35400', 
            fill=True).add_child(folium.Popup(row['Launch Site'])).add_to(site_map)
        folium.map.Marker(
            [row['Lat'], row['Long']],
            icon=folium.DivIcon(
                icon_size=(20,20),
                icon_anchor=(0,0),
                html=f'<div style="font-size: 12; color:#d35400;"><b>{row["Launch Site"]}</b></div>'
            )
        ).add_to(site_map)
        
    # Marker Clusters
    marker_cluster = MarkerCluster().add_to(site_map)
    
    def assign_marker_color(launch_outcome):
        if launch_outcome == 1:
            return 'green'
        else:
            return 'red'
            
    df['marker_color'] = df['class'].apply(assign_marker_color)
    
    for index, record in df.iterrows():
        folium.Marker(
            location=[record['Lat'], record['Long']],
            icon=folium.Icon(color='white', icon_color=record['marker_color']),
            popup=record['Launch Site'],
        ).add_to(marker_cluster)

    if not os.path.exists('assets'):
        os.makedirs('assets')
        
    site_map.save('launch_site_map.html')
    print("Generated launch_site_map.html")

if __name__ == "__main__":
    create_folium_map()
