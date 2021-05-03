# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 15:48:20 2020
https://moonbooks.org/Articles/How-to-find-all-combinations-from-a-list-of-elements-in-python-/
@author: yaron
"""
from sklearn.metrics import mean_squared_error
import numpy as np
import scipy.stats
# Import pandas package  
import pandas as pd  
from itertools import combinations
from sklearn.metrics import r2_score

def index_f(B1,B2):
  result=(B1-B2)/(B1+B2)
  return  result 






L = ['a','b','c','d',"e","f"]
L2 = ['a','b','c','d',"e","X"]
L3 = ['a','b','c','d',"C","X"]


for i in combinations(L2,2):
    print(i)
    index  =i[0]+i[1] 
    
c2 = [i for i in combinations(L,2)]

print(c2)

#נמצא את כל הצירופים ברשימה הראשונה ויצור רשימה ארוכה שכוללת
#את כל הצריפים אפשרים
#ואז נקח כל צירוף ונעשה ממנו סדרת זמן תשווה למשתנה המסביר

def calculateSquare(n):
    return n*n

B1 = [9,8]
B2 = [9,9]

numbers = (1, 2, 3, 4)
result = map(index_f, B1,B2)
numbersSquare = set(result)
print(numbersSquare)
    
# making data frame  
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")  
data = pd.read_csv('C:/Users/yaron/Desktop/TEST_BAND.csv')  
Y = data["Y"].tolist()    
# list(data) or 
L=list(data.columns)     
del L[0]
combinations_vale = [i for i in combinations(L,2)]
# calling head() method   
# storing in new variable  
data_top = data.head()  
R2 =[]
MSE =[]
B1 =[]
B2 =[]


number = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]#index of nubmer of combisne
for band in number:
    print (band)
    a=combinations_vale[band][0]
    print(a)
    b=combinations_vale[band][1]  
    x = data[[a,b]]#here we have a list of of two band that need to turn indo index   
    index_list_vale=list(map(index_f, x[a].tolist(), x[b].tolist())) 
   # RR = r2_score([1,1,1,1,1], index_list_vale)
    #make the list that wil store the new datafreame
    
    R2.append(r2_score(Y, index_list_vale))
    MSE.append(mean_squared_error(Y, index_list_vale))
  

    B1.append(a)
    B2.append(b)
    
    #MSE =

 
    
    
    
    #GET the data to new datafrme
    
df = pd.DataFrame(list(zip(R2,MSE,B1, B2)), 
               columns =['R2',"MSE",'B1','B2']) 

    
df.to_csv('C:/INCA MEAN/test.csv')    


mean_squared_error(y_true, y_pred)

# display  
data_top  
ages = titanic["Age"]


#עוובר על כל שורה ולוקח את כל ערכים והפוך לרשימה ,מוציא את ערך המסביר משם
#כל ערך יצטרך לשמור גם על מספר ערוץ שלו
