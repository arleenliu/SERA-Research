################################################################
from time import time

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import decomposition
from sklearn import manifold, datasets

# Next line to silence pyflakes. This import is needed.
Axes3D

n_points = 1000
X, color = datasets.samples_generator.make_s_curve(n_points, random_state=0)
n_neighbors = 10
n_components = 2

fig = plt.figure(figsize=(15, 8))
plt.suptitle("Manifold Learning with %i points, %i neighbors"
             % (1000, n_neighbors), fontsize=14)

ax = fig.add_subplot(111, projection='3d')
ax.scatter(X[:, 0], X[:, 1], zs=X[:, 2], c=color, cmap=plt.cm.Spectral)
ax.view_init(4, -72)
plt.show()

####TSNE####
fig = plt.figure()
t0 = time()
tsne = manifold.TSNE(n_components=2, init='pca', random_state=0)
Y = tsne.fit_transform(X)
t1 = time()
print("t-SNE: %.2g sec" % (t1 - t0))
ax = fig.add_subplot(1,2,1)
plt.scatter(Y[:, 0], Y[:, 1], c=color, cmap=plt.cm.Spectral)
plt.title("t-SNE (%.2g sec)" % (t1 - t0))

####PCA####
t0 = time()
pca = decomposition.PCA(n_components=2)
X1 = pca.fit_transform(X)
t1 = time()
ax = fig.add_subplot(1,2,2)
plt.scatter(X1[:, 0], X1[:, 1], c=color, cmap=plt.cm.spectral)
plt.title("PCA (%.2g sec)" % (t1 - t0))
plt.show()
