import matplotlib.pyplot as plot
# set up your lists
numlist = [8, 7, 5, 3]
namelist = ['pink', 'purple', 'red', 'orange']
colorlist = ['pink', 'purple', 'red', 'orange' ]
explodelist = [0.1, 0.1, 0.1, 0.1]
# make the pie chart
plot.pie(numlist, labels=namelist, autopct='%.3f%%', colors=colorlist,
    	explode = explodelist, startangle = 180)
plot.axis('equal')
plot.savefig('piechart.png')
