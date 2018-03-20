import numpy as np
import matplotlib.pyplot as plt
import csv

from mpl_toolkits.mplot3d import Axes3D
from sklearn import decomposition
from sklearn import datasets
from sklearn import manifold
from sklearn.neighbors import KNeighborsClassifier as KNN
from sklearn import metrics as m
from sklearn.svm import LinearSVC as LSVC
from time import time

np.random.seed(5)

centers = [[1, 1], [-1, -1], [1, -1]]

with open('breast-cancer-wisconsin.csv') as csvfile:
	readCSV = csv.reader(csvfile)
	array1 = []
	x=False
	for row in readCSV:
		array1.append(row)
	array1 = np.array(array1)	
	print (array1)	

	####PCA####

	fig = plt.figure(figsize=(15, 8))
	# Reorder the labels to have colors matching the cluster results
	#ax = fig.add_subplot(131, projection='3d')
	ax1 = fig.add_subplot(221)
	#y = np.choose(y, [1, 2, 0]).astype(np.float)

	####PCA####

	time1_start = time()
	pca1 = decomposition.PCA(n_components=2)
	A1 = pca1.fit_transform(array1[:,1:9])
	time1_end = time()

	knn1 = KNN()
	B1 = knn1.fit(A1,array1[:,10])
	knn1.kneighbors_graph(A1, n_neighbors = 10, mode = 'connectivity')
	b_pred = knn1.predict(A1)
	acc1 = m.accuracy_score(array1[:,10], b_pred)
	print ('K-NN and PCA accuracy score is: ' + str(acc1))

	ax1.scatter(A1[:, 0], A1[:, 1], c = b_pred, cmap=plt.cm.spectral)
	ax1.set_title("K-NN and PCA (%.2g)" % (time1_end - time1_start))

	# Reorder the labels to have colors matching the cluster results
	#y = np.choose(y, [1, 2, 0]).astype(np.float)
	#plt.scatter(X1[:, 0], X1[:, 1], c=y, cmap=plt.cm.spectral)
	#plt.show()

	####TSNE####

	time2_start = time()
	tsne = manifold.TSNE(n_components=2, init='pca', random_state=0)
	A2 = tsne.fit_transform(array1[:,1:9])
	time2_end = time()

	knn2 = KNN()
	B2 = knn2.fit(A2,array1[:,10])
	knn2.kneighbors_graph(A2, n_neighbors = 10, mode = 'connectivity')
	b2_pred = knn2.predict(A2)
	acc2 = m.accuracy_score(array1[:,10], b2_pred)
	print ('K-NN and T-SNE accuracy score is: ' + str(acc2))

	ax2 = fig.add_subplot(222)
	ax2.scatter(A2[:, 0], A2[:, 1], c=b2_pred, cmap=plt.cm.spectral)
	ax2.set_title("K-NN and T-SNE (%.2g)" % (time2_end - time2_start))

	lsvc1 = LSVC(random_state = 0)
	L1 = lsvc1.fit(A1,array1[:,10])
	l_pred = lsvc1.predict(A1)
	acc3 = m.accuracy_score(array1[:,10], l_pred)
	print ('SVM and PCA accuracy score is: ' + str(acc3))

	ax3 = fig.add_subplot(223)
	ax3.scatter(A1[:, 0], A1[:, 1], c = l_pred, cmap=plt.cm.spectral)
	ax3.set_title("SVM and PCA (%.2g)" % (time1_end - time1_start))

	lsvc2 = LSVC(random_state = 0)
	L2 = lsvc2.fit(A2,array1[:,10])
	l2_pred = lsvc2.predict(A2)
	acc4 = m.accuracy_score(array1[:,10], l2_pred)
	print ('SVM and T-SNE accuracy score is: ' + str(acc4))

	ax4 = fig.add_subplot(224)
	ax4.scatter(A2[:, 0], A2[:, 1], c=l2_pred, cmap=plt.cm.spectral)
	ax4.set_title("SVM and T-SNE (%.2g)" % (time2_end - time2_start))

	plt.show()