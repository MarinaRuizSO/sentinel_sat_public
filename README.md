Python3 code to automatically download data from the sentinelhub website from a .csv file.


1. `polygon_csv_to_pd_landslides.py`: Takes in a .csv file, sorts the useful columns and transforms into pandas dataframe and creates shorter .csv file.
2. `format_polygon_landslide_csv.py`: Takes the appropiate columns and creates a geojson file with polygons.
3. `polygon_advanced_data_download_batch.py`: accesses sentinel hub and downloads the data.
4. `unzip_files.py`: unzips downloaded data.


Run each of the files in the given order. To access the SentinelHub website you will need to create an account. Include the username and password as strings in the designated space in the file `polygon_advanced_data_download_batch.py`.

Libraries needed (make sure the installed version is compatible with Python3): 
1. `matplotlib`
2. `pandas` 
3. `geopandas`
4. `geojson`
5. `sentinelsat`
6. `datetime`
7. `zipfile`
8. `glob`
9. `os`
