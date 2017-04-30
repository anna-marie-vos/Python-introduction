import folium
map = folium.Map(location = [45.372,-121.697],zoom_start=12, tiles='Stamen Terrain')
folium.Marker(location = [45.3288,-121.6625],popup = 'Mt. Hood Meadows').add_to(map)
folium.Marker(location = [45.3311,-121.7311],popup = 'Timberlake Lodge').add_to(map)
map.save('test.html')
