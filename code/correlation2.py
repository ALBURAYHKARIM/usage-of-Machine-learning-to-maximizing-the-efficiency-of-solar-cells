# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 09:22:29 2021

@author: Abdul
"""


import os,sys
import subprocess as SC
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn import preprocessing
import statistics
from numpy import asarray


data = pd.read_excel('delta-pv-10000.xlsx')
features = data[['Chi_HTM_',	'Eg_HTM_'	,'eps_HTM_',	'Nc_HTM_',	'Nv_HTM_',	'mn_HTM_'	,'mp_HTM_',	'tn_HTM_',	'tp_HTM_',	'A_HTM_',	'thickness_HTM_',	'numacceprot_',	'Chi_ETM_',	'Eg_ETM_'	,'eps_ETM_'	,'Nc_ETM_'	,'Nv_ETM_',	'mn_ETM_',	'mp_ETM_',	'tn_ETM_',	'tp_ETM_',	'A_ETM_',	'thickness_ETM_',	'num_donor_',	'Chi_absorber_',	'Eg_absorber_',	'eps_absorber_',	'Nc_absorber_',	'Nv_absorber_',	'mn_absorber_',	'mp_absorber_',	'tn_absorber_',	'tp_absorber_',	'A_absorber_',	'thickness_absorber_',	'OCvoltage',	'SCcurrent',	'effeciency','FF']]


X = np.array(features)
X=X.T
print(X)

for i in range(len(X)):
    for j in range(len(X[i])):
        X[i][j] = float(X[i][j])

c=0
for i in X:
    X[c] = preprocessing.scale(X[c].astype('float64'))
    c=c+1

X=X.T

import xlwt
workbook = xlwt.Workbook()
sheet = workbook.add_sheet("Sheet")

for i in range(len(X)):
    for j in range(len(X[i])):
        sheet.write(i, j, X[i][j])
workbook.save("test.xls")


panda_df = pd.DataFrame(data = X, 
                        columns = ['Chi_HTM_',	'Eg_HTM_'	,'eps_HTM_',	'Nc_HTM_',	'Nv_HTM_',	'mn_HTM_'	,'mp_HTM_',	'tn_HTM_',	'tp_HTM_',	'A_HTM_',	'thickness_HTM_',	'numacceprot_',	'Chi_ETM_',	'Eg_ETM_'	,'eps_ETM_'	,'Nc_ETM_'	,'Nv_ETM_',	'mn_ETM_',	'mp_ETM_',	'tn_ETM_',	'tp_ETM_',	'A_ETM_',	'thickness_ETM_',	'num_donor_',	'Chi_absorber_',	'Eg_absorber_',	'eps_absorber_',	'Nc_absorber_',	'Nv_absorber_',	'mn_absorber_',	'mp_absorber_',	'tn_absorber_',	'tp_absorber_',	'A_absorber_',	'thickness_absorber_',	'OCvoltage',	'SCcurrent',	'effeciency','FF'])



import seaborn as sns
#Using Pearson Correlation
plt.figure(figsize=(5*12,5*10))
cor = panda_df.corr()
sns.heatmap(cor, annot=True, cmap=plt.cm.binary)
plt.savefig('delta-pv-10000-heat.png')
plt.show()




