import gdal, geojson, subprocess
from osgeo import ogr
import os 

geojsonFileName = '../BritishColumbia/BritishColumbia.geojson'

outputFileName = 'BC_Footprints.shp'

inputString = 'ogr2ogr -f "ESRI Shapefile" ' + outputFileName + ' ' + geojsonFileName
os.system(inputString)
