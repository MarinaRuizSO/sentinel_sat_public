# connect to the API
# part of this code is taken from the sentinelsat Python API (https://sentinelsat.readthedocs.io/en/stable/api.html)
# options about the different options for data download are also found there
from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt
from datetime import date
import sys
import pandas as pd
import geopandas as geopd
import geojson
import datetime
from datetime import timedelta

# read the geojson file first 
def read_geojson(geojson_file):
    with open(geojson_file) as f:
        gj = geojson.load(f)
        return gj

my_landslide = read_geojson('./landslide.geojson')

# connect with the online sentinel hub website
api = SentinelAPI(<username>, <password>, 'https://scihub.copernicus.eu/dhus')

# change according to date format needed
date_format = "%Y%m%d"

# note: to read one feature: print(my_landslide['features'][0]['properties']['date'])

# defines time window for data search given an exact date
def time_interval(i):
    exact_date = my_landslide['features'][i]['properties']['date']
    exact_date = datetime.datetime.strptime(exact_date, date_format).date()
    start_date = exact_date - timedelta(days = 20)
    end_date = exact_date + timedelta(days = 20)  
    return start_date.strftime("%Y%m%d"), end_date.strftime(date_format)

# loop over all instances of landslides given in geojson file 

for i in range(len(my_landslide['features'])):
   
    exact_date = my_landslide['features'][i]['properties']['date']
    start_date, end_date = time_interval(i)
    # checks if date is after Sentinel 2 was launched(23-06-2015) 
    if datetime.datetime.strptime(start_date, date_format) >= (datetime.datetime.strptime('20150623', date_format)):
        
        # search by polygon, time and SciHub query keywords
        footprint = geojson_to_wkt(my_landslide[i])
        products = api.query(footprint, date=(start_date, end_date),platformname='Sentinel-2', cloudcoverpercentage=(0,10))
        
        # convert to pandas dataframe
        products_df = api.to_dataframe(products)
        # further sorting, check sentinelsat documentation for sorting options
        products_df_sorted = products_df.sort_values('ingestiondate', ascending = True)
        products_df_sorted_head = products_df_sorted.head(1)
        products_df_sorted_tail = products_df_sorted.tail(1)
 
        api.download_all(products_df_sorted_head.index)
        api.download_all(products_df_sorted_tail.index)
