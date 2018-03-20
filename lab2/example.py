#from mpltoolkits_basemap import Basemap

import matplotlib.pyplot as plt
import numpy as np

# Numpy array is a gift to Data scientists and statisticians
# If you already have the data in hand and it is small, you can directly create a numpy array
# If it is obtained dynamically, the efficient way is to create a list first and then create a numpy array

xlist=[2000,2001,2002,2003,2004,2005,2006,2007,2008,2009]
ylist=[5,-2,8,2,1,2,-3,-1,1,3]
x=np.array(xlist)
y=np.array(ylist)
plt.plot(x, y)

#totalist=[[2000,5],[2001,-2],[2002,8],[2003,2],[2004,1],[2005,2],[2006,-3],[2007,-1],[2008,1],[2009,3]]
#totalnp=np.array(totalist)
#print(totalnp.shape)
#plt.plot(totalnp[:,0],totalnp[:,1])


plt.xlabel('Year')
plt.ylabel('Percent rise or fall')
plt.title('Stock trend over a few years of company X')
plt.grid(True)
plt.savefig("test.png")
plt.show()

# Get more results and statistics out of your data using stats of scipy