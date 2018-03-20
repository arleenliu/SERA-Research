import csv
import numpy as np
import pandas as pd
import collections
import re
data = []
headers = ['buying','maint','doors','persons','lug_boot','safety','quality']
def getFrequencyInfo(c1, c2, data):  
    #format a lookup table with each row [c1, c2, count]
    
    #################Hints for Potential Solution###################
    #create an list with only the two columns of data formatted    #
    #["c1,c2","c1,c2",...,"c1,c2"]                                 #
    #create a counter, counting the instance of each state "c1,c2" #
    #reformat counter to a list with each row = [c1, c2, count]    #
    ################################################################
    labels={'buying':0, 'maint':1, 'doors':2, 'persons':3, 'lug_boot':4, 'safety':5, 'acceptable':6}
    
    frequencyLookup = pd.crosstab(index=data[:,labels[c1]], 
                            columns=data[:,labels[c2]],
                             margins=True)   # Include row and column totals
   
    
    
    return frequencyLookup
def naiveBayes(c, x, lookup):
    #c and x are labels
    #use lookup table for the x column in relation to c
    #Naive Bayes Formula: P(c|x) = P(x|c) * P(c) / P(x)
    #use lookup table to calculate P(c|x)
    c_x=lookup.at[x, c]/lookup.at['All', c]
    
    c=lookup.at['All', c]/lookup.at['All', 'All']
    x=lookup.at[x, 'All']/lookup.at['All', 'All']
    pcx = float(c_x*c)/float(x)
    return pcx
#Import 'carCat.csv' file
with open('/Users/arleenliu/Data Analysis References/lab5/carCat.csv') as csvfile:
    readCSV = csv.reader(csvfile)
    array1 = []
    for row in readCSV:
        array1.append(row)
        
            
    data = np.array(array1)
    
#Create Lookup Tables for each columns relationship to the quality column
#test getFrequency
def testit(arr,col,c):
    
    
    highest=0
    w=''   
    for x in arr:
        buying=getFrequencyInfo(col,'acceptable', data)
        if(naiveBayes(c, x,  buying)>highest):
            highest=naiveBayes(c, x,  buying)
            w=x
    print(col+' : '+w+' '+str(highest)+'\n')
print('label that predicts the highest acceptability for each attribute')
testit(['high','med','low','vhigh'],'buying','acc')
testit(['high','med','low','vhigh'],'maint','acc')
testit(['2', '3', '4', '5more'],'doors','acc')
testit(['2','4','more'],'persons','acc')
testit(['small','med','big'],'lug_boot','acc')
testit(['high','med','low'],'safety','acc')