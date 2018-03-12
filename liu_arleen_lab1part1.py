import re
 
#pattern = r'(^([0-1]?[0-9])[/-]([0-3]?[1-9])[/-]?(\d{0}|\d{1}|\d{2}|\d{4})$)'

#pattern = r'((^([0-3]?[0-9])[\./-]([0-3]?[0-9])[\./-]?\b(\d{0}|\d{1}|\d{2}|\d{4})$)|(^(\d{2}|\d{4})[\./-]([0-1]?[0-9])[\./-]?\b([0-3]?[0-9])?$))'

#pattern = r'(^([0-3]?[0-9])[\./-]([0-3]?[0-9])[\./-]?\b(\d{0}|\d{1}|\d{2}|\d{4})$)'

pattern1 = r'((^([0-3]?[0-9])[\.\s\,/-]([0-3]?[0-9])[\.\s\,/-]*\b(\d{0}|\d{1}|\d{2}|\d{4})?$)|(^(\d{2}|\d{4})[\.\s\,/-]([0-1]?[0-9])[\.\s\,/-]?\b([0-3]?[0-9])?$))'
#pattern2 = r'(()|(\d{0}|\d{1}|\d{2}|\d{4}))'

input_file = "input1_step4.txt"
output_file = "output.txt"
 
with open(input_file, "r") as f: 
	contentList = f.readlines()
	
results = []
	
for line in contentList:

	#if(re.sub('June','06',line)!=line):
	line=re.sub('June','06',line)
	#elif(re.sub('March','03',line)!=line):
	line=re.sub('March','03',line)
	#elif(re.sub('July','07',line)!=line):
	line=re.sub('July','07',line)
	#elif(re.sub('April','04',line)!=line):
	line=re.sub('April','04',line)
	#elif(re.sub('August','08',line)!=line):
	line=re.sub('August','08',line)
	#elif(re.sub('May','05',line)!=line):
	line=re.sub('May','05',line)
	#elif(re.sub('Apr','04',line)!=line):
	line=re.sub('Apr','04',line)
	#elif(re.sub('Dec','12',line)!=line):
	line=re.sub('Dec','12',line)
	#elif(re.sub('MAY','05',line)!=line):
	line=re.sub('MAY','05',line)

	#if(re.sub('1st','01',line)!=line):
	line=re.sub('1st','01',line)
	#elif(re.sub('2nd','02',line)!=line):
	line=re.sub('2nd','02',line)
	#elif(re.sub('3rd','03',line)!=line):
	line=re.sub('3rd','03',line)
	#elif(re.sub('4th','04',line)!=line):
	line=re.sub('4th','04',line)

	matches = re.findall(pattern1, line)
	date = ""

	for i in matches:		
		i2 = ""
		i3 = ""
		i4 = ""

		#month day year
		if len(i[2]) != 0:
			if int(i[2]) <= 12:	
				i2=i[2]
				i3=i[3]
				i4=i[4]

				if len(i[4]) == 2:
					i4 = "20" + i[4]
				elif len(i[4]) == 1:
					i4 = "200" + i[4]

				if len(i[2]) < 2:    				
					i2 = "0" + i[2]

				if len(i[3]) < 2:
					i3= "0" + i[3]	

				if len(i[4]) != 0:
					date = i2+"/"+i3+"/"+i4
				else:
					date = i2+"/"+i3

			else:
			#day month year
				i2=i[3]
				i3=i[2]
				i4=i[4]

				if len(i[4]) == 2:
					i4 = "20" + i[4]

				if len(i[3]) < 2:    				
					i2 = "0" + i[3]

				if len(i[2]) < 2:
					i3= "0" + i[2]	
				    			
				if len(i[4]) == 1:
					i4 = "200" + i[4]

				if len(i[4]) > 0:
					date = i2+"/"+i3+"/"+i4
				else:
					date = i2+"/"+i3

		else:
			#year month day
			i2=i[7]
			i3=i[8]
			i4=i[6]

			if len(i[6]) == 2:
				i4 = "20" + i[6]

			if len(i[7]) < 2:    				
				i2 = "0" + i[7]

			if len(i[8]) < 2:
				i3= "0" + i[8]	
			    			
			if len(i[6]) == 1:
				i4 = "200" + i[6]

			if len(i[6]) > 0:
				if len(i[8]) > 0:
					date = i2+"/"+i3+"/"+i4
				else:
					date = i2+"/"+i4	
			else:
				date = i2+"/"+i3	
				
		print(date)

		results.append(date)
 
with open(output_file, 'w') as file:
	for i in results:

		file.write(i + '\n')