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


data = pd.read_excel('CLEANED-SCAPS-35000-.xlsx')
features =data[['WF (eV)',	'WB (eV)',	'TE (mum)','10^DCE (1/cm3)',	'EGE (eV)',	'EME (cm2/V.s)',	'HME (cm2/V.s)',	'10^AE (1/cm.eV1/2)',	'10^CBE (1/cm3)',	'10^VBE (1/cm3)',	'AEE (eV)'	,'DE'	,'TP (mum)',	'TH (mum)',	'10^ACH (1/cm3)',	'EGH (eV)',	'EMH (cm2/V.s)',	'HMH (cm2/V.s)',	'10^AH (1/cm.eV1/2)',	'10^CBH (1/cm3)',	'10^VBH (1/cm3)',	'AEH (eV)'	,'DH',	'EGP (eV)',	'AEP (eV)',	'Voc',	'Jsc',	'FF',	'eta']]


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
                        columns = ['WF (eV)',	'WB (eV)',	'TE (mum)','10^DCE (1/cm3)',	'EGE (eV)',	'EME (cm2/V.s)',	'HME (cm2/V.s)',	'10^AE (1/cm.eV1/2)',	'10^CBE (1/cm3)',	'10^VBE (1/cm3)',	'AEE (eV)'	,'DE'	,'TP (mum)',	'TH (mum)',	'10^ACH (1/cm3)',	'EGH (eV)',	'EMH (cm2/V.s)',	'HMH (cm2/V.s)',	'10^AH (1/cm.eV1/2)',	'10^CBH (1/cm3)',	'10^VBH (1/cm3)',	'AEH (eV)'	,'DH',	'EGP (eV)',	'AEP (eV)',	'Voc',	'Jsc',	'FF',	'eta'])



import seaborn as sns
#Using Pearson Correlation
plt.figure(figsize=(5*12,5*10))
cor = panda_df.corr()
sns.heatmap(cor, annot=True, cmap=plt.cm.binary)
plt.savefig('CLEANED-SCAPS-35000-heat.png')
plt.show()






