import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

random_state = 170

#https://miguelmota.com/blog/k-means-clustering-in-javascript/demo/
#https://www.naftaliharris.com/blog/visualizing-k-means-clustering/

a = np.asarray([[1,2],[1,4],[2,3],[2,7],[3,3],[3,5],[3,6],[4,2],[4,4],[4,12],[4,15],[5,3],[5,11],[5,13],[6,12],[6,13],[6,14],[7,14],[8,12],[9,7],[10,6],[10,8],[10,9],[10,10],[11,8],[11,9],[11,11],[12,10]])

b = np.asarray([[1,2],[1,4],[2,3],[2,7],[3,3],[3,5],[3,6],[4,4],[4,12],[5,11],[5,13],[6,12],[6,13],[6,14],[7,14],[8,12],[9,5],[9,7],[10,6],[10,8],[10,9],[10,10],[11,8],[11,9],[11,11]])

c = np.asarray([[1,2],[1,4],[1,11],[2,3],[2,7],[3,3],[3,5],[4,15],[4,12],[5,11],[5,13],[6,12],[6,13],[6,14],[7,9],[7,14],[8,2],[8,12],[9,7],[10,6],[10,8],[10,9],[10,10],[11,3],[11,8],[11,9],[11,11],[12,10],[13,3],[13,5],[14,4],[14,13],[14,14],[15,13]])

a_pred = KMeans(n_clusters=2, random_state=random_state).fit_predict(a)

plt.scatter(a[:, 0], a[:, 1], c=a_pred)
plt.title("Scatter plot A, 2 clusters")
plt.show()

a2_pred = KMeans(n_clusters=3, random_state=random_state).fit_predict(a)

fig = plt.figure()
ax1 = fig.add_subplot(211)
ax1.scatter(a[:, 0], a[:, 1], c=a_pred)
ax2 = fig.add_subplot(212)
ax2.scatter(a[:, 0], a[:, 1], c=a2_pred)
plt.show()

b_pred = KMeans(n_clusters=2, random_state=random_state).fit_predict(b)

plt.scatter(b[:, 0], b[:, 1], c=b_pred)
plt.title("Scatter plot B, 2 clusters")
plt.show()

b2_pred = KMeans(n_clusters=3, random_state=random_state).fit_predict(b)

fig = plt.figure()
ax1 = fig.add_subplot(211)
ax1.scatter(b[:, 0], b[:, 1], c=b_pred)
ax2 = fig.add_subplot(212)
ax2.scatter(b[:, 0], b[:, 1], c=b2_pred)
plt.show()

c1_pred = KMeans(n_clusters=2, random_state=random_state).fit_predict(c)
c2_pred = KMeans(n_clusters=3, random_state=random_state).fit_predict(c)
c3_pred = KMeans(n_clusters=4, random_state=random_state).fit_predict(c)
c4_pred = KMeans(n_clusters=5, random_state=random_state).fit_predict(c)

fig = plt.figure()
ax1 = fig.add_subplot(221)
ax1.scatter(c[:, 0], c[:, 1], c=c1_pred)
ax2 = fig.add_subplot(222)
ax2.scatter(c[:, 0], c[:, 1], c=c2_pred)
ax3 = fig.add_subplot(223)
ax3.scatter(c[:, 0], c[:, 1], c=c3_pred)
ax4 = fig.add_subplot(224)
ax4.scatter(c[:, 0], c[:, 1], c=c4_pred)
plt.show()
