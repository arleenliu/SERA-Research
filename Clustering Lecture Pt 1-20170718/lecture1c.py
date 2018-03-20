import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import make_blobs
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import KMeans

plt.figure(figsize=(12, 12))

n_samples = 1500
random_state = 170
X, y = make_blobs(n_samples=n_samples, random_state=random_state)

# Incorrect number of clusters
ya_pred = AgglomerativeClustering(n_clusters=2).fit_predict(X)
yk_pred = KMeans(n_clusters=2, random_state=random_state).fit_predict(X)

fig = plt.figure()
ax1 = fig.add_subplot(212)
ax1.scatter(X[:, 0], X[:, 1], c=ya_pred)
ax2 = fig.add_subplot(211)
ax2.scatter(X[:, 0], X[:, 1], c=yk_pred)
plt.title("Incorrect Number of Blobs")
plt.show()

# Anisotropicly distributed data
transformation = [[ 0.60834549, -0.63667341], [-0.40887718, 0.85253229]]
X_aniso = np.dot(X, transformation)
ya_pred = AgglomerativeClustering(n_clusters=3).fit_predict(X_aniso)
yk_pred = KMeans(n_clusters=3, random_state=random_state).fit_predict(X_aniso)

fig = plt.figure()
ax1 = fig.add_subplot(212)
ax1.scatter(X_aniso[:, 0], X_aniso[:, 1], c=ya_pred)
ax2 = fig.add_subplot(211)
ax2.scatter(X_aniso[:, 0], X_aniso[:, 1], c=yk_pred)
plt.title("Anisotropicly Distributed Blobs")
plt.show()


# Different variance
X_varied, y_varied = make_blobs(n_samples=n_samples,
                                cluster_std=[1.0, 2.5, 0.5],
                                random_state=random_state)
ya_pred = AgglomerativeClustering(n_clusters=3).fit_predict(X_varied)
yk_pred = KMeans(n_clusters=3, random_state=random_state).fit_predict(X_varied)

fig = plt.figure()
ax1 = fig.add_subplot(212)
ax1.scatter(X_varied[:, 0], X_varied[:, 1], c=ya_pred)
ax2 = fig.add_subplot(211)
ax2.scatter(X_varied[:, 0], X_varied[:, 1], c=yk_pred)
plt.title("Unequal Variance")
plt.show()

# Unevenly sized blobs
X_filtered = np.vstack((X[y == 0][:500], X[y == 1][:100], X[y == 2][:10]))
ya_pred = AgglomerativeClustering(n_clusters=3).fit_predict(X_filtered)
yk_pred = KMeans(n_clusters=3, random_state=random_state).fit_predict(X_filtered)

fig = plt.figure()
ax1 = fig.add_subplot(212)
ax1.scatter(X_filtered[:, 0], X_filtered[:, 1], c=ya_pred)
ax2 = fig.add_subplot(211)
ax2.scatter(X_filtered[:, 0], X_filtered[:, 1], c=yk_pred)
plt.title("Unevenly Sized Blobs")
plt.show()
