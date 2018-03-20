#This program displays the Gaussian mixture model

import csv
import scipy as sp
import bokeh as bk
import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
from matplotlib import dates
import re
from sklearn import mixture
import itertools
from scipy import linalg

from bokeh.plotting import *
from bokeh.models import Range1d, OpenURL, TapTool, HoverTool, ColumnDataSource, DatetimeTickFormatter

with open('/Users/arleenliu/liu_arleen_SERA/lab4/flea.csv') as csvfile:
	random_state = 170

	readCSV = csv.reader(csvfile)
	array1 = []
	headers = []
	x=False
	for row in readCSV:
		array2 = []
		if(x==False):
			for i in row:
				i = i.split(' ')
				headers.append(i)	
			x=True
		else:	
			for i in row:
				i = i.split(' ')
				array1.append(i)

	intArray = []
	plot_points = []

	for row in array1:
		new_row = []
		new_row.append(int(row[1]))
		new_row.append(int(row[2]))
		new_row = np.array(new_row)
		intArray.append(new_row)

	intArray = np.array(intArray)
	max1 = max(intArray[:,0])
	max2 = max(intArray[:,1])
	min1 = min(intArray[:,0])
	min2 = min(intArray[:,1])

	for row in intArray:
		new_row = []
		new_row.append(float(row[0]-min1)/float(max1-min1))
		new_row.append(float(row[1]-min2)/float(max2-min2))
		plot_points.append(new_row)

	plot_points = np.array(plot_points)	

	array1 = np.array(array1)
	headers = np.array(headers)

	color_iter = itertools.cycle(['navy', 'c', 'cornflowerblue', 'gold', 'darkorange'])

	def plot_results(X, Y_, means, covariances, index, title): 
		splot = plt.subplot(1, 1, 1 + index)
		for i, (mean, covar, color) in enumerate(zip(
				means, covariances, color_iter)):
			v, w = linalg.eigh(covar)
			v = 2. * np.sqrt(2.) * np.sqrt(v)
			u = w[0] / linalg.norm(w[0])
			# as the DP will not use every component it has access to # unless it needs it, we shouldn't plot the redundant
			# components.
			if not np.any(Y_ == i):
				continue
			plt.scatter(X[Y_ == i, 0], X[Y_ == i, 1], 1, color=color)
			# Plot an ellipse to show the Gaussian component
			angle = np.arctan(u[1] / u[0])
			angle = 180. * angle / np.pi  # convert to degrees
			ell = mpl.patches.Ellipse(mean, v[0], v[1], 180. + angle, color=color)
			ell.set_clip_box(splot.bbox)
			ell.set_alpha(0.5)
			splot.add_artist(ell)
		plt.xticks(())
		plt.yticks(())
		plt.title(title)


	a_pred = mixture.GaussianMixture(n_components=3).fit(plot_points)
	plot_results(plot_points, a_pred.predict(plot_points), a_pred.means_, a_pred.covariances_, 0, "Gaussian Model")

	#fig, ax = plt.subplots()
	colors = {'conc' : 'red', 'heik' : 'blue', 'hept' : 'green'}

	#fig=plt.figure()
	#plt.subplots_adjust(left=0.06, bottom=0.06, right=0.95, top=0.95, wspace=0.25, hspace=0.5)
	#plt.title('KMeans Clustering')
	plt.xlabel('Maximum Width')
	plt.ylabel('Front Angle')
	#plt.scatter(plot_points[:,0], plot_points[:,1], c=a_pred)

	#graph2=fig.add_subplot(212)
	#graph2.set_title('Agglomerative Clustering')
	#graph2.set_xlabel('Maximum Width')
	#graph2.set_ylabel('Front Angle')
	#graph2.scatter(plot_points[:,0], plot_points[:,1], c=a2_pred)

	#plt.scatter(plot_points[:,0], plot_points[:,1], color = [colors[i] for i in array1[:,0]])	
	#plt.xlabel('Maximum Width')
	#plt.ylabel('Front Angle')
	#plt.title('Flea Data')
	plt.show()

	print (array1)



