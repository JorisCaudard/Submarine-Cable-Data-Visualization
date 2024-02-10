import folium
from folium.plugins import AntPath
import json
import random


mapObj = folium.Map(zoom_control=False,
                    control_scale=False,
                    #tiles='Stamen Terrain',
                    wrap_control=False)


geojsonFilePath = "./data/submarine_cables.geojson"
geojsonData = json.load(open(geojsonFilePath))

fullMap = False

for line in geojsonData['features']:
    if fullMap:
        lineCoordinates = line['geometry']['coordinates']
        lineCoordinates = [(point[1], point[0]) for point in lineCoordinates]
        AntPath(locations=lineCoordinates,
                delay = random.randint(100, 800),
                color='rgba(255, 255, 255, 0.1)',
                pulse_color='green').add_to(mapObj)
    else:
        if random.random() <= 0.1:
            lineCoordinates = line['geometry']['coordinates']
            lineCoordinates = [(point[1], point[0]) for point in lineCoordinates]
            AntPath(locations=lineCoordinates,
                    delay = random.randint(100, 800),
                    color='rgba(255, 255, 255, 0.1)',
                    pulse_color='green').add_to(mapObj)
    
if fullMap:
    mapObj.save("mapObj_Full.html")
else:
    mapObj.save("mapObj.html")