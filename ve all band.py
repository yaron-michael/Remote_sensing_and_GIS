#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 15:16:23 2019

@author: yaron
"""

import ee
import os
from ipygee import *

import pandas as pd 
from openpyxl import load_workbook
from datetime import datetime
ee.Initialize()







feature_to_use ='users/yaron1205/Mizam_Israeli_Wheat_Adaptation_to_Climate_Change/LR2019_GEE'
#feature_to_use ='users/yaron1205/Mizam_Israeli_Wheat_Adaptation_to_Climate_Change/PW2019_genus'

#fid_st of
id_colum_to_use = 'st_fid'
#id_colum_to_use = 'cv'
path_to_xls = 'D:/F.xlsx'
Scale = 0.001


name_of_columns = {
         'b1': 'VE1',
         'b2': 'VE2',
         'b3': 'VE3',
         'b4': 'VE4',
         'b5': 'VE5',
         'b6': 'VE6',
         'b7': 'VE7',
         'b8': 'VE8',
         'b9': 'VE9',
         'b10': 'VE10',
         'b11': 'VE11',
         'b12': 'VE12',
         'b15': 'CloudMask',
 }  
    




def Scale_function(x):
    x= x*Scale
    return x


feature = ee.FeatureCollection(feature_to_use)
fc_temp = feature.getInfo()
fc_info =fc_temp['features']



list_of_vale_to_loop =[]
# Using for loop 

for i in fc_info: 

    print(i['properties'][id_colum_to_use]) 

    list_of_vale_to_loop.append(i['properties'][id_colum_to_use])


# start the work
list_of_sheet =[]
list_of_sheet_name =[]
for vale in  list_of_vale_to_loop:
    print (vale)
    FC = (ee.FeatureCollection(feature_to_use).filter(ee.Filter().eq(id_colum_to_use, vale)))
    print(FC)  
    col = ee.ImageCollection('users/venusdataw10/VEw10').filterBounds(feature)
    time_series = col.filterDate('2018-07-11', '2019-05-31')
    bands = ['b1', 'b2', 'b3','b4', 'b5', 'b6','b7', 'b8', 'b9','b10', 'b11', 'b12','b15']
    chart_ts = chart.Image.series(**{
    'imageCollection': time_series, 
    'region': FC,
    'scale': 5,
    'bands': bands,
    'reducer': ee.Reducer.mean()}) 
    print(chart_ts.dataframe)   
 
    dataframe = chart_ts.dataframe.apply(Scale_function, axis=1)
 
   
        
    
    #chart_ts.dataframe['DATE'] = chart_ts.dataframe.index
    #chart_ts.dataframe = chart_ts.dataframe.reindex(columns=['DATE','B1', 'B2', 'B3','B4', 'B5', 'B6','B7', 'B8', 'B8A','B9', 'B10', 'B11','B12'])
    list_of_sheet.append(dataframe)
    list_of_sheet_name.append(vale)
    
    
# save the data
for sheet_data, sheet in zip(list_of_sheet, list_of_sheet_name):
    print(sheet_data, sheet)
    
    sheet_data['DATE'] = sheet_data.index
    sheet_data = sheet_data.reindex(columns=['DATE','b1', 'b2', 'b3','b4', 'b5', 'b6','b7', 'b8', 'b9','b10', 'b11', 'b12','b15'])
    sheet_data['b15'] = sheet_data['b15'].apply(lambda x: x* 1000) #cloud mask info
    sheet_data = sheet_data.rename(name_of_columns, axis='columns')
    sheet_data['DATE'] = sheet_data['DATE'].apply(lambda x: x.strftime("%d/%m/%Y"))
    writer = pd.ExcelWriter(path_to_xls, engine='openpyxl')
    book = load_workbook(path_to_xls)
    writer.book = book
    writer.sheets = dict((ws.title, ws) for ws in book.worksheets)

    sheet_data.to_excel(writer, sheet_name=sheet, index=False )
    writer.save()
    
    
#columnsTitles = ['ID','Vb1', 'Vb2', 'Vb3','Vb4', 'Vb5', 'Vb6','Vb7', 'Vb8', 'Vb9','Vb10', 'Vb11', 'Vb12']



#df = df.reindex(columns=columnsTitles)   
    