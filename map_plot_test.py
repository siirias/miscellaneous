# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 10:44:09 2022

@author: siirias
"""
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt          # just for plots
import matplotlib.ticker as mticker      # just for plots
import numpy as np
from PIL import Image

PX_RESOLUTION = 0.100 # km
MAX_PX_X = 3000
MAX_PX_Y = 3000
C_LAT = 59.78085  #tutkan sijainti
C_LON = 21.36793  #tutkan sijainti
Proj = ccrs.TransverseMercator(\
           central_latitude = C_LAT,\
           central_longitude = C_LON,\
           scale_factor = 0.001, approx=True) #kilometers, center at radar
Crs_LatLon = ccrs.PlateCarree()

DO_PLOT = True

def point_to_latlon(px_x,px_y):
    """
    px_x, px_y is to pixel index,
    0,0 being upper left corner

    Returns corresponding (lon, lat)

    uses variables:
    PX_RESOLUTION, MAX_PX_X, MAX_PX_Y, C_LAT, C_LON
    Proj, crs_latlon
    """
    x_km = (px_x-(MAX_PX_X/2.0))*PX_RESOLUTION  # convert pixel index into
    y_km = (px_y-(MAX_PX_Y/2.0))*PX_RESOLUTION  # km distance from center.
    return Crs_LatLon.transform_point(x_km, y_km, Proj)

if DO_PLOT: #loppu on vaan plottausta
    MIN_LAT = C_LAT - (150.0/1.852)/60.0
    MAX_LAT = C_LAT + (150.0/1.852)/60.0
    MIN_LON = C_LON - ((150.0/1.852)/60.0) / np.cos(MIN_LAT/180.0*np.pi)
    MAX_LON = C_LON + ((150.0/1.852)/60.0) / np.cos(MIN_LAT/180.0*np.pi)
    for p in [Proj]:#, Crs_LatLon]:
        plt.figure(figsize = (10,10))
        ax = plt.axes(projection=p)
        ax.coastlines(resolution = '10m')
        ax.add_feature(cfeature.GSHHSFeature())
        ax.set_extent((MIN_LON,MAX_LON,MIN_LAT, MAX_LAT))
        ax.set_aspect('auto')
        gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,\
                          linewidth=1, color='gray', alpha=0.5)
        gl.xlocator = mticker.FixedLocator(np.arange(MIN_LON,MAX_LON,0.1))
        gl.ylocator = mticker.FixedLocator(np.arange(MIN_LAT,MAX_LAT,0.1))
        a = Image.open('C:\\Users\\siirias\\Downloads\\mediaanisuodatettu.jpg')
        ax.imshow(a, extent=(-150,150,-150,150), transform=Proj)
        