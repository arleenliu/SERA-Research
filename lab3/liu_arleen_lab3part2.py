import csv
import scipy as sp
import bokeh as bk
import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
from matplotlib import dates
import re

from bokeh.plotting import *
from bokeh.models import Range1d, OpenURL, TapTool, HoverTool, ColumnDataSource, DatetimeTickFormatter

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
	
	labels=[]
	
	counter=0
	for i in innerArr:
		labels.append(dt.datetime.strptime(i, "%Y-%m-%d"))

	print(labels)
	
	data = {'1': arr1[:,4],
'2': arr1[:,6],
'3': arr1[:,8],
'4': arr1[:,10],
'5': arr1[:,12],
'6': arr1[:,14],
'7': arr1[:,17],
'date': labels,
'dateStr':innerArr
}
	source = ColumnDataSource(data=data)
	TOOLS = ['hover', 'pan', 'tap']
	
	fig, ax = plt.subplots()
	ax.set_title('Number of Searches for Novels')
	#hover2 = HoverTool(names=["test1", "test2"])
	plt= figure(title='Number of Searches for Novels',x_axis_type='datetime',tools=TOOLS)
	#plt= figure(title='Number of Searches for Novels',x_axis_type='datetime',tools=[hover2,])
	#plt.title('Number of Searches')
	
	
	
	#plt.xlabel('Dates')
	#plt.ylabel('Number of Searches (millions)')
	#plt.plot(labels[:], arr1[:,1], label='Film (all)')
	#plt.plot(labels[:], arr1[:,2], label='Novel (all)')

	#line1 = ax.plot('date', '1', lw = 2, color='red', label='Novel 1',source=source)
	#line2 = ax.plot('date', '2', lw = 2, color='turquoise', label='Novel 2',source=source)
	#line3 = ax.plot('date', '3', lw = 2, color='orange', label='Novel 3',source=source)
	#line4 = ax.plot('date', '4', lw = 2, color='green', label='Novel 4',source=source)
	#line5 = ax.plot('date', '5', lw = 2, color='blue', label='Novel 5',source=source)
	#line6 = ax.plot('date', '6', lw = 2, color='purple', label='Novel 6',source=source)
	#line7 = ax.plot('date', '7', lw = 2, color='indigo', label='Novel 7',source=source)

	plt.line('date', '1', color='red', legend='Novel 1',source=source)
	plt.line('date', '2', color='turquoise', legend='Novel 2',source=source)
	plt.line('date', '3', color='orange', legend='Novel 3',source=source)
	plt.line('date', '4', color='green', legend='Novel 4',source=source)
	plt.line('date', '5', color='blue', legend='Novel 5',source=source)
	plt.line('date', '6', color='purple', legend='Novel 6',source=source)
	plt.line('date', '7', color='indigo', legend='Novel 7',source=source)
	#legend(plt)
	#leg = ax.legend(loc='upper left', fancybox = True, shadow = True)
	#leg.get_frame().set_alpha(0.4)

	#lines = [line1, line2, line3, line4, line5, line6, line7]
	#lines = dict()
	#for legline, origline in zip(leg.get_lines(), lines):
		#legline.set_picker(5)  # 5 pts tolerance
		#lined[legline] = origline

	def onpick(event):
		legline = event.artist
		origline = lined[legline]
		vis = not origline.get_visible()
		origline.set_visible(vis)

		if vis:
			legline.set_alpha(1.0)
		else:
			legline.set_alpha(0.2)
			fig.canvas.draw()

	fig.canvas.mpl_connect('pick_event', onpick)

	#plt.plot(arr1[:,4])
	#print(arr1[:,3])

hover = plt.select(type=HoverTool)
hover.tooltips = [
("date", "@dateStr"),
("Num Searches", "$y")
]
url = 'url/@dateStr/'
taptool = plt.select(type=TapTool)
taptool.callback = OpenURL(url=url)



	#plt.grid(True)
	#plt.savefig("lab3_part1_graph1.png")
show(plt)

