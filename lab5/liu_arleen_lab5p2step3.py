import numpy as np
import csv
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
header = []
data = []
data2 = []
with open('/Users/arleenliu/liu_arleen_SERA/lab5/carVal_train.csv') as csvfile:
    readCSV = csv.reader(csvfile)
    array1 = []
    for row in readCSV:
        arr2=[]
        for i in row:
            arr2.append(float(i))
        array1.append(arr2)
        
            
    
data = np.asarray(array1).astype(np.float)
with open('/Users/arleenliu/liu_arleen_SERA/lab5/carVal_test.csv') as csvfile:
    readCSV = csv.reader(csvfile)
    array1 = []
    for row in readCSV:
        arr2=[]
        for i in row:
            arr2.append(float(i))
        array1.append(arr2)
        
data2 = np.asarray(array1).astype(np.float)
gnb = GaussianNB()
gnb.fit(data[:,:5],data[:,6])
print( gnb.score(data2[:,:5],data2[:,6]))
print (gnb.class_prior_) 
print( gnb.class_count_) 
y=[]
for i in range(9,13):
    for x in range(8,12):
        clf = DecisionTreeClassifier(criterion="entropy", max_depth=i+1, min_samples_split = x+1, random_state=0)
        clf.fit(data[:,:5],data[:,6])
        print (clf.score(data2[:,:5],data2[:,6]))
        print (clf.feature_importances_)
        y.append(clf.score(data2[:,:5],data2[:,6]))
        print('max depth: '+str(i)+', min. samples: '+str(x))
        tree.export_graphviz(clf, out_file='tree'+str(i)+str(x)+'.dot')
print(str(max(y)))