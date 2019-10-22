import numpy as np
import pandas as pd, requests, json
import geopandas as gpd
from geojson import Feature, FeatureCollection, Point
landslide_df = pd.read_csv('short_landslide.csv')
landslide_df = pd.DataFrame(landslide_df)
landslide_df.drop('location_a', axis = 1, inplace = True)
landslide_df.columns = ['date','lat','lon']
landslide_df['date_short'] = landslide_df['date'].str.split(' ').str[0]
landslide_df.drop('date', axis = 1, inplace = True)
landslide_df = landslide_df.rename({'date_short':'date'}, axis = 1)
landslide_df['date'] = pd.to_datetime(landslide_df["date"]).dt.strftime('%Y%m%d')
print(landslide_df.head())
landslide_df['lat'] = landslide_df['lat'].astype(float)
landslide_df['lon'] = landslide_df['lon'].astype(float)
#landslide_df['date'] = landslide_df['date'].astype(float)

'''
Function taken from 'geoffboeing.com'
Exports a Pandas DataFrame to GeoJSON
'''

def df_to_geojson(df, properties, lat='lat', lon='lon'):
    print('hello')
    geojson = {'type':'FeatureCollection', 'features':[]}
    for _, row in df.iterrows():
        feature = {'type':'Feature', 'properties':{},'geometry':{'type':'Point','coordinates':[]}}
        feature['geometry']['coordinates'] = [row[lon],row[lat]]
        for prop in properties:
            feature['properties'][prop] = row[prop]
        geojson['features'].append(feature)
    return geojson



#geojson_landslide = df_to_geojson(landslide_df, properties = 'date')


features = landslide_df.apply(lambda row: Feature(geometry=Point((float(row['lon']), float(row['lat'])))),axis=1).tolist()



# all the other columns used as properties

#properties = landslide_df.drop(['lat', 'lon'], axis=1).to_dict('date')



# whole geojson object

feature_collection = FeatureCollection(features=features)#, properties=properties)



with open('./landslides.geojson', 'w', encoding='utf-8') as f:

    json.dump(feature_collection, f, ensure_ascii=False)
