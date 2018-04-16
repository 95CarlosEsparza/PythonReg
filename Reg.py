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
import re

#UNCOMMENT NEXT LINE FOR DEBUG
#'''
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

#UNCOMMENT NEXT LINE FOR DEBUG
#'''
# Reading in your data file

try:   
    filename = "Test.xlsx"
    #needs specific names right now ONLY works with Run 2 of 3 HC.xlsx
    Data = pd.read_excel(filename,sheetname="Sorted Data")
    DashMpg = Data['Dash MPG']
    MAF = Data['g/s']
    Speed = Data['mph']
    Time = Data['Time']
    
#    est.summary()
    
    #print(DashMpg)
except:
    print('Error in reading file')
    sys.exit(1)

a_MAF = ([])
a_MPG = ([])
a_Speed = ([])
a_Time = ([])

for k in range(len(DashMpg)):
    a_MAF.append(MAF[k])
    a_Speed.append(Speed[k])
    a_MPG.append(DashMpg[k])
    a_Time.append(Time[k])
#print(data)

df = pd.DataFrame({"A": a_MPG, "B": a_Speed, "C": a_MAF})
result = sm.ols(formula="A ~ B + C", data=df).fit()

#for getting the intercepts
temp_string = ''
temp_string = temp_string + str(result.params)

print (result.summary())
#shows the coefficents
print (re.findall(r"[-+]?\d*\.\d+|[-+]?\d+", temp_string ))
list = re.findall(r"[-+]?\d*\.\d+|[-+]?\d+", temp_string )

a = float(list[0])
b = float(list[1])
c = float(list[2])

#where the data for graphing is stored
data_out = ([])

#equation for the MPG
for j in range(len(DashMpg)):
    data_out.append(a +  (float(b)*float(Speed[j]))  + (float(c)*float(MAF[j])))

#for ploting the data
plt.plot(a_Time,data_out, 'r-', a_Time, a_MPG)
plt.xlabel('Time')
plt.ylabel('MPG')
#plt.rcParams['figure.figsize'] = (20,10)

plt.show((30,20))
