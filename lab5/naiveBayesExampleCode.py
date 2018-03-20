import csv

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
    
    frequencyLookup = []
    return frequencyLookup

def naiveBayes(c, x, lookup, total):
    #c and x are labels
    #use lookup table for the x column in relation to c
    #Naive Bayes Formula: P(c|x) = P(x|c) * P(c) / P(x)
    #use lookup table to calculate P(c|x)
    pcx = 0
    return pcx

#Import 'carCat.csv' file



#Create Lookup Tables for each columns relationship to the quality column

#Calculate probabilities of the examples


