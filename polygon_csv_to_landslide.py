'''
Imports the landslide catalog in a .csv file, reads it and puts selected columns into a pandas dataframe. 
Saves the resualting dataframe to a shorter .csv file.
'''
import matplotlib.pyplot as plt
import pandas as pd


landslides = pd.read_csv("./example_Global_Landslide_Catalog_Export_polygon.csv")

landslide_df = pd.DataFrame(landslides)

# these column names can be changed to whatever columns are of interest

landslide_df = landslide_df[['event_date', 'location_accuracy','landslide_size', 'latitude_1', 'longitude_1', 'latitude_2', 'longitude_2', 'latitude_3', 'longitude_3', 'latitude_4', 'longitude_4']]

landslide_df.to_csv('polygon_landslide.csv', encoding='utf-8', index = False)



