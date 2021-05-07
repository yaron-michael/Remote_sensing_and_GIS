# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 12:47:58 2021

@author: YARON
"""


import statistics
import pandas as pd
import itertools
import numpy as np
import os
import shutil
import gdown
from datetime import datetime
import csv
from itertools import chain
import os
import shutil
import gdown
from datetime import datetime
import csv
import datetime
import time
from datetime import datetime, date, time, timedelta
import pandas_bokeh
#https://datacarpentry.org/python-ecology-lesson/09-working-with-sql/index.html
import schedule







def run_code():
    #Parameters
#number_of_tap = 10 
#number_of_tap_with_the_same_vale = 6
#assem we work in minet  in the end -fuul cyley is 30 min or 60 min or else
 each_time_tap_send_data = 0.5 #in sencde (0.5= 30 sencd)
 number_of_time_step_to_skip =4
 #number_of_timp_step_to_mean = 6 
 time_of_time_step_for_tap = 6#'number_of_tap_with_the_same_vale'
 number_of_timp_step_to_mean = time_of_time_step_for_tap
 Lines_to_ignore = 525 #this is because of of error in the csv file 

 save_dir_of_dat = 'C:/Users/dhelman-lab/Downloads/temp'
 os.chdir(save_dir_of_dat) 

 number_of_tap = 10
 Valve_no_start  = 1
 NAME = "temp.dat"
 output_file_to_plot = "data_to_plot_co2.csv"
 figsize_of_html_x = 1500
 figsize_of_html_y = 750
#end of Parameters
 url_of_dat_file = 'https://drive.google.com/uc?id=1DHJuGDyoI8TtboI3EVF7Mf6Hed2XthhU'



 dir_to_save_the_dat_file = save_dir_of_dat




 os.chdir(save_dir_of_dat)
 now = datetime.now()
 print ("Current date and time : ")
 date_and_time = now.strftime("%Y-%m-%d %H:%M:%S")
 #dir_of_dat = 'D:/download_from_web'
 #dat_dir =dir_of_dat +"/" + date_and_time +".dat"

 x = date_and_time[0:10] +"-"+date_and_time[11:13]+"-"+date_and_time[14:16]+"-"+date_and_time[17:19]
 gdown.download(url_of_dat_file, "temp.dat", quiet=False)#we need to chnge the file name after this
 shutil.copy2("temp.dat", "data "+x+".dat") #we work on this file now 
 #os.rename("temp.dat","data "+x+".dat")

 data = pd.read_csv("temp.dat", header=3)      
 print(data.columns)
 data.columns = ['TIMESTAMP', 'record', 'temp_in', 'RH_in', 'temp_out', 'RH_out', 'Valve_no', 'CO2_Avg',
       'Batt_volt_Avg']
 data.to_csv('temp_co2.csv', index=False)#this is data_with_co2
 data = data.iloc[Lines_to_ignore:]
 data_no_co2 = data[['TIMESTAMP','temp_in', 'RH_in', 'temp_out', 'RH_out']]#this it data with no co2
 data_no_co2.to_csv('data_no_co2data.csv', index=False)
 data = pd.read_csv('temp_co2.csv', index_col='TIMESTAMP',parse_dates=True )#dayfirst=True
 data = data.iloc[Lines_to_ignore:]




#first_date_of_output_csv = '02/01/2021 12:30'
#freq_of_min = '30Min'#of output csv
#cycle = '30min'
#Parameters
#columns_NAME = ['record', 'Temp_in', 'RH_in', 'temp_out','RH_out','Value_no']
#vertical_stack.columns = columns_NAME
 periods_vale = number_of_tap *time_of_time_step_for_tap*each_time_tap_send_data#output in Seconds
#X = time_step_if_sub_tap*time_of_time_step_for_tap
 freq_of_min = str(int(periods_vale))+"min"
 cycle = str(int(periods_vale))+"min"


 columns_vale  = list(range(1, number_of_tap+1))


 def unique(list1):
     
    # insert the list to the set
    list_set = set(list1)
    # convert the set to the list
    unique_list = (list(list_set))
    for x in unique_list:
        print (x)


 DATE_FOR_CODE =  datetime(2021, 2, 16, 0, 0, 0, 0)#this is just for the code to find The combination of minutes is possible 

 #date_list = [Today + timedelta(minutes=15) for x in range(0, 100)]
 date_list = [DATE_FOR_CODE + timedelta(minutes= int(periods_vale)*x) for x in range(0, 100)]
 datetext=[x.strftime(' T%H:%M ') for x in date_list]
 datetext=[x.strftime('%M') for x in date_list]



 temp=[]
 for x in datetext:
  temp.append(x)
  print(x)
 Possibility_of_MIN = np.unique(temp)
 Possibility_of_MIN = Possibility_of_MIN.tolist()



# function to get unique values
 #def unique(list1):
     
    # insert the list to the set
 #   list_set = set(list1)
    # convert the set to the list
 #   unique_list = (list(list_set))
  #  for x in unique_list:
 #       print (x)
        
 
    

 tap_vale = list(range(1, number_of_tap+1))




 equal_arrays1 =[]
 for vale in tap_vale:
     print(vale)
    
     myarray = np.empty(time_of_time_step_for_tap, dtype=np.int)
     myarray.fill(vale)  
     x = myarray.tolist()
     one_sub_cycle_of_tap = len(x)
     equal_arrays1.append(x)
    
 equal_arrays_to_compre=np.concatenate((equal_arrays1))


 templist =[]
#data = pd.read_csv("wokring.csv", index_col='TIMESTAMP',parse_dates=True )#dayfirst=True

#data = pd.read_csv("temp_csv.csv", index_col='TIMESTAMP',parse_dates=True)
 DATE=data.index.values[0]
 first_timestamp = pd.to_datetime(DATE)
#set number of step in the output file and the freq of output file ,
 data['DATE'] = data.index

 start = data.iloc[1]
 index = len(data)
 list_of_range = list(range(0,index))
 data['ID_INDEX'] = list_of_range



 for index, row in data.iterrows():
   
       Valve_no = row['Valve_no']
       #print(Valve_no)
       temp_DATE = str(row['DATE'])
       strdate = temp_DATE[17:19]
       print(strdate)
       if strdate in Possibility_of_MIN and Valve_no == 1:
        break   
        
 print ("FOUND")        
 print(index)
 start_range =index
 start_range_string =  str(start_range)
#we have the start range od the data
#THIS FROMAT '2021-02-11 15:57:30'

 data=data.loc[start_range:]





 data = data.groupby(pd.Grouper(freq=cycle))


 DATA = []
 templist0 =[]
 templist_of_date =[]


 #now work on
 count=0
 for k, gp in data:
             count+=1
             print (count)
             print('key=' + str(k))
             print (gp)
            # time_to_test = gp.index[0]
             
     
 
             array_to_test =gp["Valve_no"].to_numpy()     
           #  equal_arrays1 = np.array(equal_arrays1)
            
             comparison = np.array_equal(equal_arrays_to_compre, array_to_test)
             print(comparison)
             temp_list =[]
             if comparison== True:
                print ("yes")
                time= gp.index[0]
                templist0.append(gp)
                gp_split = np.array_split(gp, number_of_tap)#WE split by number of tap to get df for each tap in timesteap
                for df in  gp_split:
                 print(df[number_of_time_step_to_skip:])
                 temp_list.append(df[number_of_time_step_to_skip:])#the number of timestep to skip for each tap
                 redy = pd.concat(temp_list, axis=0)  
                x = redy.groupby('Valve_no').mean() 
           
                date_of_row = x.transpose()
                X1=  date_of_row.iloc[5]
                CO2_Avg_list = list(X1)
    
                df = pd.DataFrame(CO2_Avg_list, columns_vale) 
                df=df.transpose()
                DATA.append(df)
                templist_of_date.append(time)
                vertical_stack = pd.concat(DATA, axis=0)
           
             elif comparison== False:

                print ("NO")
                time= gp.index[0]
          
                gp.loc[:,'CO2_Avg'] = np.NaN
                x = gp.groupby('Valve_no').mean() 
                date_of_row = x.transpose()
                X1=  date_of_row.iloc[5]
           
            
                CO2_Avg_list = np.empty((len(columns_vale)))
                CO2_Avg_list[:] = np.nan
                df = pd.DataFrame(CO2_Avg_list, columns_vale) 
                df=df.transpose()
                DATA.append(df)
                templist_of_date.append(time)


 vertical_stack = pd.concat(DATA, axis=0)
 vertical_stack.insert(0, "TIMESTAMP", templist_of_date)
 vertical_stack.to_csv(output_file_to_plot, index=False)  






 Plot = pd.read_csv('data_to_plot_co2.csv', index_col='TIMESTAMP',parse_dates=True )#dayfirst=True

 pandas_bokeh.output_file("Interactive Plot_co2.html")
 Plot.plot_bokeh(rangetool=True,figsize=(figsize_of_html_x, figsize_of_html_y))


 pandas_bokeh.output_file("Interactive Plot_no_co2.html")
 plotdata_NO_CO2 = pd.read_csv('data_no_co2data.csv', index_col='TIMESTAMP',parse_dates=True )#dayfirst=True

 plotdata_NO_CO2.plot_bokeh(rangetool=True,figsize=(figsize_of_html_x, figsize_of_html_y))


from time import time, sleep
while True:
    sleep(1200 - time() % 1200)
    print ("a")
    run_code()
	# thing to run


#import schedule
#import time

#def job():
#    print("I'm working...")

#schedule.every(60).minutes.do(run_code)
#schedule.every().hour.do(run_code)
#schedule.every().day.at("10:30").do(run_code)

# Creating a loop so that the scheduling task keeps on running all time
#while True:
#Checks whether the scheduled task is running or not
# schedule.run_pending()


      
      
"""

from redis import Redis
from rq import Queue


from redis import Redis
from rq import Queue

q = Queue(connection=Redis())
job = Queue.enqueue_in(timedelta(seconds=10), run_code)
import time as t
#schedule.every(24).hours.do(run_code)
#schedule.every(900).seconds.do(run_code)
schedule.every().day.at("15:37").do(run_code)
while 10:
  schedule.run_pending()
  t.sleep(10)

"""










