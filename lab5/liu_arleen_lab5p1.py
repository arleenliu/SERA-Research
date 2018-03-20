import csv
import numpy as np
import pandas as pd

array = []
headers = ['buying','maint','doors','persons','lug_boot','safety','quality']

def getFrequencyInfo(c1, c2, data):  
    #format a lookup table with each row [c1, c2, count]

    labels={'buying':0, 'maint':1, 'doors':2, 'persons':3, 'lug_boot':4, 'safety':5, 'quality':6}
    #print (counters)
    #for row in data:
        #if 'unacc' in row:
            #for x in range(0, len(states)):
                #if states[x] in row:
                    #counters[x] = counters[x] + 1
                    #print (counters[x])
        #else:
            #for x in range(len(states) - 1, 2 * len(states)):
                #if states[x - len(states)] in row:
                    #counters[x] = counters[x] + 1

        #for i in range(0, len(counters)):
        #    table.append(counters(i))

    
    #################Hints for Potential Solution###################
    #create an list with only the two columns of data formatted    #
    #["c1,c2","c1,c2",...,"c1,c2"]                                 #
    #create a counter, counting the instance of each state "c1,c2" #
    #reformat counter to a list with each row = [c1, c2, count]    #
    ################################################################
    
    frequencyLookup = pd.crosstab(index=data[:,labels[c1]], 
                            columns=data[:,labels[c2]],
                             margins=True)
    
    return frequencyLookup

def test(arr,col,c):
    
    highest=0
    w=''   
    for x in arr:
        buying=getFrequencyInfo(col,'quality', array)
        if(naiveBayes(c, x,  buying)>highest):
            highest=naiveBayes(c, x,  buying)
            w=x
    print(col+' : '+w+' '+str(highest)+'\n')

def naiveBayes(c, x, lookup):
    #c and x are labels
    #use lookup table for the x column in relation to c
    #Naive Bayes Formula: P(c|x) = P(x|c) * P(c) / P(x)
    #use lookup table to calculate P(c|x)
    cx_prob=lookup.at[x, c]/lookup.at['All', c]
    
    c_prob=lookup.at['All', c]/lookup.at['All', 'All']
    x_prob=lookup.at[x, 'All']/lookup.at['All', 'All']
    pcx = float(cx_prob*c_prob)/float(x_prob)
    return pcx

def multNaiveBayes(index, c, x, y, z):

    lookup2 = getFrequencyInfo(x[0], 'quality', array)
    lookup3 = getFrequencyInfo(y[0], 'quality', array)
    lookup4 = getFrequencyInfo(z[0], 'quality', array)

    #print (getFrequencyInfo('quality', x[0], array))

    ba = naiveBayes(c, x[1], lookup2)
    ca = naiveBayes(c, y[1], lookup3)
    da = naiveBayes(c, z[1], lookup4)

    a = float(lookup2.at['All', c])/float(lookup2.at['All', 'All'])
    x1 = float(lookup2.at[x[1], 'All'])/float(lookup2.at['All', 'All'])
    y1 = float(lookup3.at[y[1], 'All'])/float(lookup3.at['All', 'All'])
    z1 = float(lookup4.at[z[1], 'All'])/float(lookup4.at['All', 'All'])

    prob = (da*ca*ba*a)/(x1*y1*z1)

    print ('Test value ' + str(index) + ': ' + str(prob))


array1 = []
#Import 'carCat.csv' file
with open('/Users/arleenliu/liu_arleen_SERA/lab5/carCat.csv') as csvfile:
    readCSV = csv.reader(csvfile)
    array1 = []
    for row in readCSV:
        array1.append(row)
            
    array = np.array(array1)
    print (array)
    #print(getFrequencyInfo('quality', 'buying', array1))

    test(['high','med','low','vhigh'],'buying','acc')
    test(['high','med','low','vhigh'],'maint','acc')
    test(['2', '3', '4', '5more'],'doors','acc')
    test(['2','4','more'],'persons','acc')
    test(['small','med','big'],'lug_boot','acc')
    test(['high','med','low'],'safety','acc')

    print ('Part 1 Analysis Part b')
    multNaiveBayes(1, 'acc', ['buying', 'high'], ['maint', 'vhigh'], ['doors', '4'])
    multNaiveBayes(2, 'acc', ['buying', 'low'], ['maint', 'med'], ['safety', 'med'])
    multNaiveBayes(3, 'acc', ['buying', 'high'], ['maint', 'vhigh'], ['safety', 'low'])
    multNaiveBayes(4, 'acc', ['doors', '5more'], ['persons', 'more'], ['lug_boot', 'big'])
    multNaiveBayes(5, 'acc', ['doors', '2'], ['persons', '2'], ['lug_boot', 'small'])

#Create Lookup Tables for each columns relationship to the quality column

#Calculate probabilities of the examples


