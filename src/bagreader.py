import bagpy
from bagpy import bagreader 
import rosbag
import pandas as pd

bag = bagreader('/home/shak/catkin_ws/src/lab2/rosbag/close_walk.bag')

readings = bag.message_by_topic('/GPS/gps_data')
print(readings)
