#This program displays KMeans and Agglomerative Clustering

import csv
import scipy as sp
import bokeh as bk
import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
from matplotlib import dates
import re
from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering

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

	a_pred = KMeans(n_clusters=3, random_state = random_state).fit_predict(plot_points)
	a2_pred = AgglomerativeClustering(n_clusters=3).fit_predict(plot_points)

	#fig, ax = plt.subplots()
	colors = {'conc' : 'red', 'heik' : 'blue', 'hept' : 'green'}

	fig=plt.figure()
	plt.subplots_adjust(left=0.06, bottom=0.06, right=0.95, top=0.95, wspace=0.25, hspace=0.5)
	graph1=fig.add_subplot(211)
	graph1.set_title('KMeans Clustering')
	graph1.set_xlabel('Maximum Width')
	graph1.set_ylabel('Front Angle')
	graph1.scatter(plot_points[:,0], plot_points[:,1], c=a_pred)

	graph2=fig.add_subplot(212)
	graph2.set_title('Agglomerative Clustering')
	graph2.set_xlabel('Maximum Width')
	graph2.set_ylabel('Front Angle')
	graph2.scatter(plot_points[:,0], plot_points[:,1], c=a2_pred)

	#plt.scatter(plot_points[:,0], plot_points[:,1], color = [colors[i] for i in array1[:,0]])	
	#plt.xlabel('Maximum Width')
	#plt.ylabel('Front Angle')
	#plt.title('Flea Data')
	plt.show()

	print (array1)



