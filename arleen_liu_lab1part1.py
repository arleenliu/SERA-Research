import re
 
pattern = r'(^([0-1]?[0-9]|[1][0])[/-]([0-3]?[1-9])[/-]?(\d{0}|\d{1}|\d{2}|\d{4})$)'
input_file = "input1_step1.txt"
output_file = "output.txt"
 
with open(input_file, "r") as f: 
	contentList = f.readlines()
	
results = []
	
for line in contentList:
    matches = re.findall(pattern, line)
    for i in matches:
	    #print(i)
	    i1=i[1]
	    i2=i[2]
	    i3=i[3]

	    if len(i[1]) < 2:    				
			i1 = "0" + i[1]

    			if len(i[2]) < 2:
    				i2 = "0" + i[2]	
    			else:
    				i2=i[2]	

    			if len(i[3]) == 1:
   					i3 = "200" + i[3]

	    if len(i[3]) == 2:
    		i3 = "20" + i[3]
		else:
			i3=i[3]

    		date = i1+"/"+i2+"/"+i3
    		print(date)

	    	results.append(i)
 
with open(output_file, 'w') as file:
    for i in results:

    	i1=i[1]
    i2=i[2]
    i3=i[3]

    if len(i[1]) < 2:    				
			i1 = "0" + i[1]

    			if len(i[2]) < 2:
    				i2 = "0" + i[2]	
    			else:
    				i2=i[2]

    			if len(i[3]) == 1:
   					i3 = "200" + i[3]

	    		if len(i[3]) == 2:
    				i3 = "20" + i[3]
    			else:
    				i3=i[3]
	

    			date = i1+"/"+i2+"/"+i3

        		file.write(date + '\n')