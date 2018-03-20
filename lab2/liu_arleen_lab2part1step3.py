import json
import requests
import re
from collections import Counter

output_file = "liu_arleen_lab2part1step3.txt"

data = requests.get("http://www.recipepuppy.com/api/?", params={'i':'onions,garlic', "q":'omelet', "p":'3'}).json()

results = []

count=0
matches=[]

for i in data['results']:

	if (count<3):
		print (i['title'])
		results.append(i['title'])		
    
	count=count+1

tracker = 0
newMatch = []

for i in data['results']:

	if (tracker<3):
		matches=re.sub(", ","\n",str(i['ingredients']))
		newMatch = newMatch + re.findall('.*\n', matches)
		#results.append(str(matches))
		#print (str(matches))

	tracker=tracker+1	

#print(str(Counter(newMatch).items()))
newMatch = Counter(newMatch).items()
newMatch = sorted(newMatch)

def getKey(item):
	return item[0]

for i in newMatch:
	print(str(i[1])+" "+str(i[0]))
	results.append(str(i[1])+" "+str(i[0]))

with open(output_file, 'w') as file:
	for i in results:
		file.write(str(i))