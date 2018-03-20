import csv
import scipy as sp
import bokeh as bk
import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
from matplotlib import dates
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
	arr4=np.transpose(arr3)

	corr = np.corrcoef(arr4)
	print(corr)

	#Book 1 Film 1
	corr1 = np.corrcoef(arr3[:,2],y=arr3[:,3])
	print (corr1)
	#Book 2 Film 1
	corr2 = np.corrcoef(arr3[:,4],y=arr3[:,5])
	print (corr2)
	#Book 3 Film 1
	corr3 = np.corrcoef(arr3[:,6],y=arr3[:,7])
	print (corr3)
	#Book 4 Film 1
	corr4 = np.corrcoef(arr3[:,8],y=arr3[:,9])
	print (corr4)
	#Book 5 Film 1
	corr5 = np.corrcoef(arr3[:,10],y=arr3[:,11])
	print (corr5)
	#Book 6 Film 1
	corr6 = np.corrcoef(arr3[:,12],y=arr3[:,13])
	print (corr6)
	#Book 7 Film 1
	corr7 = np.corrcoef(arr3[:,14],y=arr3[:,16])
	print (corr7)
	#Book 7 Film 2
	corr8 = np.corrcoef(arr3[:,15],y=arr3[:,16])
	print (corr8)
	#General
	corr9 = np.corrcoef(arr3[:,0],y=arr3[:,1])
	#plt.show()

	#fig=plt.figure()
	fig=plt.figure(figsize=(20,7.25))
	plt.subplots_adjust(left=0.06, bottom=0.06, right=0.95, top=0.95, wspace=0.25, hspace=0.25)
	#plt.title("Number of Searches of Films and Novels")
	graph1=fig.add_subplot(251)
	graph1.set_title('All')
	graph1.imshow(corr)
	plt.legend()
	graph2=fig.add_subplot(252)
	graph2.set_title('Book 1')
	graph2.imshow(corr1)
	plt.legend()
	graph3=fig.add_subplot(253)
	graph3.set_title('Book 2')
	graph3.imshow(corr2)
	plt.legend()
	graph4=fig.add_subplot(254)
	graph4.set_title('Book 3')
	graph4.imshow(corr3)
	plt.legend()
	graph5=fig.add_subplot(255)
	graph5.set_title('Book 4')
	graph5.imshow(corr4)
	plt.legend()
	graph6=fig.add_subplot(256)
	graph6.set_title('Book 5')
	graph6.imshow(corr5)
	plt.legend()
	graph7=fig.add_subplot(257)
	graph7.set_title('Book 6')
	graph7.imshow(corr6)
	plt.legend()
	graph8=fig.add_subplot(258)
	graph8.set_title('Book 7 (Film 1)')
	graph8.imshow(corr7)
	graph9=fig.add_subplot(259)
	graph9.set_title('Book 7 (Film 2)')
	graph9.imshow(corr8)
	graph9=fig.add_subplot(2,5,10)
	graph9.set_title('General')
	graph9.imshow(corr9)

	#fig.tight_layout()
	#plt.plot(arr1[:,4])
	#print(arr1[:,3])
	plt.savefig("lab3_part1_graph2.png")
	plt.show()
