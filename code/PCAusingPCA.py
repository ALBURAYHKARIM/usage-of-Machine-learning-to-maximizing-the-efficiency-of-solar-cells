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



data = pd.read_excel('___1000datapoints.xlsx')
#features_in = data[['Chi_HTM_',	'Eg_HTM_'	,'eps_HTM_',	'Nc_HTM_',	'Nv_HTM_',	'mn_HTM_'	,'mp_HTM_',	'tn_HTM_',	'tp_HTM_',	'A_HTM_',	'thickness_HTM_',	'numacceprot_',	'Chi_ETM_',	'Eg_ETM_'	,'eps_ETM_'	,'Nc_ETM_'	,'Nv_ETM_',	'mn_ETM_',	'mp_ETM_',	'tn_ETM_',	'tp_ETM_',	'A_ETM_',	'thickness_ETM_',	'num_donor_',	'Chi_absorber_',	'Eg_absorber_',	'eps_absorber_',	'Nc_absorber_',	'Nv_absorber_',	'mn_absorber_',	'mp_absorber_',	'tn_absorber_',	'tp_absorber_',	'A_absorber_',	'thickness_absorber_',	'OCvoltage',	'SCcurrent',	'effeciency','FF']]
features_in = data[['Chi_HTM_' ,	'Eg_HTM_'	,'eps_HTM_',	'Nc_HTM_',	'Nv_HTM_',	'mn_HTM_'	,'mp_HTM_',	'tn_HTM_',	'tp_HTM_',	'A_HTM_',	'thickness_HTM_',	'numacceprot_',	'Chi_ETM_',	'Eg_ETM_'	,'eps_ETM_'	,'Nc_ETM_'	,'Nv_ETM_',	'mn_ETM_',	'mp_ETM_',	'tn_ETM_',	'tp_ETM_',	'A_ETM_',	'thickness_ETM_',	'num_donor_',	'Chi_absorber_',	'Eg_absorber_',	'eps_absorber_',	'Nc_absorber_',	'Nv_absorber_',	'mn_absorber_',	'mp_absorber_',	'tn_absorber_',	'tp_absorber_',	'A_absorber_',	'thickness_absorber_']]
#features_in = data[['Chi_HTM_',	'Eg_HTM_','eps_HTM_',	'Nc_HTM_',	'Nv_HTM_']]
features_out = data[['OCvoltage']]
names = ['Chi_HTM_',	'Eg_HTM_'	,'eps_HTM_',	'Nc_HTM_',	'Nv_HTM_',	'mn_HTM_'	,'mp_HTM_',	'tn_HTM_',	'tp_HTM_',	'A_HTM_',	'thickness_HTM_',	'numacceprot_',	'Chi_ETM_',	'Eg_ETM_'	,'eps_ETM_'	,'Nc_ETM_'	,'Nv_ETM_',	'mn_ETM_',	'mp_ETM_',	'tn_ETM_',	'tp_ETM_',	'A_ETM_',	'thickness_ETM_',	'num_donor_',	'Chi_absorber_',	'Eg_absorber_',	'eps_absorber_',	'Nc_absorber_',	'Nv_absorber_',	'mn_absorber_',	'mp_absorber_',	'tn_absorber_',	'tp_absorber_',	'A_absorber_',	'thickness_absorber_',	'OCvoltage',	'SCcurrent',	'effeciency','FF']


X = np.array(features_in)
X=X.T
Y = np.array(features_out) 
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
# print(X.dtype)
workbook.save("test.xls")
pca = PCA(n_components=15)
pca.fit(X)

print('cov matrix = \n',pca.get_covariance())
print('eigen vectors = \n',pca.components_)
print('eigen values = \n',pca.singular_values_)
workbook = xlwt.Workbook()
sheet = workbook.add_sheet("Sheet")
PCA_vectors= pca.components_
PCA_Value= pca.singular_values_
PCA_vectors=np.array(PCA_vectors)
PCA_Value= np.array(PCA_Value)

for i in range(len(PCA_vectors)):
    for j in range(len(PCA_vectors[i])):
        sheet.write(i, j, PCA_vectors[i][j])
# print(X.dtype)
workbook.save("Eigenvectors.xls")

workbook = xlwt.Workbook()
sheet = workbook.add_sheet("Sheet")
j=0
for i in range(len(PCA_Value)):
    sheet.write(i, j, PCA_Value[i])
# print(X.dtype)
workbook.save("Eigenvalue.xls")
Z = pca.transform(X)

        
feature0 = []
feature1 = []
feature2 = []
feature3 = []
feature4 = []
feature5 = []
feature6 = []
feature7 = []
voltage_ = []
current_ = []
feildfactor_ = []
c=0
for i in Z[:,0]:
    feature0.append(Z[:,0][c])
    feature1.append(Z[:,1][c])
    feature2.append(Z[:,2][c])
    feature3.append(Z[:,3][c])
    feature4.append(Z[:,4][c])
    # feature5.append(Z[:,5][c])
    # feature6.append(Z[:,6][c])
    # feature7.append(Z[:,7][c])
    voltage_.append(data['OCvoltage'][c])
    current_.append(data['SCcurrent'][c])
    feildfactor_.append(data['FF'][c])
    c=c+1
    

data = pd.DataFrame({

        
        'feature0' : (feature0),
        'feature1' : (feature1),
        'feature2' : (feature2),
        'feature3' : (feature3),
        'feature4' : (feature4),
        # 'feature5' : (feature5),
        # 'feature6' : (feature6),
        # 'feature7' : (feature7),
        'voltage' : (voltage_),
        'current' : (current_),
        'feild factor' : (feildfactor_)

     })
data.to_excel('PCA11data.xlsx')




