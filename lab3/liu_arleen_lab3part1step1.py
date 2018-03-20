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

	#fig=plt.figure()
	fig=plt.figure(figsize=(20,7.25))
	plt.subplots_adjust(left=0.06, bottom=0.06, right=0.95, top=0.95, wspace=0.25, hspace=0.25)
	#plt.title("Number of Searches of Films and Novels")
	graph1=fig.add_subplot(241)
	graph1.set_title('General')
	graph1.set_xlabel('Dates')
	graph1.set_ylabel('# of Searches (mill.)')
	graph1.plot(labels[:], arr1[:,1], label='Film')
	graph1.plot(labels[:], arr1[:,2], label='Novel')
	plt.legend()
	graph2=fig.add_subplot(242)
	graph2.set_title('Book 1')
	graph2.set_xlabel('Dates')
	graph2.set_ylabel('# of Searches (mill.)')
	graph2.plot(labels[:], arr1[:,3], label='Film')
	graph2.plot(labels[:], arr1[:,4], label='Novel')
	plt.legend()
	graph3=fig.add_subplot(243)
	graph3.set_title('Book 2')
	graph3.set_xlabel('Dates')
	graph3.set_ylabel('# of Searches (mill.)')
	graph3.plot(labels[:], arr1[:,5], label='Film')
	graph3.plot(labels[:], arr1[:,6], label='Novel')
	plt.legend()
	graph4=fig.add_subplot(244)
	graph4.set_title('Book 3')
	graph4.set_xlabel('Dates')
	graph4.set_ylabel('# of Searches (mill.)')
	graph4.plot(labels[:], arr1[:,7], label='Film')
	graph4.plot(labels[:], arr1[:,8], label='Novel')
	plt.legend()
	graph5=fig.add_subplot(245)
	graph5.set_title('Book 4')
	graph5.set_xlabel('Dates')
	graph5.set_ylabel('# of Searches (mill.)')
	graph5.plot(labels[:], arr1[:,9], label='Film')
	graph5.plot(labels[:], arr1[:,10], label='Novel')
	plt.legend()
	graph6=fig.add_subplot(246)
	graph6.set_title('Book 5')
	graph6.set_xlabel('Dates')
	graph6.set_ylabel('# of Searches (mill.)')
	graph6.plot(labels[:], arr1[:,11], label='Film')
	graph6.plot(labels[:], arr1[:,12], label='Novel')
	plt.legend()
	graph7=fig.add_subplot(247)
	graph7.set_title('Book 6')
	graph7.set_xlabel('Dates')
	graph7.set_ylabel('# of Searches (mill.)')
	graph7.plot(labels[:], arr1[:,13], label='Film')
	graph7.plot(labels[:], arr1[:,14], label='Novel')
	plt.legend()
	graph8=fig.add_subplot(248)
	graph8.set_title('Book 7')
	graph8.set_xlabel('Dates')
	graph8.set_ylabel('# of Searches (mill.)')
	graph8.plot(labels[:], arr1[:,15], label='Film 1')
	graph8.plot(labels[:], arr1[:,16], label='Film 2')
	graph8.plot(labels[:], arr1[:,17], label='Novel')
	plt.legend()

	#fig.tight_layout()
	#plt.plot(arr1[:,4])
	#print(arr1[:,3])
	plt.savefig("lab3_part1_graph1.png")
	plt.show()
