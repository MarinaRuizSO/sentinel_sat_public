import geojson

def read_geojson(geojson_file):
    with open(geojson_file) as f:
        gj = geojson.load(f)
        return gj 

my_land = read_geojson('./landslide.geojson')
print(my_land['features'][0]['properties']['date'])
exact_date = my_land['features'][0]['properties']['date']
print(type(exact_date))

print('length: {}'.format(len(my_land['features'])))


#print(my_land[0])
