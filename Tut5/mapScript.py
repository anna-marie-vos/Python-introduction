import folium
import pandas

df = pandas.read_csv("Volcanoes-USA.txt")

map = folium.Map(location = [45.372,-121.697],zoom_start=6, tiles='Stamen Terrain')

def newColor(elevation):
    if elevation in range(0,1500):
        return 'green'
    elif elevation in range(1500,3000):
        return 'orange'
    else:
        return 'red'

for lat, lon, name, elev in zip(df['LAT'],df['LON'],df['NAME'], df['ELEV']):
    folium.Marker(location = [lat,lon],popup = name,icon=folium.Icon(newColor(elev))).add_to(map)

map.save('test.html')
