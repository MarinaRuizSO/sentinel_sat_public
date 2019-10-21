import matplotlib.pyplot as plt
import pickle
import pandas as pd


landslides = pd.read_csv("./landslide_inventory.csv")

landslide_df = pd.DataFrame(landslides)


landslide_df = landslide_df[['date_', 'location_a', 'latitude', 'longitude']]



