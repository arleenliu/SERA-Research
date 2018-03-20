import re
 
#pattern = r'(^([0-1]?[0-9])[/-]([0-3]?[1-9])[/-]?(\d{0}|\d{1}|\d{2}|\d{4})$)'

#pattern = r'((^([0-3]?[0-9])[\./-]([0-3]?[0-9])[\./-]?\b(\d{0}|\d{1}|\d{2}|\d{4})$)|(^(\d{2}|\d{4})[\./-]([0-1]?[0-9])[\./-]?\b([0-3]?[0-9])?$))'

#pattern = r'(^([0-3]?[0-9])[\./-]([0-3]?[0-9])[\./-]?\b(\d{0}|\d{1}|\d{2}|\d{4})$)'

#pattern = r'((^([0-3]?[0-9])[\./-]([0-3]?[0-9])[\./-]?\b(\d{0}|\d{1}|\d{2}|\d{4})?$)|(^(\d{2}|\d{4})[\./-]([0-1]?[0-9])[\./-]?\b([0-3]?[0-9])?$))'

pattern = r'((^([0-3]?[0-9])[\.\s\,/-]([0-3]?[0-9])[\.\s\,/-]*\b(\d{0}|\d{1}|\d{2}|\d{4})?$)|(^(\d{2}|\d{4})[\.\s\,/-]([0-1]?[0-9])[\.\s\,/-]?\b([0-3]?[0-9])?$))'

input_file = "input1_step3.txt"
output_file = "output_part1step2.txt"
 
with open(input_file, "r") as f: 
	contentList = f.readlines()
	
results = []
	
for line in contentList:
    matches = re.findall(pattern, line)
    for i in matches:
	    #print(i)
		   	
    		print(i)

	    	results.append(i)
 
with open(output_file, 'w') as file:
    for i in results:
    	file.write(i + '\n')