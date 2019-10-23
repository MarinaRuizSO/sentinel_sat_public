import numpy as np
import pandas as pd, requests, json
import geopandas as gpd
from geojson import Feature, FeatureCollection, Point
import geojson


landslide_df = pd.read_csv('short_landslide.csv')
landslide_df = pd.DataFrame(landslide_df)
landslide_df.drop('gazeteer_distance', axis = 1, inplace = True)
landslide_df.columns = ['date','lat','lon']
landslide_df['date_short'] = landslide_df['date'].str.split(' ').str[0]
landslide_df.drop('date', axis = 1, inplace = True)
landslide_df = landslide_df.rename({'date_short':'date'}, axis = 1)

landslide_df = landslide_df.dropna(how='any',axis=0) # gets ride of rows with missing data 
landslide_df['date'] = pd.to_datetime(landslide_df['date']).dt.strftime('%Y%m%d')
landslide_df['lat'] = landslide_df['lat'].astype(float)
landslide_df['lon'] = landslide_df['lon'].astype(float)






def  data2geojson(df):

    features = []

    insert_features = lambda X: features.append(

            geojson.Feature(geometry=geojson.Point((X["lon"],

                                                    X["lat"])),

                            properties=dict(date=X["date"])))

    df.apply(insert_features, axis=1)

    with open('landslide.geojson', 'w', encoding='utf8') as fp:

        geojson.dump(geojson.FeatureCollection(features), fp, sort_keys=True, ensure_ascii=False)




data2geojson(landslide_df)






