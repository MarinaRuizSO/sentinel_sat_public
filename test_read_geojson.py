import geojson

def read_geojson(geojson_file):
    with open(geojson_file) as f:
        gj = geojson.load(f)
        return gj 

my_land = read_geojson('./landslides.geojson')
print(my_land[0])
