###Importing libraries
import folium
from folium.plugins import AntPath
import json
import random
import streamlit

def map_init():
    """
    Initializing a map object
    """
    mapObj = folium.Map(zoom_control=False,
                    control_scale=False,
                    #tiles='Stamen Terrain',
                    wrap_control=False)
    return mapObj


def data_init():
    """
    Initializing data in a geojson format
    """
    geojsonFilePath = "./data/submarine_cables.geojson"
    geojsonData = json.load(open(geojsonFilePath))

    return geojsonData


def line_creating(map, data, prop = 1):
    """
    Creating AntPath instances of each line in geojson file
    """
    for line in data['features']:
        if random.random() <= prop:
            lineCoordinates = line['geometry']['coordinates']
            lineCoordinates = [(point[1], point[0]) for point in lineCoordinates]
            AntPath(locations=lineCoordinates,
                    delay = random.randint(100, 800),
                    color='rgba(255, 255, 255, 0.1)',
                    pulse_color='green').add_to(map)
    return mapObj

def map_saving(map):
    """
    Saving a map in a mapObj.html file"""
    map.save('maps/mapObj.html')

if __name__ == "__main__":
    mapObj = map_init()
    dataGeojson = data_init()

    fullMap = line_creating(mapObj, dataGeojson, 0.2)

    map_saving(fullMap)