import matplotlib.pyplot as plt
import pickle
import pandas as pd


landslides = pd.read_csv("./Global_Landslide_Catalog_Export.csv")

landslide_df = pd.DataFrame(landslides)


landslide_df = landslide_df[['event_date', 'gazeteer_distance', 'latitude', 'longitude']]

landslide_df.to_csv('short_landslide.csv', encoding='utf-8', index = False)



