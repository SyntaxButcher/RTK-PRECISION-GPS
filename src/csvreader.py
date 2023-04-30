import csv
import matplotlib.pyplot as plot
import numpy as np

file = open('/home/shak/catkin_ws/src/lab2/rosbag/open_stat.csv') #for still data in open area
#file = open('/home/shak/catkin_ws/src/lab2/rosbag/open_walk.csv') #for walking data in open area
#file = open('/home/shak/catkin_ws/src/lab2/rosbag/close_stat.csv') #for still data in partially closed area
#file = open('/home/shak/catkin_ws/src/lab2/rosbag/close_walk.csv') #for walking data in partially closed area

csvreader = csv.reader(file)

header = []
header = next(csvreader)

rows = []
for row in csvreader:
		rows.append(row)

time = []
first = rows[0][0]

for i in rows:
	timeInSeconds = int(float(i[0])) - int(float(first))
	time.append(timeInSeconds)	

latitude = []
for i in rows:
	latitude.append(float(i[5]))

longitude = []
for i in rows:
	longitude.append(float(i[6]))
	
altitude = []
for i in rows:
	altitude.append(float(i[7]))
	
utm_easting = []
for i in rows:
	utm_easting.append(float(i[8]))
	
utm_northing = []
for i in rows:
	utm_northing.append(float(i[9]))
	
fix = []
for i in rows:
	fix.append(int(i[10]))
	

	
#graphs are in seperate .ipynb files
