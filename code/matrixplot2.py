# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 11:43:30 2021

@author: Abdul
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_excel('delta-pv-10000.xlsx')
features = data[['Chi_HTM_',	'Eg_HTM_'	,'eps_HTM_',	'Nc_HTM_',	'Nv_HTM_',	'mn_HTM_'	,'mp_HTM_',	'tn_HTM_',	'tp_HTM_',	'A_HTM_',	'thickness_HTM_',	'numacceprot_',	'Chi_ETM_',	'Eg_ETM_'	,'eps_ETM_'	,'Nc_ETM_'	,'Nv_ETM_',	'mn_ETM_',	'mp_ETM_',	'tn_ETM_',	'tp_ETM_',	'A_ETM_',	'thickness_ETM_',	'num_donor_',	'Chi_absorber_',	'Eg_absorber_',	'eps_absorber_',	'Nc_absorber_',	'Nv_absorber_',	'mn_absorber_',	'mp_absorber_',	'tn_absorber_',	'tp_absorber_',	'A_absorber_',	'thickness_absorber_',	'OCvoltage',	'SCcurrent',	'effeciency','FF']]
#features_in = data[['Chi_HTM_' ,	'Eg_HTM_'	,'eps_HTM_',	'Nc_HTM_',	'Nv_HTM_',	'mn_HTM_'	,'mp_HTM_',	'tn_HTM_',	'tp_HTM_',	'A_HTM_',	'thickness_HTM_',	'numacceprot_',	'Chi_ETM_',	'Eg_ETM_'	,'eps_ETM_'	,'Nc_ETM_'	,'Nv_ETM_',	'mn_ETM_',	'mp_ETM_',	'tn_ETM_',	'tp_ETM_',	'A_ETM_',	'thickness_ETM_',	'num_donor_',	'Chi_absorber_',	'Eg_absorber_',	'eps_absorber_',	'Nc_absorber_',	'Nv_absorber_',	'mn_absorber_',	'mp_absorber_',	'tn_absorber_',	'tp_absorber_',	'A_absorber_',	'thickness_absorber_']]

#data = pd.read_excel('CLEANED.xlsx')
#features =data[['WF (eV)',	'WB (eV)',	'TE (mum)','10^DCE (1/cm3)',	'EGE (eV)',	'EME (cm2/V.s)',	'HME (cm2/V.s)',	'10^AE (1/cm.eV1/2)',	'10^CBE (1/cm3)',	'10^VBE (1/cm3)',	'AEE (eV)'	,'DE'	,'TP (mum)',	'TH (mum)',	'10^ACH (1/cm3)',	'EGH (eV)',	'EMH (cm2/V.s)',	'HMH (cm2/V.s)',	'10^AH (1/cm.eV1/2)',	'10^CBH (1/cm3)',	'10^VBH (1/cm3)',	'AEH (eV)'	,'DH',	'EGP (eV)',	'AEP (eV)',	'Voc',	'Jsc',	'FF',	'eta']]

# print(data[['Eg_HTM_','Chi_HTM_']].head())
# features= data[['Eg_HTM_','Chi_HTM_']]
# sns.pairplot(features)
# features = data[['WF (eV)',	'WB (eV)',	'TE (mum)','10^DCE (1/cm3)',	'EGE (eV)',	'EME (cm2/V.s)',	'HME (cm2/V.s)',	'10^AE (1/cm.eV1/2)',	'10^CBE (1/cm3)',	'10^VBE (1/cm3)',	'AEE (eV)'	,'DE'	,'TP (mum)',	'TH (mum)',	'10^ACH (1/cm3)',	'EGH (eV)',	'EMH (cm2/V.s)',	'HMH (cm2/V.s)',	'10^AH (1/cm.eV1/2)',	'10^CBH (1/cm3)',	'10^VBH (1/cm3)',	'AEH (eV)'	,'DH',	'EGP (eV)',	'AEP (eV)',	'DP',	'10^CBP (1/cm3)',	'10^VBP (1/cm3)',	'EMP (cm2/V.s)',	'HMP (cm2/V.s)',	'10^DD (1/cm3)',	'10^AD (1/cm3)',	'ETV (cm/s)',	'HTV (cm/s)',	'RRC (cm3/s)',	'Voc',	'Jsc',	'FF',	'eta']]

print(features)
plt.figure(figsize=(5*12,5*10))
sns.pairplot(features,vars=features.columns[:-1])
plt.savefig('delta-pv-10000-matrix.png')
plt.show()

#[['WF (eV)',	'WB (eV)',	'TE (mum)','10^DCE (1/cm3)',	'EGE (eV)',	'EME (cm2/V.s)',	'HME (cm2/V.s)',	'10^AE (1/cm.eV1/2)',	'10^CBE (1/cm3)',	'10^VBE (1/cm3)',	'AEE (eV)'	,'DE'	,'TP (mum)',	'TH (mum)',	'10^ACH (1/cm3)',	'EGH (eV)',	'EMH (cm2/V.s)',	'HMH (cm2/V.s)',	'10^AH (1/cm.eV1/2)',	'10^CBH (1/cm3)',	'10^VBH (1/cm3)',	'AEH (eV)'	,'DH',	'EGP (eV)',	'AEP (eV)',	'DP',	'10^CBP (1/cm3)',	'10^VBP (1/cm3)',	'EMP (cm2/V.s)',	'HMP (cm2/V.s)',	'10^DD (1/cm3)',	'10^AD (1/cm3)',	'ETV (cm/s)',	'HTV (cm/s)',	'RRC (cm3/s)',	'con1',	'con2',	'con3',	'con4',	'c',	'Voc',	'Jsc',	'FF',	'eta']]
# WF (eV)	WB (eV)	TE (mum)	10^DCE (1/cm3)	EGE (eV)	EME (cm2/V.s)	HME (cm2/V.s)	10^AE (1/cm.eV1/2)	10^CBE (1/cm3)	10^VBE (1/cm3)	AEE (eV)	DE	TP (mum)	TH (mum)	10^ACH (1/cm3)	EGH (eV)	EMH (cm2/V.s)	HMH (cm2/V.s)	10^AH (1/cm.eV1/2)	10^CBH (1/cm3)	10^VBH (1/cm3)	AEH (eV)	DH   Voc	Jsc	FF	eta

