import re
 
pattern = r'(\d+-\d+-\d+)'
input_file = "input1_step1.txt"
output_file = "output.txt"
 
with open(input_file, "r") as f: 
	contentList = f.readlines()
	
results = []
	
for line in contentList:
    matches = re.findall(pattern, line)
    for i in matches:
	    print(i)
	    results.append(i)
	    
 
with open(output_file, 'w') as file:
    for i in results:
        file.write(i + '\n')
      

