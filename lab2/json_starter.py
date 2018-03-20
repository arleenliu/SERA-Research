import json
import requests

output_file = "output.txt"

data = requests.get("http://www.recipepuppy.com/api/?", params={'i':'onions,garlic', "q":'omelet', "p":'3'}).json()

results = []

for i in data['results']:
    print (i)
    results.append(str(i))
    
with open(output_file, 'w') as file:
    for i in results:
        file.write(i)
