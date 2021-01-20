# -*- coding: utf-8 -*-
"""
Created on Wed May 31 18:14:00 2017
https://developers.planet.com/tutorials/calculate-ndvi/
@author: YARON
"""
#del all DN_udm by hand do seacrh insde the dir and del
import rasterio
import numpy
from xml.dom import minidom

"D:\\TESTPATCH\NDVI\\"
import os
rootdir = "D:\\TESTPATCH\\"
#rootdir = r'D:\TESTPATCH'
d=rootdir
dir_list =filter(lambda x: os.path.isdir(os.path.join(d, x)), os.listdir(d))

coeffs = {} 
#files = os.listdir(os.curdir)


for dir0 in dir_list:
    s = os.chdir(rootdir+dir0)  
   
    #get file in working dir
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for name_file in files:
     if name_file[-3:] == "tif":  
         
      print name_file   
      A = name_file[:-3] 
      xml_file_name =  name_file[:-4] + "_metadata.xml"
      with rasterio.open(name_file) as src:
             band_red = src.read(2)
      with rasterio.open(name_file) as src:
             band_nir = src.read(3)
    xmldoc = minidom.parse(xml_file_name)
    nodes = xmldoc.getElementsByTagName("ps:bandSpecificMetadata")  
    # XML parser refers to bands by numbers 1-4
    coeffs = {}
    for node in nodes:
      bn = node.getElementsByTagName("ps:bandNumber")[0].firstChild.data
      #if bn in ['1', '2', '3', '4']:#
      if bn in ['1', '2', '3', '4']:#
          print bn
          i = int(bn)
          value = node.getElementsByTagName("ps:reflectanceCoefficient")[0].firstChild.data
          coeffs[i] = float(value)
    # Multiply by corresponding coefficients
    band_red = band_red * coeffs[3]
    band_nir = band_nir * coeffs[4]
    
     # Allow division by zero
    numpy.seterr(divide='ignore', invalid='ignore')
    # Calculate NDVI
    ndvi = (band_nir.astype(float) - band_red.astype(float)) / (band_nir + band_red)
    # Set spatial characteristics of the output object to mirror the input
    kwargs = src.meta
    kwargs.update(dtype=rasterio.float32,count = 1)
     
     
    # Create the file
    with rasterio.open("D:\\TESTPATCH\\"+"NDVI"+A+"tif", 'w', **kwargs) as dst:
        dst.write_band(1, ndvi.astype(rasterio.float32))
    




       
    

  


        
 


     
