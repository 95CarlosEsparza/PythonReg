# -*- coding: utf-8 -*-
"""
Carlos Esparza
Regression Modeling
"""
import pandas as pd
import numpy as np
import sys
import os
import statsmodels.formula.api as sm
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model

'''
choice = int(input('If this is a CSV file please press [1] to continue. If this is an EXCEl file press [2]:\n'))

#for csv files
if choice == 1:
    #prints all the csv files in folder
    print('Here are the .csv files in the current folder')
    FilesInFolder = (os.listdir())
    for f in FilesInFolder:
        if '.csv' in f:
            print(f)
    #find the cvs file you want
    filename = input('Enter the filename you want to load into python:')
    extension = ".csv"
    if extension not in filename:
        filename = filename + extension
    
    try:
        df_new = pd.read_csv(filename)
        newfilename = filename.strip('.csv') + '.xlsx'
        writer = pd.ExcelWriter(newfilename)
        df_new.to_excel(writer, index = False)
        writer.save()
        
        filename = newfilename
    except:
        print('File not found please try again!')
        sys.exit(1)
        
#for excel files
else:
    #prints all the excel files in folder
    print('Here are the .xlsx files in the current folder')
    FilesInFolder = (os.listdir())
    for f in FilesInFolder:
        if '.xlsx' in f:
            print(f)
    filename = input('Enter the filename you want to load into python:')
    extension = '.xlsx'
    if extension not in filename:
        filename = filename + extension
    else:
        filename = choice 
    
print(filename)
'''
# Reading in your data file

try:   
    filename = "Test.xlsx"
    #needs specific names right now ONLY works with Run 2 of 3 HC.xlsx
    Data = pd.read_excel(filename,sheetname="Sorted Data")
    DashMpg = Data['Dash MPG']
    MAF = Data['g/s']
    Speed = Data['mph']
    
#    est.summary()
    
    #print(DashMpg)
except:
    print('Error in reading file')
    sys.exit(1)

a_MAF = ([])
a_MPG = ([])
a_Speed = ([])
for k in range(len(DashMpg)):
    a_MAF.append(MAF[k])
    a_Speed.append(Speed[k])
    a_MPG.append(DashMpg[k])
#print(data)

df = pd.DataFrame({"A": a_MPG, "B": a_Speed, "C": a_MAF})
result = sm.ols(formula="A ~ B + C", data=df).fit()
print (result.params)

print (result.summary())

#x, y ,z = zip(*data)
#plt.plot(x,y,z,'kv')  