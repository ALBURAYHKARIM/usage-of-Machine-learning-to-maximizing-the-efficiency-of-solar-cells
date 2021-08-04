# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 12:56:55 2021

@author: Abdul
"""
import docx2txt
import pandas as pd
import numpy as np

# replace following line with location of your .docx file
# MY_TEXT = docx2txt.process("VVsJ1.docx")

# print(MY_TEXT)
starting_filenumber = 20001
ending_filenumber = 30000
for i in range(starting_filenumber,ending_filenumber+1):
    try:
        MY_TEXT = docx2txt.process("VVsJ.25prameters.%d.docx"%(int(i)))
        fo = open("VVsJ%d.txt"%(int(i)), "w")
        fo.write(MY_TEXT)
        fo.close()
    except:
        continue 
        

Voc = []
Jsc = []
FF = []
eta = []
cc=[]
Extrapolatedvo=[]
ExtrapolatedCu=[]
ExtrapolatedFF=[]
Extrapolatedefa=[]

c= 20001
for i in range(starting_filenumber,ending_filenumber+1):
    try:
        fo = open('VVsJ%d.txt' %(int(c))) 
        x= []
        for rec in fo:
            x.append(rec)
    
        
        line_eff = x[-5].split()
        line_FF = x[-7].split()
        line_Jsc = x[-9].split()
        line_Voc = x[-11].split()
        voltage = line_Voc[2]
        try:
            extavo= line_Voc[4]
        except:
            extavo= '-'
            pass
        
        current = line_Jsc[2]
        try:
            extacu= line_Jsc[4]
        except:
            extacu= '-'
            pass
        
        Feild_Factor= line_FF[2]
        try:
            extaFF= line_FF[4]
        except:
            extaFF= '-'
            pass
        
        efficiency= line_eff[2]
        try:
            extaeff= line_eff[4]
        except:
            extaeff= '-'
            pass
        
        
    except:
        Voc.append('-')
        Jsc.append('-')
        FF.append('-')
        eta.append('-')
        cc.append('-')
        Extrapolatedvo.append('-')
        ExtrapolatedCu.append('-')
        ExtrapolatedFF.append('-')
        Extrapolatedefa.append('-')
        c=c+1
        continue
    
    # voltage = line_Voc[2]
    # current = line_Jsc[2]
    # Feild_Factor= line_FF[2]
    # efficiency= line_eff[2]
    Voc.append(float(voltage))
    Jsc.append(float(current))
    FF.append(float(Feild_Factor))
    eta.append(float(efficiency))
    cc.append(float(c))
    Extrapolatedvo.append(extavo)
    ExtrapolatedCu.append(extacu)
    ExtrapolatedFF.append(extaFF)
    Extrapolatedefa.append(extaeff)
    c=c+1
data = pd.DataFrame({
    'c' :(cc),
    'Voc' : (Voc),
    'Jsc' : (Jsc),
    'FF' : (FF),
    'eta': (eta),
    'extvo':(Extrapolatedvo),
    'extcu':(ExtrapolatedCu),
    'extFF':(ExtrapolatedFF),
    'exteff':(Extrapolatedefa),
    




    })
data.to_excel("final_111100projectdata.xlsx")

    
    
    
    
#         L = i.split()

#         if word in L:
#             linenumber = c
#         c= c+1
    
#     l = x[linenumber-1]
#     l = l.split()
#     energy= l[2]



# with open("Output.txt", "w") as text_file:
#     print(MY_TEXT, file=text_file)