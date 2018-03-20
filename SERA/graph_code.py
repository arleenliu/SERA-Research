import csv
import scipy as sp
import bokeh as bk
import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import re
import pandas as pd

readCSV1 = None
readCSV2 = None

array1 = []
headers1 = []

with open('/Users/arleenliu/Downloads/SERA/vgsales.csv') as csvfile:
	df = pd.read_csv("/Users/arleenliu/Downloads/SERA/vgsales.csv", encoding = "ISO-8859-1", delimiter = "\n", header=None)
	readCSV1 = df.values
	x=False
	for row in readCSV1:
		array3 = []
		if(x==False):
			headers1.append(row)
			x=True
		else:	
			for i in row:
				array3.append(i)
			array1.append(array3)
	array1 = np.array(array1)

array2 = []
headers2 = []

with open('/Users/arleenliu/Downloads/SERA/Output.csv') as csvfile:
	df = pd.read_csv("/Users/arleenliu/Downloads/SERA/vgsales.csv", encoding = "ISO-8859-1", delimiter = "\n", header=None)
	readCSV2 = df.values
	for row in readCSV2:
		array3 = []
		for i in row:
			array3.append(i)
		array2.append(array3)
	array2 = np.array(array2)	
	
	#fig=plt.figure()
	fig=plt.figure(figsize=(20,7.25))
	plt.subplots_adjust(left=0.06, bottom=0.06, right=0.95, top=0.95, wspace=0.25, hspace=0.25)
	#plt.title("Number of Searches of Films and Novels")
	graph1=fig.add_subplot(111)
	graph1.set_title('General')
	graph1.set_ylabel('Units Sold (mill.)')
	graph1.set_xlabel('# of Searches (mill.)')
	graph1.scatter(array2[:,1], array1[:,10].astype(float))

	#fig.tight_layout()
	#plt.plot(arr1[:,4])
	#print(arr1[:,3])
	plt.savefig("results.png")
	plt.show()
