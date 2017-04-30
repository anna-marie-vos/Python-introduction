import folium
import pandas

df = pandas.read_csv("Volcanoes-USA.txt")
# .mean takes the average
map = folium.Map(location = [df['LAT'].mean(), df['LON'].mean()],zoom_start=6, tiles='Stamen Terrain')

def newColor(elevation):
    minVal = int(min(df['ELEV']))
    maxVal = int(max(df['ELEV']))
    incriment = int((maxVal - minVal)/3)
    if elevation in range(minVal, minVal+incriment ):
        return 'green'
    elif elevation in range(minVal+incriment ,minVal+incriment*2 ):
        return 'orange'
    else:
        return 'red'

for lat, lon, name, elev in zip(df['LAT'],df['LON'],df['NAME'], df['ELEV']):
    folium.Marker(location = [lat,lon],popup = name,icon=folium.Icon(newColor(elev))).add_to(map)

map.save('test.html')
