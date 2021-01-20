# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 22:45:44 2018

@author: YARON
"""
#https://www.google.com/url?hl=en&q=http://www.codeastar.com/regression-model-rmsd/&source=gmail&ust=1524427820407000&usg=AFQjCNHifodVeJahnWewBpzFUGAl7hHvhw
#http://www.ritchieng.com/machine-learning-linear-regression/
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn import metrics
df_tips = sns.load_dataset("tips")
df_tips.head(5)
sns.regplot(x="total_bill", y="tip", data=df_tips);
plt.title('add title here')
plt.text(40, 00, r'S', fontsize=20)
plt.show()
"""
We keep using the “tips” data set from the above section, get the first 200 records as learning values and the last 44 records as testing values.
"""


learning_x = df_tips[['total_bill', 'size']].values [:200]
learning_y = df_tips['tip'].values [:200]
testing_x = df_tips[['total_bill', 'size']].values[-44:]
testing_y = df_tips['tip'].values[-44:]
"""
Then we call out a machine learning model. Since we are doing regression, so we use the Linear Regression model.
"""
from sklearn.linear_model import LinearRegression
lreg = LinearRegression()
lreg.fit(learning_x, learning_y)
prediction = lreg.predict(testing_x)
"""
Now we have our predicted output, let’s compare it with the actual output..
"""
import pandas as pd
df_output_compare = pd.DataFrame({'predicted':prediction, 'actual':testing_y})
sns.regplot(x="actual", y="predicted", data=df_output_compare)
plt.show()

df_output_compare["actual"]
df_output_compare["predicted"]


df_tips["tip"]

print(np.sqrt(metrics.mean_squared_error(df_output_compare["actual"], df_output_compare["predicted"])))
RMASE=(np.sqrt(metrics.mean_squared_error(df_output_compare["actual"], df_output_compare["predicted"])))






import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn import metrics
df_tips = sns.load_dataset("tips")
df_tips.head(5)
sns.regplot(x="predicted", y="actual", data=df_output_compare);
plt.title(RMASE)
plt.text(1, 1, r'S', fontsize=20)
plt.show()

df = pd.read_csv(r'D:\RMSE_Density of trees and avg DBH.csv')

df.head(3)
sns.regplot(x="GCC", y="TREE", data=df);
plt.title(RMASE)
plt.text(1, 1, r'S', fontsize=20)
plt.show()
print(np.sqrt(metrics.mean_squared_error(df["GCC"], df["TREE"])))
RMASE=(np.sqrt(metrics.mean_squared_error(df["GCC"], df["TREE"])))

print(np.sqrt(metrics.mean_squared_error(df["GCC"], df["DBH_Average"])))
RMASE=(np.sqrt(metrics.mean_squared_error(df["GCC"], df["DBH_Average"])))

RMASE=(np.sqrt(metrics.mean_squared_error(df["GCC"], df["DBH_Average"])))

from sklearn import metrics
# calculate MAE using scikit-learn
from sklearn import metrics

print(metrics.mean_absolute_error(df["GCC"], df["TREE"]))
print(metrics.mean_absolute_error(df["GCC"], df["DBH_Average"]))


