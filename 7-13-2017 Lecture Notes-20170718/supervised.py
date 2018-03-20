import numpy as np
import csv
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB

header = []
data = []
data2 = []

with open('golf.csv', 'rb') as csvfile:
    read = csv.reader(csvfile, delimiter=',')
    header = next(read)
    for row in read:
        data.append(row)

data = np.asarray(data).astype(np.float)

with open('golf2.csv', 'rb') as csvfile:
    read = csv.reader(csvfile, delimiter=',')
    header = next(read)
    for row in read:
        data2.append(row)

data2 = np.asarray(data2).astype(np.float)

gnb = GaussianNB()
gnb.fit(data[:,:4],data[:,4])
print (gnb.score(data[:,:4],data[:,4]))
print (gnb.class_prior_) #probability of each class.
print (gnb.class_count_) #number of training samples observed in each class.

gnb = GaussianNB()
gnb.fit(data2[:,:4],data2[:,4])
print (gnb.score(data2[:,:4],data2[:,4]))
print (gnb.class_prior_) #probability of each class.
print (gnb.class_count_) #number of training samples observed in each class.

clf = DecisionTreeClassifier(criterion="entropy", random_state=0)
clf.fit(data[:,:4],data[:,4])
print (clf.score(data[:,:4],data[:,4]))
print (clf.feature_importances_)

tree.export_graphviz(clf, out_file='tree1.dot')

clf = DecisionTreeClassifier(criterion="entropy", random_state=0)
clf.fit(data2[:,:4],data2[:,4])
print (clf.score(data2[:,:4],data2[:,4]))
print (clf.feature_importances_)

tree.export_graphviz(clf, out_file='tree2.dot')

#dot -Tpng tree.dot -o tree.png
