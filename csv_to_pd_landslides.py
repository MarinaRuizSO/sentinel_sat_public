'''
Imports the landslide catalog in a .csv file, reads it and puts selected columns into a pandas dataframe. 
Saves the resualting dataframe to a shorter .csv file.
'''
import matplotlib.pyplot as plt
import pandas as pd


landslides = pd.read_csv("./Global_Landslide_Catalog_Export.csv")

landslide_df = pd.DataFrame(landslides)

# these column names can be changed to whatever columns are of interest

landslide_df = landslide_df[['event_date', 'location_accuracy','landslide_size', 'latitude', 'longitude']]

landslide_df.to_csv('short_landslide.csv', encoding='utf-8', index = False)



