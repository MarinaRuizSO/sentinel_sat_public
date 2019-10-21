# connect to the API

from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt

from datetime import date

import sys
import pandas as pd
import geopandas as geopd
import pickle
api = SentinelAPI('MarinaRuiz', 'Guamnaquillo_96', 'https://scihub.copernicus.eu/dhus')

# search by polygon, time, and SciHub query keywords
footprint = geojson_to_wkt(read_geojson('./map.geojson'))
products = api.query(footprint, date=('20151219', date(2015, 12, 29)),platformname='Sentinel-2', cloudcoverpercentage=(0, 5))



# download all results from the search
api.download_all(products)



# convert to Pandas DataFrame
products_df = api.to_dataframe(products)
products_df = products_df.to_pickle("./sentinel_data.pkl")


# GeoJSON FeatureCollection containing footprints and metadata of the scenes
'''
geojson_products_df = api.to_geojson(products)
geojson_products_df = geojson_products_df.to_pickle("./geojson_sentinel_data.pkl")
'''


# GeoPandas GeoDataFrame with the metadata of the scenes and the footprints as geometries

geopd_products_df = api.to_geodataframe(products)
geopd_products_df = geopd_products_df.to_pickle("./geopd_products_df.pkl")


