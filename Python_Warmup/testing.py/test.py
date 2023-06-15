from roslibpy import ros,Topic
import rospy
import numpy as np
from PIL import Image as im
import math
from sensor_msgs.msg import Image

def message_callback(data):
    print(type(data.data))
    print("hello")

rospy.init_node('subscriber_node')
topic_name = '/locobot/camera/color/image_raw'
rospy.Subscriber(topic_name,Image,message_callback)
rospy.spin()









