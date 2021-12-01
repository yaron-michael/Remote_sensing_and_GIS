# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 11:21:29 2016
#the plot wil be upsid its ok the geotif wil be good
@author: yaron
https://chrisalbon.com/statistics/frequentist/spearmans_rank_correlation/

'D:/python course/python_2018/Lesson 7/python7.py'
"""

import numpy as np
import pandas as pd
import scipy.stats

# stack array to make raster time series
DAY1 = np.array([[10, 7, 15], [10, 2, 10]])
DAY2 = np.array([[10, 7, 10], [45, 2, 5]])
DAY3 = np.array([[10, 7, 10], [25, 1, 5]])
stack = np.dstack((DAY1,DAY2,DAY3))
#print stack
#print stack.shape
#print np.mean(stack, axis=2)
#print np.sum(stack, axis=2)
a = stack[1,0,:]  # make a time series
#print a








# Create two lists of random values
x = [1,2,3,4,5,6,7,8,9]
y = [2,1,2,4.5,7,6.5,6,9,9.11]
# Create a function that takes in x's and y's
def spearmans_rank_correlation(xs, ys):
    
    # Calculate the rank of x's
    xranks = pd.Series(xs).rank()
    
    # Caclulate the ranking of the y's
    yranks = pd.Series(ys).rank()
    
    # Calculate Pearson's correlation coefficient on the ranked versions of the data
    return scipy.stats.pearsonr(xranks, yranks)
# Run the function
spearmans_rank_correlation(x, y)[0]

scipy.stats.spearmanr(x, y)[0]



import shutil
import numpy as np
import glob
import gdal
import rasterio   
import os 
from osgeo import gdal_array
import datetime
import xarray as xr
import itertools
import datetime

#linear_trend function
#in order to make time
def linear_trend(x):
    pf= np.polyfit(x.time, x, 1)
    # we need to return a dataarray or else xarray's groupby won't be happy
    return xr.DataArray(pf[0])


def spearmans_correlation(x):
    pf,pvale = scipy.stats.spearmanr(x.time, x)
    # we need to return a dataarray or else xarray's groupby won't be happy
    return xr.DataArray(pf)
        
        
#####################################
for_file_number= []
#set working dir
os.chdir('D:/TEST WORKING ON BIG FILE/test p vale')
working_dir = 'D:/TEST WORKING ON BIG FILE/test p vale'

src = rasterio.open('D:/TEST WORKING ON BIG FILE/2001mod13.tif')


#make a mult list with list of file insde it
for folder, subs, files in os.walk(working_dir):
    for filename0 in files:
       # print filename0[0:4]
        for_file_number.append(filename0)        
        
muilt_list = []
num = len(for_file_number)
for a in range(num-1):
    #for_file_number[a+1:]
    
    #print a+1
    muilt_list.append( for_file_number[a:])
    #muilt_list.append( for_file_number[a+1:])        
        
        
num = len(muilt_list)
x2 = muilt_list[1]
x = muilt_list[0]

folder =  'D:\\TEST WORKING ON BIG FILE\\test p vale'
for folder, subs, files in os.walk(working_dir):
        
       for n in range(num) :
           rasters =[] 
           #print n
           for filename in muilt_list[n]:   
           # print filename
            rasterfilename =[]
            
            rasterfilename.append(filename)
            
            aSrcF = gdal_array.LoadFile(os.path.join(folder,filename))
         #aSrc = np.flipud(aSrcF)#FILEP THE RASTER
           #aSrc[aSrc== -1.79769300e+308] = np.nan
            rasters.append(aSrcF)
          
      

       
           stackRast = np.dstack(rasters)
          # print muilt_list[n][0] 
         #  print stackRast.shape
           xr.DataArray(stackRast)
           da = xr.DataArray(stackRast, dims=('lat','lon', 'time'))
           kwargs = src.meta
           src = rasterio.open('D:/TEST WORKING ON BIG FILE/2001mod13.tif')
         #  print da
           # stack lat and lon into a single dimension called allpoints
           stacked = da.stack(allpoints=['lat','lon'])
           # apply the function over allpoints to calculate the trend at each point
           trend = stacked.groupby('allpoints').apply(spearmans_correlation)
           trend_unstacked = trend.unstack('allpoints')
           #print trend_unstacked
           #print trend_unstacked
           #trend_unstacked.plot()
           #print r'D:\TEST WORKING ON BIG FILE\\'"trnd"+muilt_list[n][0]+"-"+muilt_list[n][-1]
           with rasterio.open(r'D:\TEST WORKING ON BIG FILE\\'"trnd"+muilt_list[n][0]+"-"+muilt_list[n][-1], 'w', **kwargs) as dst:
            dst.write_band(1, trend_unstacked.astype(rasterio.float32))
           
           del stackRast
           del rasters
           del stacked
           del trend_unstacked

print ("a")





