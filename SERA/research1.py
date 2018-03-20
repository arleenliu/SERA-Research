import requests
from bs4 import BeautifulSoup
import urllib.request
import time
import random
import csv
import pandas as pd
import numpy as np

output_file = "/Users/arleenliu/Downloads/SERA/SearchResults.csv"

with open('/Users/arleenliu/Downloads/SERA/vgsales.csv') as csvfile:
	df = pd.read_csv("/Users/arleenliu/Downloads/SERA/vgsales.csv", encoding = "ISO-8859-1", delimiter = "\n", header=None)
	readCSV = df.values
	array1 = []
	headers = []

	x=False
	count = 0
	for row in readCSV:
		row_array = row[0].split(',')
		row_array = np.array(row_array)
		array2 = []
		if(x==False):
			headers = row_array
			x=True
		else:	
			if (count < 100):
				array1.append(row_array)
			count = count + 1	

	headers = np.array(headers)
	array1 = np.array(array1)

	print (array1)			
	#https://stackoverflow.com/questions/33523549/return-the-number-of-results-for-google-search
	
	results = []
	counter = 0

	for i in array1:
		row = []
		search = i[1]

		r = requests.get("https://www.google.com/search", params={'q':search})

		soup = BeautifulSoup(r.text, "lxml")
		res = soup.find("div", {"id": "resultStats"})

		GoogleResults=float(res.text.replace(",", "").split()[1])
		#print('Google Results:',GoogleResults)
		#GoogleResults = "test"

		row.append(search)
		row.append(GoogleResults)
		row = np.array(row)

		results.append(row)

		counter = counter + 1
		time.sleep(random.randint(10,21) * 0.0001)
		#print (row)

	results = np.array(results)

	#np.savetxt(output_file, results, delimiter=",", fmt='%.18e')

	df = pd.DataFrame(results)
	df.to_csv("/Users/arleenliu/Downloads/SERA/Output.csv")


