import zipfile
import glob
import os

satellite_zip = glob.glob('*.zip')
print(satellite_zip)



for i in range(len(satellite_zip)):
    zf = zipfile.ZipFile(satellite_zip[i])
    zf.extractall(path='.')
    zf.close()
    os.remove(satellite_zip[i])


