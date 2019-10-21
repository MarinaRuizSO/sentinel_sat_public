import pandas as pd
import geopandas as gpd
import pickle as pkl
import matplotlib.pyplot as plt
import fiona; fiona.supported_drivers


satellite_df = pd.read_pickle("./sentinel_data.pkl")

#satellite_geodf = gpd.read_pickle("./geopd_products_df.pkl")

print("this is the pandas dataframe")
print(list(satellite_df))
'''
print("this is the geopandas dataframe")
print(satellite_geodf.head())
'''
