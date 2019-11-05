import numpy as np
import pandas as pd, requests, json
import geopandas as gpd
from geojson import Feature, FeatureCollection, Point
import geojson

# Read data and load it into a dataframe

landslide_df = pd.read_csv('short_landslide.csv')
landslide_df = pd.DataFrame(landslide_df)


# rename the time column and delete time data
landslide_df['date'] = landslide_df['event_date'].str.split(' ').str[0]

# delete original date-time column
landslide_df.drop('event_date', axis = 1, inplace = True)
#landslide_df = landslide_df.rename({'date_short':'date'}, axis = 1)

landslide_df = landslide_df.dropna(how='any',axis=0) # gets rid of rows with missing data 
landslide_df.columns = landslide_df.columns.str.replace(' ', '') # gets rid of whitespaces

# change values from column to integers
landslide_df['location_accuracy'] = landslide_df['location_accuracy'].map(lambda x: x.rstrip('km')) # deletes "km" from colunm
landslide_df['location_accuracy'] = landslide_df['location_accuracy'].replace('exact', 0)
landslide_df['location_accuracy'] = landslide_df['location_accuracy'].replace('unknown', np.nan)
landslide_df = landslide_df.dropna(how='any',axis=0) # gets rid of rows with missing data 
landslide_df[['location_accuracy']] = landslide_df[['location_accuracy']].astype(int)

# sets which threshold radius is allowed (ie radius_accuracy=5 takes values of landslides where location is know within 5km)
radius_accuracy = 5

# selects rows of values withing the selected radius
indexNames = landslide_df[(landslide_df['location_accuracy'] > radius_accuracy)].index
landslide_df.drop(indexNames , inplace=True) 

# selects landslide size
landslide_df = landslide_df[(landslide_df.landslide_size == 'large') | (landslide_df.landslide_size == 'very_large') | (landslide_df.landslide_size == 'catastrophic')]
print('{} landslides within a {} radius accuracy'.format(landslide_df.count(), radius_accuracy))

landslide_df['date'] = pd.to_datetime(landslide_df['date']).dt.strftime('%Y%m%d')
landslide_df['latitude'] = landslide_df['latitude'].astype(float)
landslide_df['longitude'] = landslide_df['longitude'].astype(float)



# selects the landslide date range in format yyyymmdd

start_date = '20150623'
end_date = '20170307'

landslide_df = landslide_df[(landslide_df['date'] > start_date) & (landslide_df['date'] < end_date)]
print('{} landslides between {} and {}'.format(landslide_df.count(), start_date, end_date))



# function to convert csv data to geoJSON (taken from https://gis.stackexchange.com/questions/220997/pandas-to-geojson-multiples-points-features-with-python )


def  data2geojson(df):
    features = []
    insert_features = lambda X: features.append(geojson.Feature(geometry=geojson.Point((X["longitude"],X["latitude"])),properties=dict(date=X["date"])))
    df.apply(insert_features, axis=1)
    with open('landslide.geojson', 'w', encoding='utf8') as fp:
        geojson.dump(geojson.FeatureCollection(features), fp, sort_keys=True, ensure_ascii=False)


data2geojson(landslide_df)






