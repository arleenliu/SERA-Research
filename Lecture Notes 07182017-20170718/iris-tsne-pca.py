#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
=========================================================
PCA example with Iris Data-set
=========================================================

Principal Component Analysis applied to the Iris dataset.

See `here <https://en.wikipedia.org/wiki/Iris_flower_data_set>`_ for more
information on this dataset.

"""
print(__doc__)


# Code source: Gaël Varoquaux
# License: BSD 3 clause
# Modified by Hannah Wolfe

import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
from sklearn import decomposition
from sklearn import datasets
from sklearn import manifold
from time import time

np.random.seed(5)

centers = [[1, 1], [-1, -1], [1, -1]]
iris = datasets.load_iris()
X = iris.data
y = iris.target

####PCA####
'''
pca = decomposition.PCA(n_components=3)
pca.fit(X)
X1 = pca.transform(X)

fig = plt.figure(figsize=(15, 8))
# Reorder the labels to have colors matching the cluster results
ax = fig.add_subplot(111, projection='3d')
y = np.choose(y, [1, 2, 0]).astype(np.float)
ax.scatter(X1[:, 0], X1[:, 1], zs=X1[:,2], c=y, cmap=plt.cm.spectral)
plt.show()
'''
####PCA####

pca = decomposition.PCA(n_components=2)
pca.fit(X)
X1 = pca.transform(X)

# Reorder the labels to have colors matching the cluster results
y = np.choose(y, [1, 2, 0]).astype(np.float)
plt.scatter(X1[:, 0], X1[:, 1], c=y, cmap=plt.cm.spectral)
plt.show()

####TSNE####

tsne = manifold.TSNE(n_components=2, init='pca', random_state=0)
X2 = tsne.fit_transform(X)


plt.scatter(X2[:, 0], X2[:, 1], c=y, cmap=plt.cm.spectral)
plt.show()


