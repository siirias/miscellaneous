# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 17:02:43 2022

@author: siirias
"""

#import pyproj
from pyproj import Proj
from pyproj import Transformer

the_tmerc = '+proj=longlat +datum=WGS84 +no_defs +ellps=WGS84 +towgs84=0,0,0'
transformer = Transformer.from_crs("EPSG:2393","WGS84")
print(transformer.transform(21.2604, 59.7545))

#wgslon 21.36793
#wgslat 59.78085
#tmerc_lon = 21.2604
#tmerc_lat = 59.7545