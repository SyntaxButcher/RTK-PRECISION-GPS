#!/usr/bin/env python
# -*- coding: utf-8 -*-S

import rospy
import serial
import utm
from math import sin, pi
from lab2.msg import custom

def parse_GNGGA(line):
	line_array = line.split(',')
	if line_array[3] == "N":
		DD = int(float(line_array[2])/100)
		MM = (float(line_array[2]) - (DD*100))/60
		GPS_lat = DD + MM
	else:
		DD = int(float(line_array[2])/100)
		MM = (float(line_array[2]) - (DD*100))/60
		GPS_lat = (DD + MM) * (-1)
	if line_array[5] == "E":	
		DD = int(float(line_array[4])/100)
		MM = (float(line_array[4]) - (DD*100))/60
		GPS_lon = DD + MM
	else:
		DD = int(float(line_array[4])/100)
		MM = (float(line_array[4]) - (DD*100))/60
		GPS_lon = (DD + MM) * (-1)
	GPS_alt = line_array[9]
	GPS_fix = int(line_array[6])
	return GPS_lat, GPS_lon, GPS_alt, GPS_quality

def talker():
	SENSOR_NAME = "GPS"
	pub = rospy.Publisher('GPS/gps_data', custom, queue_size=10)
	rospy.init_node('GPS_node', anonymous=True)
	serial_port = rospy.get_param('~port','/dev/ttyACM0')
	serial_baud = rospy.get_param('~baudrate',57600)
	port = serial.Serial(serial_port, serial_baud, timeout=3.)
	rate = rospy.Rate(10)
	GPS = custom()
	GPS.header.frame_id = "GPS"
	GPS.header.seq = 0
	GPS.header.stamp = rospy.Time.now()
	while not rospy.is_shutdown():
		rospy.sleep(0.2)
		line = port.readline()
		line = str(line)
		if "GNGGA" in line:
			GPS.latitude, GPS.longitude, GPS.altitude, GPS.fix = parse_GNGGA(line)
			GPS.utm_easting, GPS.utm_northing, GPS.Zone, GPS.letter = utm.from_latlon(GPS.latitude, GPS.longitude)
			rospy.loginfo(GPS)
			pub.publish(GPS)
			GPS.header.seq += 1


			
if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass

  
    

