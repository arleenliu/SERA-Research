import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
import math
import csv

data=[]
with open('/Users/arleenliu/liu_arleen_SERA/lab5/carVal_train.csv') as csvfile:
    readCSV = csv.reader(csvfile)
    array1 = []
    for row in readCSV:
        array2=[]
        for i in row:
            array2.append(float(i))
        array1.append(array2)
        
            
    data = np.array(array1)

a=data[:,:5].reshape(1407,5)

ay = data[:,6]

data2=[]
with open('/Users/arleenliu/liu_arleen_SERA/lab5/carVal_test.csv') as csvfile:
    readCSV = csv.reader(csvfile)
    array1 = []
    for row in readCSV:
        array2=[]
        for i in row:
            array2.append(float(i))
        array1.append(array2)
        
            
    data2 = np.array(array1)

b=data2[:,:5].reshape(321,5)

by=data2[:,6]

model = GaussianNB()
model.fit(a, ay)
pred = model.predict(b)
pred=np.asarray(pred)
#print (pred)
#print(by)
print(str(np.sum(pred == by))+' of '+str(by.size)+' correct')
    
plt.scatter(a[:, 0], a[:, 1], c=ay, s=100)

plt.show()