import json
import requests
import re

output_file = "liu_arleen_lab2part1step1.txt"

data = requests.get("http://www.recipepuppy.com/api/?", params={'i':'onions,garlic', "q":'omelet', "p":'3'}).json()

results = []

count=0
matches=[]

for i in data['results']:

	if (count==0):
		print (i['title'])
		print("\n")
		matches=re.sub(", ","\n",str(i['ingredients']))
		print (str(matches))
		results.append(i['title'])
		results.append("\n")
		results.append(str(matches))
		
    
	count=count+1

with open(output_file, 'w') as file:
	for i in results:
		file.write(i)
