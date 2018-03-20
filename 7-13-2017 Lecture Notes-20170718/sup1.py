import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d
from sklearn.naive_bayes import GaussianNB
import math

a = np.asarray([[1,2],[1,4],[2,3],[2,7],[3,3],[3,5],[3,6],[4,2],[4,4],[4,12],[4,15],[5,3],[5,11],[5,13],[6,12],[6,13],[6,14],[7,14],[8,12],[9,7],[10,6],[10,8],[10,9],[10,10],[11,8],[11,9],[11,11],[12,10]])

ay = ([1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0])

c = np.asarray([[1,2],[1,4],[1,11],[2,3],[2,7],[3,3],[3,5],[4,15],[4,12],[5,11],[5,13],[6,12],[6,13],[6,14],[7,9],[7,14],[8,2],[8,12],[9,7],[10,6],[10,8],[10,9],[10,10],[11,3],[11,8],[11,9],[11,11],[12,10],[13,3],[13,5],[14,4],[14,13],[14,14],[15,13]])

#######naive bayes

model = GaussianNB()
model.fit(a, ay)
predicted= model.predict([[1,2],[14,6],[7,8]])
print (predicted)
plt.scatter(a[:, 0], a[:, 1], c=ay, s=100)
plt.show()

#######k-nearest neighbor

vor = Voronoi(a)
voronoi_plot_2d(vor)
plt.show()

vor = Voronoi(c)
voronoi_plot_2d(vor)
plt.show()

######logistic regression

def sigmoid(x):
    a = []
    for item in x:
        a.append(1/(1+math.exp(-item)))
    return a

Xaxis = np.arange(-10., 10., 0.2)
#Xaxis is an one-dimensional array with 100 elements
#begin from -10.0 to 10.0, with interval of 0.2 for each two elements
sig = sigmoid(Xaxis)

plt.plot(Xaxis, sig, color="blue")
plt.show()


