# -*- coding: utf-8 -*-
"""
Carlos Esparza
Regression Modeling
"""
import pandas as pd
import numpy as np
import sys
import os

choice = int(input('If this is a CSV file please press [1] to continue. If this is an EXCEl fie press [2]:\n'))

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
# Reading in your data file
try:   
    unRegData = pd.ExcelFile(newfilename)
    #print(unRegData)
except:
    print('Error in reading file')
    sys.exit(1)
