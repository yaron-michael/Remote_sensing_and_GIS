# -*- coding: utf-8 -*-
"""
Created on Tue May 18 16:39:07 2021
need to do conda back to vaeriosn nfeore i intall from sklego.linear_model import LowessRegression
@author: dhelman-lab
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import HourLocator, DayLocator, DateFormatter
import statsmodels.api as sm



   
   
  
df = pd.read_csv('C:/Users/dhelman-lab/Desktop/EBI-VI.csv', index_col="TIMESTAMP", parse_dates=True)
column = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33]
#column = [1,2,3,4,5]
column = map(str, column) 
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import statsmodels.api as sm

n=len(df)
x = list(range(0,n))

#לצייר את המקורי בלי אנטרלפיה
#את לואס עם אנטרלפתיה
#לייצא טבלה יומית

column = ['A',"B","C","D","E"]
idx  = pd.date_range('06-26-2016', '01-01-2021')#friast date is moutnh
#https://kanoki.org/2020/04/14/resample-and-interpolate-time-series-data/
df = pd.read_csv('C:/Users/dhelman-lab/Desktop/xxxa.csv', index_col="DATE", parse_dates=True)
df['index'] = df.index
#df=df.dropna()
df['A'] =  df['A'].interpolate('linear')
y = df["A"].tolist()
x = df["index"].tolist()


#df = df[df['A'].notna()]
#x = df['A'].interpolate('polynomial',order=2)
#x.plot()
#y = df["A"].tolist()
#x = df["index"].tolist()

#count_nan = len(df["A"]) - df["A"].count()
n=len(df)
x = list(range(0,n))

lowess = sm.nonparametric.lowess(y, x, frac=.1)
lowess_x = list(zip(*lowess))[0]
lowess_y = list(zip(*lowess))[1]




df= df.reindex(idx)#,fill_value=0
#https://kanoki.org/2020/04/14/resample-and-interpolate-time-series-data/


for name in column:
    print(name)
    original_y  = df[name].tolist()
    original_x = df["index"].tolist()
   
    df[name] =  df[name].interpolate('linear')
    y = df[name].tolist()
    x = df["index"].tolist()
    n=len(df)
    x = list(range(0,n))
    
    lowess = sm.nonparametric.lowess(y, x, frac=.1)
    lowess_x = list(zip(*lowess))[0]
    lowess_y = list(zip(*lowess))[1]
    df[name] = lowess_y
    
   # plt.plot(x, original_y, 'o')#not working good dount know what i got to plot
    #plt.plot(lowess_x, lowess_y, '*')#not working good dount know what i got to plot
    print(name)
   # plt.close()
    #plt.clf()
 

idx  = pd.date_range('06-26-2016', '01-01-2021')#friast date is moutnh
df = df.reindex(idx)
df = df.drop([ 'index'], axis=1)
df.to_csv('data1.csv')   
             





    
    

 
  


