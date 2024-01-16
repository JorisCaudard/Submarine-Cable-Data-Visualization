import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as cx

def pre_process():
    points_data = gpd.read_file("./data/landing_points.geojson")
    line_data = gpd.read_file("./data/submarine_cables.geojson")

    points_data = points_data.to_crs(epsg=3857)
    line_data = line_data.to_crs(epsg=3857)

    return points_data, line_data


if __name__ == "__main__":
    points_data, line_data = pre_process()

    fig, ax = plt.subplots(figsize=(10,10))
    points_data.plot(ax=ax, color = 'red')
    line_data.plot(ax = ax, color = 'blue')

    print(points_data.crs, line_data.crs)

    #cx.add_basemap(ax)  

    plt.show()
    #return points_data.head()