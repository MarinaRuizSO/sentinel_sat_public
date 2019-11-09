# Sentinel data download from .csv file

Python3 code to automatically download data from the sentinelhub website from a .csv file by converting it to geojson file.


1. `polygon_csv_to_pd_landslides.py`: Takes in a .csv file, sorts the useful columns and transforms into pandas dataframe and creates shorter .csv file.
2. `format_polygon_landslide_csv.py`: Takes the appropiate columns and creates a geojson file with polygons.
3. `polygon_advanced_data_download_batch.py`: accesses sentinel hub and downloads the data.
4. `unzip_files.py`: unzips downloaded data.


Run each of the files in the given order. To access the SentinelHub website you will need to create an account. Include the username and password as strings in the designated space in the file `polygon_advanced_data_download_batch.py`.




## Installing 
Create a Python3 virtual environment if you do not have admin permissions (instructions given for Linux). 

### Install virtualenv package with `pip`
```
python3 -m pip install --user virtualenv
```

### Create the virtual environment
```
python3 -m venv my_virtual_env
```

### Activate the virtual environment (Linux)
```
source my_virtual_env/bin/activate
```
The name of the environment will now appear in brackets on the terminal.

### Deactivate the virtual environment
```
deactivate
```


## Prerequisites
Libraries needed (make sure the installed version is compatible with Python3): 
1. `pip3 install matplotlib`
2. `pip3 install pandas` 
3. `pip3 install geopandas`
4. `pip3 install geojson`
5. `pip3 install sentinelsat`
6. `pip3 install DateTime`
7. `pip3 install zipfile`
8. `pip3 install glob3`

