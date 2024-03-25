###Importing libraries
import folium
from folium.plugins import AntPath
import json
import random

###Global variables
#TODO: Change Syntax
lineColorPalette = ['#FF6E40', '#FF4081', '#7C4DFF', '#00E5FF', '#64DD17', '#9C27B0', '#FFD54F']

def map_init():
    """
    Initializing a map object
    """
    mapObj = folium.Map(zoom_control=False,
                    control_scale=False,
                    tiles='https://{s}.basemaps.cartocdn.com/dark_nolabels/{z}/{x}/{y}{r}.png',
                    attr='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
                    max_bounds=True)
    return mapObj


def data_init():
    """
    Initializing data in a geojson format
    """
    geojsonFilePath = "SubmarineDataVisualization/data/submarine_cables.geojson"
    geojsonData = json.load(open(geojsonFilePath))

    return geojsonData


def line_creating(map, data, prop = 1):
    """
    :map: A folium map Object
    :data: A geojson file
    :prop: Proportion of displayed lines (by default, all are displayed)
    Creating AntPath instances of each line in geojson file
    """
    for line in data['features']:
        if random.random() <= prop:
            lineCoordinates = line['geometry']['coordinates']
            lineCoordinates = [(point[1], point[0]) for point in lineCoordinates]
            AntPath(locations=lineCoordinates,
                    delay = random.randint(100, 800),
                    weight=1,
                    color='rgba(255, 255, 255, 0.1)',
                    pulse_color=random.choice(lineColorPalette),
                    reversed=random.choice([True, False]),
                    dash_array=[random.randint(10,50),50],
                    popup=line['properties']['name']
                    ).add_to(map)
    return mapObj

def map_saving(map):
    """
    Saving a map in a mapObj.html file
    :map: A folium map object
    """
    map.save('SubmarineDataVisualization/maps/mapObj.html')

if __name__ == "__main__":
    mapObj = map_init()
    dataGeojson = data_init()

    fullMap = line_creating(mapObj, dataGeojson)

    map_saving(fullMap)
