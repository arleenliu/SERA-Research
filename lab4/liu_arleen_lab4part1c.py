#This program displays the DBSCAN graphs

import csv
import scipy as sp
import bokeh as bk
import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
from matplotlib import dates
import re
from sklearn.cluster import DBSCAN

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

	#fig, ax = plt.subplots()
	colors = {'conc' : 'red', 'heik' : 'blue', 'hept' : 'green'}

	fig=plt.figure(figsize = (20, 7.25))
	plt.subplots_adjust(left=0.06, bottom=0.06, right=0.95, top=0.95, wspace=0.75, hspace=1)
	
	eps1 = 0.11
	for i in range(1, 5):
		a_pred = DBSCAN(eps=eps1, min_samples = i+1).fit_predict(plot_points)
		graph=fig.add_subplot(4,4,i)
		graph.set_title('DBSCAN Graph ' + str(i))
		graph.set_xlabel('Maximum Width')
		graph.set_ylabel('Front Angle')
		graph.scatter(plot_points[:,0], plot_points[:,1], c=a_pred)

	eps2 = 0.12
	for i in range(1, 5):
		a_pred = DBSCAN(eps=eps2, min_samples = i+1).fit_predict(plot_points)
		graph=fig.add_subplot(4,4,i+4)
		graph.set_title('DBSCAN Graph ' + str(i+4))
		graph.set_xlabel('Maximum Width')
		graph.set_ylabel('Front Angle')
		graph.scatter(plot_points[:,0], plot_points[:,1], c=a_pred)

	eps3 = 0.13
	for i in range(1, 5):
		a_pred = DBSCAN(eps=eps3, min_samples = i+1).fit_predict(plot_points)
		graph=fig.add_subplot(4,4,i+8)
		graph.set_title('DBSCAN Graph ' + str(i+8))
		graph.set_xlabel('Maximum Width')
		graph.set_ylabel('Front Angle')
		graph.scatter(plot_points[:,0], plot_points[:,1], c=a_pred)

	eps4 = 0.14
	for i in range(1, 5):
		a_pred = DBSCAN(eps=eps4, min_samples = i+1).fit_predict(plot_points)
		graph=fig.add_subplot(4,4,i+12)
		graph.set_title('DBSCAN Graph ' + str(i+12))
		graph.set_xlabel('Maximum Width')
		graph.set_ylabel('Front Angle')
		graph.scatter(plot_points[:,0], plot_points[:,1], c=a_pred)

	#plt.scatter(plot_points[:,0], plot_points[:,1], color = [colors[i] for i in array1[:,0]])	
	#plt.xlabel('Maximum Width')
	#plt.ylabel('Front Angle')
	#plt.title('Flea Data')
	plt.show()

	print (array1)



