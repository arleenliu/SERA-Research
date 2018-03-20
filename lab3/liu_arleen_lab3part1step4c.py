import csv
import scipy as sp
import bokeh as bk
import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
from matplotlib import dates
from scipy import stats
import re


with open('/Users/arleenliu/Downloads/lab3/harryPotter-film-novel.csv') as csvfile:
	readCSV = csv.reader(csvfile)
	array1 = []
	headers = []
	x=False
	for row in readCSV:
		array2 = []
		if(x==False):
			headers.append(row)
			x=True
		else:	
			for i in row:
				array2.append(i)
			array1.append(array2)
	arr1 = np.array(array1)
	heads = np.array(headers)
	#print(arr1[:,0])
	arr2 = []
	innerArr = []
	for i in arr1:
		count = 0
		for a in i:
			if(count==0):
				innerArr.append(a)
			count=count+1
		arr2.append(innerArr)

	arr2=np.array(arr2)
	print(arr2[:,0])

	labels=[]
	counter=0
	for i in innerArr:
		labels.append(dt.datetime.strptime(i, "%Y-%m-%d"))

	labels = np.array(labels)

	arr3=[]
	for i in arr1:
		count = 0
		innerArr2=[]
		for a in i:
			if(count>0):
				a=float(a)
				innerArr2.append(a)	
			count=count+1
		arr3.append(innerArr2)

	arr3 = np.array(arr3)

	arr1_max1=float(max(arr1[:,1]))
	arr1_norm1=[]
	for i in arr1[:,1]:
	    arr1_norm1.append(float(i)/arr1_max1)
	    
	arr1_max2=float(max(arr1[:,2]))
	arr1_norm2=[]
	for i in arr1[:,2]:
	    arr1_norm2.append(float(i)/arr1_max2)	

	corr = np.corrcoef(np.transpose(arr1_norm1),y=np.transpose(arr1_norm2))
	print (corr)

	#fig=plt.figure()
	plt.title("Number of General Searches of Films and Novels")
	plt.plot(labels[:], arr1_norm1, label='Film')
	plt.plot(labels[:], arr1_norm2, label='Novel')
	plt.legend()

	results = []

	results=sp.stats.pearsonr(arr3[:,0],y=arr3[:,1])
	print("Correlation coefficient is: "+str(results[0]))
	print("P-value is: "+str(results[1]))

	#fig.tight_layout()
	#plt.plot(arr1[:,4])
	#print(arr1[:,3])
	plt.savefig("lab3_part1_graph4.png")
	plt.show()
