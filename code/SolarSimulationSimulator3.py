# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 09:56:36 2021

@author: Abdul
"""

import deltapv as dpv
from jax import numpy as jnp, grad
import os,sys
import subprocess as SC
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as pl


frontworkfunction = 4.0964
backworkfunction = 5.1738 



Chi_HTM= 2.0355
Eg_HTM= 3.3645
eps_HTM= 16.161
Nc_HTM=1e20
Nv_HTM=1e18
mn_HTM=4.9727
mp_HTM=436.13
tn_HTM=1e-3
tp_HTM=1e-3
A_HTM=2e4
thickness_HTM = 0.0004989
numacceptor = 1e9

Chi_ETM= 4.0303
Eg_ETM= 3.9375
eps_ETM= 7.3402
Nc_ETM=1e18
Nv_ETM=1e18
mn_ETM=175.49
mp_ETM= 5.4444
tn_ETM=1e-3
tp_ETM=1e-3
A_ETM=2e4
thickness_ETM = 0.0001707
num_donor = 1e9

Chi_absorber=3.9,
Eg_Absorber=1.5,
eps_absorber=10,
Nc_absorber=3.9e18,
Nv_absorber=2.7e18,
mn_absorber=2,
mp_absorber=2,
tn_absorber=1e-3,
tp_absorber=1e-3,
A_absorber=2e4,
thickness_absorber= 0.0007321


######
######
######
######
######
##### low :

    

low_frontworkfunction = 4
low_backworkfunction = 4.5 



low_Chi_HTM= 2.0
low_Eg_HTM= 1.3
low_eps_HTM= 2
low_Nc_HTM=2.2e19
low_Nv_HTM=3.9e19
low_mn_HTM=1e-2
low_mp_HTM=1e-2
low_tn_HTM=1e-5
low_tp_HTM=1e-5
low_A_HTM=2e4
low_thickness_HTM = 0.000005
low_numacceptor = 1e13

low_Chi_ETM= 3.8
low_Eg_ETM= 1.55
low_eps_ETM= 2
low_Nc_ETM=2e19
low_Nv_ETM=6e19
low_mn_ETM=1e-2
low_mp_ETM= 1e-2
low_tn_ETM=1e-5
low_tp_ETM=1e-5
low_A_ETM=2e4
low_thickness_ETM = 0.000001
low_num_donor = 1e13

low_Chi_absorber=3.5
low_Eg_Absorber=0.6
low_eps_absorber=2
low_Nc_absorber=2.2e19
low_Nv_absorber=3.9e19
low_mn_absorber=1e-2
low_mp_absorber=1e-2
low_tn_absorber=1e-5
low_tp_absorber=1e-5
low_A_absorber=2e4
low_thickness_absorber= 0.00003



##### high:

    


high_frontworkfunction = 5
high_backworkfunction = 5.5 



high_Chi_HTM= 4.2
high_Eg_HTM= 2.55
high_eps_HTM= 18
high_Nc_HTM=2.5e21
high_Nv_HTM=2.5e21
high_mn_HTM=1e2
high_mp_HTM=1e2
high_tn_HTM=1e-3
high_tp_HTM=1e-3
high_A_HTM=2.1e4
high_thickness_HTM = 0.00005
high_numacceptor = 1e17

high_Chi_ETM= 4.8
high_Eg_ETM= 4
high_eps_ETM= 18
high_Nc_ETM=1e21
high_Nv_ETM=1.8e21
high_mn_ETM=1e2
high_mp_ETM= 1e2
high_tn_ETM=1e-3
high_tp_ETM=1e-3
high_A_ETM=2.1e4
high_thickness_ETM = 0.00005
high_num_donor = 2e17

high_Chi_absorber= 4.5
high_Eg_Absorber= 1.5
high_eps_absorber=18
high_Nc_absorber=2.5e21
high_Nv_absorber=2.5e21
high_mn_absorber=1e2
high_mp_absorber=1e2
high_tn_absorber=1e-3
high_tp_absorber=1e-3
high_A_absorber=2.1e4
high_thickness_absorber= 0.001











front = [frontworkfunction]
back = [backworkfunction]



HTM = [Chi_HTM,
    Eg_HTM,
    eps_HTM,
    Nc_HTM,
    Nv_HTM,
    mn_HTM,
    mp_HTM,
    tn_HTM,
    tp_HTM,
    A_HTM,
    thickness_HTM,
    numacceptor]

ETM = [Chi_ETM,
    Eg_ETM,
    eps_ETM,
    Nc_ETM,
    Nv_ETM,
    mn_ETM,
    mp_ETM,
    tn_ETM,
    tp_ETM,
    A_ETM,
    thickness_ETM,
    num_donor]

absorber = [Chi_absorber,
            Eg_Absorber,
            eps_absorber,
            Nc_absorber,
            Nv_absorber,
            mn_absorber,
            mp_absorber,
            tn_absorber,
            tp_absorber,
            A_absorber,
            thickness_absorber]




c = 0
for i in HTM:
    HTM[c]=[]
    c=c+1


c = 0
for i in ETM:
    ETM[c]=[]
    c=c+1


c = 0
for i in absorber:
    absorber[c]=[]
    c=c+1


c = 0
for i in front:
    front[c]=[]
    c=c+1


c = 0
for i in back:
    back[c]=[]
    c=c+1


for i in range(0,1000000):
    
    front[0].extend([random.uniform(low_frontworkfunction,high_frontworkfunction)])
    back[0].extend([random.uniform(low_backworkfunction,high_backworkfunction)])

    
    
    HTM[0].extend([random.uniform(low_Chi_HTM,high_Chi_HTM)])
    HTM[1].extend([random.uniform(low_Eg_HTM,high_Eg_HTM)])
    HTM[2].extend([random.uniform(low_eps_HTM,high_eps_HTM)])
    HTM[3].extend([random.uniform(low_Nc_HTM,high_Nc_HTM)])
    HTM[4].extend([random.uniform(low_Nv_HTM,high_Nv_HTM)])
    HTM[5].extend([random.uniform(low_mn_HTM,high_mn_HTM)])
    HTM[6].extend([random.uniform(low_mp_HTM,high_mp_HTM)])
    HTM[7].extend([random.uniform(low_tn_HTM,high_tn_HTM)])
    HTM[8].extend([random.uniform(low_tp_HTM,high_tp_HTM)])
    HTM[9].extend([random.uniform(low_A_HTM,high_A_HTM)])
    HTM[10].extend([random.uniform(low_thickness_HTM,high_thickness_HTM)])
    HTM[11].extend([random.uniform(low_numacceptor,high_numacceptor)])


    ETM[0].extend([random.uniform(low_Chi_ETM,high_Chi_ETM)])
    ETM[1].extend([random.uniform(low_Eg_ETM,high_Eg_ETM)])
    ETM[2].extend([random.uniform(low_eps_ETM,high_eps_ETM)])
    ETM[3].extend([random.uniform(low_Nc_ETM,high_Nc_ETM)])
    ETM[4].extend([random.uniform(low_Nv_ETM,high_Nv_ETM)])
    ETM[5].extend([random.uniform(low_mn_ETM,high_mn_ETM)])
    ETM[6].extend([random.uniform(low_mp_ETM,high_mp_ETM)])
    ETM[7].extend([random.uniform(low_tn_ETM,high_tn_ETM)])
    ETM[8].extend([random.uniform(low_tp_ETM,high_tp_ETM)])
    ETM[9].extend([random.uniform(low_A_ETM,high_A_ETM)])
    ETM[10].extend([random.uniform(low_thickness_ETM,high_thickness_ETM)])
    ETM[11].extend([random.uniform(low_num_donor,high_num_donor)])
 
    absorber[0].extend([random.uniform(low_Chi_absorber,high_Chi_absorber)])
    absorber[1].extend([random.uniform(low_Eg_Absorber,high_Eg_Absorber)])
    absorber[2].extend([random.uniform(low_eps_absorber,high_eps_absorber)])
    absorber[3].extend([random.uniform(low_Nc_absorber,high_Nc_absorber)])
    absorber[4].extend([random.uniform(low_Nv_absorber,high_Nv_absorber)])
    absorber[5].extend([random.uniform(low_mn_absorber,high_mn_absorber)])
    absorber[6].extend([random.uniform(low_mp_absorber,high_mp_absorber)])
    absorber[7].extend([random.uniform(low_tn_absorber,high_tn_absorber)])
    absorber[8].extend([random.uniform(low_tp_absorber,high_tp_absorber)])
    absorber[9].extend([random.uniform(low_A_absorber,high_A_absorber)])
    absorber[10].extend([random.uniform(low_thickness_absorber,high_thickness_absorber)])
    
    # absorber[0].extend([random.uniform(low_thickness_absorber,high_thickness_absorber)])





# print(HTM)
# print(ETM)
# print(absorber)


Chi_HTM_=[]
Eg_HTM_=[]
eps_HTM_=[]
Nc_HTM_=[]
Nv_HTM_=[]
mn_HTM_=[]
mp_HTM_=[]
tn_HTM_=[]
tp_HTM_=[]
A_HTM_=[]
thickness_HTM_ = []
numacceptor_ = []



Chi_ETM_=[]
Eg_ETM_=[]
eps_ETM_=[]
Nc_ETM_=[]
Nv_ETM_=[]
mn_ETM_=[]
mp_ETM_=[]
tn_ETM_=[]
tp_ETM_=[]
A_ETM_=[]
thickness_ETM_ = []
num_donor_ = []


Chi_absorber_=[]
Eg_Absorber_=[]
eps_absorber_=[]
Nc_absorber_=[]
Nv_absorber_=[]
mn_absorber_=[]
mp_absorber_=[]
tn_absorber_=[]
tp_absorber_=[]
A_absorber_=[]
thickness_absorber_=[]

current_ = []
voltage_ = []
effeciency_ =[] 
r=0
c=0
for i in range(0,1000000):
    
    frontworkfunction = float(front[0][c])
    backworkfunction =  float(back[0][c])   
    
    Chi_HTM=float(HTM[0][c])
    Eg_HTM=float(HTM[1][c])
    eps_HTM=float(HTM[2][c])
    Nc_HTM=float(HTM[3][c])
    Nv_HTM=float(HTM[4][c])
    mn_HTM=float(HTM[5][c])
    mp_HTM=float(HTM[6][c])
    tn_HTM=float(HTM[7][c])
    tp_HTM=float(HTM[8][c])
    A_HTM=float(HTM[9][c])
    thickness_HTM = float(HTM[10][c])
    numacceptor = float(HTM[11][c])

    
    
    Chi_ETM=float(ETM[0][c])
    Eg_ETM=float(ETM[1][c])
    eps_ETM=float(ETM[2][c])
    Nc_ETM=float(ETM[3][c])
    Nv_ETM=float(ETM[4][c])
    mn_ETM=float(ETM[5][c])
    mp_ETM=float(ETM[6][c])
    tn_ETM=float(ETM[7][c])
    tp_ETM=float(ETM[8][c])
    A_ETM=float(ETM[9][c])
    thickness_ETM = float(ETM[10][c])
    num_donor = float(ETM[11][c])



    Chi_absorber= float(absorber[0][c])
    Eg_Absorber=float(absorber[1][c])
    eps_absorber=float(absorber[2][c])
    Nc_absorber=float(absorber[3][c])
    Nv_absorber=float(absorber[4][c])
    mn_absorber=float(absorber[5][c])
    mp_absorber=float(absorber[6][c])
    tn_absorber=float(absorber[7][c])
    tp_absorber=float(absorber[8][c])
    A_absorber=float(absorber[9][c])
    thickness_absorber= float(absorber[10][c])
    
    if (Chi_ETM - frontworkfunction) > 0:
        c=c+1
        print('1' ,Chi_ETM, frontworkfunction)
        continue
    elif (Chi_ETM - Chi_absorber) < 0:
        c=c+1
        print('2',Chi_ETM , Chi_absorber)
        continue
    elif (backworkfunction-Chi_HTM-Eg_HTM) > 0:
        c=c+1
        print('3',backworkfunction,Chi_HTM,Eg_HTM)
        continue
    elif (Chi_HTM+Eg_HTM-Chi_absorber-Eg_Absorber) > 0:
        c=c+1
        print('4',Chi_HTM,Eg_HTM,Chi_absorber,Eg_Absorber)
        continue
    elif (Chi_absorber-Chi_ETM)>0:
        c=c+1
        print('5',Chi_absorber,Chi_ETM)
        continue
    else: 
        
        material_HTM = dpv.create_material(Chi=Chi_HTM,
                                                Eg=Eg_HTM,
                                                eps=eps_HTM,
                                                Nc=Nc_HTM,
                                                Nv=Nv_HTM,
                                                # Ndop= 1,
                                                mn=mn_HTM,
                                                mp=mp_HTM,
                                                tn=tn_HTM,
                                                tp=tp_HTM,
                                                A=A_HTM)    
        
            
        material_absorber = dpv.create_material(Chi=Chi_absorber,
                                                Eg=Eg_Absorber,
                                                eps=eps_absorber,
                                                Nc=Nc_absorber,
                                                Nv=Nv_absorber,
                                                # Ndop= 1,
                                                mn=mn_absorber,
                                                mp=mp_absorber,
                                                tn=tn_absorber,
                                                tp=tp_absorber,
                                                A=A_absorber)    
        
        material_ETM = dpv.create_material(Chi=Chi_ETM,
                                                Eg=Eg_ETM,
                                                eps=eps_ETM,
                                                Nc=Nc_ETM,
                                                Nv=Nv_ETM,
                                                mn=mn_ETM,
                                                mp=mp_ETM,
                                                tn=tn_ETM,
                                                tp=tp_ETM,
                                                A=A_ETM)    
        
        
        des = dpv.make_design(n_points=500,
                              Ls=[thickness_ETM, thickness_absorber, thickness_HTM],
                              mats=[material_ETM, material_absorber, material_HTM],
                              Ns=[num_donor, 0, -numacceptor],
                              Snl=1.16e7, Snr=1.16e7, Spl=1.16e7, Spr=1.16e7,
                              PhiM0 = frontworkfunction ,
                              PhiML = backworkfunction)
                              
    
        ls = dpv.incident_light() 
        try:
                              
            results = dpv.simulate(des,ls)    
        except:
            c=c+1
            continue
        else:
               
            voltage = results["iv"][0]
            current = results["iv"][1]
            current = (10**3)*current #mA/cm^2
            effeciency = results["eff"]
            
            
            
            current_.append(float(current[0]))
            voltage_.append(float(voltage[-1]))
            effeciency_.append(float(effeciency))
            Chi_HTM_.append(float(Chi_HTM))
            Eg_HTM_.append(float(Eg_HTM))
            eps_HTM_.append(float(eps_HTM))
            Nc_HTM_.append(float(Nc_HTM))
            Nv_HTM_.append(float(Nv_HTM))
            mn_HTM_.append(float(mn_HTM))
            mp_HTM_.append(float(mp_HTM))
            tn_HTM_.append(float(tn_HTM))
            tp_HTM_.append(float(tp_HTM))
            A_HTM_.append(float(A_HTM))
            thickness_HTM_.append(float(thickness_HTM))
            numacceptor_.append(float(numacceptor))
                
            
            Chi_ETM_.append(float(Chi_ETM))
            Eg_ETM_.append(float(Eg_ETM))
            eps_ETM_.append(float(eps_ETM))
            Nc_ETM_.append(float(Nc_ETM))
            Nv_ETM_.append(float(Nv_ETM))
            mn_ETM_.append(float(mn_ETM))
            mp_ETM_.append(float(mp_ETM))
            tn_ETM_.append(float(tn_ETM))
            tp_ETM_.append(float(tp_ETM))
            A_ETM_.append(float(A_ETM))
            thickness_ETM_.append(float(thickness_ETM))
            num_donor_.append(float(num_donor))  
            
            Chi_absorber_.append(float(Chi_absorber))
            Eg_Absorber_.append(float(Eg_Absorber))
            eps_absorber_.append(float(eps_absorber))
            Nc_absorber_.append(float(Nc_absorber))
            Nv_absorber_.append(float(Nv_absorber))
            mn_absorber_.append(float(mn_absorber))
            mp_absorber_.append(float(mp_absorber))
            tn_absorber_.append(float(tn_absorber))
            tp_absorber_.append(float(tp_absorber))
            A_absorber_.append(float(A_absorber))
            thickness_absorber_.append(float(thickness_absorber))
        
            c =c+1
            r=r+1
            if r==10000 :
                break
        
    
data = pd.DataFrame({

        
        'Chi_HTM_' : (Chi_HTM_),
        'Eg_HTM_' : (Eg_HTM_),
        'eps_HTM_': (eps_HTM_),
        'Nc_HTM_': (Nc_HTM_),
        'Nv_HTM_': (Nv_HTM_),
        'mn_HTM_': (Nv_HTM_),
        'mp_HTM_': (mp_HTM_),
        'tn_HTM_': (tn_HTM_),
        'tp_HTM_': (tp_HTM_),
        'A_HTM_': (A_HTM_),
        'thickness_HTM_': (thickness_HTM_),
        'numacceprot_' : (numacceptor_),
        
        'Chi_ETM_' : (Chi_ETM_),
        'Eg_ETM_' : (Eg_ETM_),
        'eps_ETM_': (eps_ETM_),
        'Nc_ETM_': (Nc_ETM_),
        'Nv_ETM_': (Nv_ETM_),
        'mn_ETM_': (Nv_ETM_),
        'mp_ETM_': (mp_ETM_),
        'tn_ETM_': (tn_ETM_),
        'tp_ETM_': (tp_ETM_),
        'A_ETM_': (A_ETM_),
        'thickness_ETM_': (thickness_ETM_),
        'num_donor_' : (num_donor_),
        
        'Chi_absorber_' : (Chi_absorber_),
        'Eg_absorber_' : (Eg_Absorber_),
        'eps_absorber_': (eps_absorber_),
        'Nc_absorber_': (Nc_absorber_),
        'Nv_absorber_': (Nv_absorber_),
        'mn_absorber_': (Nv_absorber_),
        'mp_absorber_': (mp_absorber_),
        'tn_absorber_': (tn_absorber_),
        'tp_absorber_': (tp_absorber_),
        'A_absorber_': (A_absorber_),
        'thickness_absorber_' : (thickness_absorber_),
        
        
        'OCvoltage' : (voltage_),
        'SCcurrent' : (current_),
        'effeciency' : (effeciency_)
        


    })
data.to_excel("___10000datapoints.xlsx")


    


