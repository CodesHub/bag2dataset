#coding:utf-8

import sys
import roslib;  
import rosbag
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from cv_bridge import CvBridgeError

rgb_path="./rgb/" #存放图片的位置
d_path="./depth/"
bag_path='2021-04-03-19-08-04.bag'
class ImageCreator():


    def __init__(self):
        self.bridge = CvBridge()
        print(bag_path);
        with rosbag.Bag(bag_path, 'r') as bag:   #要读取的bag文件；
            for topic,msg,t in bag.read_messages():
                if topic == "/camera/rgb/image_raw":  #图像的topic；
                        try:
                            cv_image = self.bridge.imgmsg_to_cv2(msg,"bgr8")
                        except CvBridgeError as e:
                            print e
                        timestr = "%.6f" %  msg.header.stamp.to_sec()
                        #%.6f表示小数点后带有6位，可根据精确度需要修改；
                        image_name = timestr+ ".png" #图像命名：时间戳.jpg
                        cv2.imwrite(rgb_path+image_name, cv_image)  #保存；
                        print(rgb_path+image_name);

                if topic == "/camera/depth_registered/hw_registered/image_rect":  #depth图像的topic；
                        try:
                            #cv_image = self.bridge.imgmsg_to_cv2(msg,"bgr8")
			    cv_image = self.bridge.imgmsg_to_cv2(msg,"16UC1")
			    #cv_image = self.bridge.imgmsg_to_cv2(msg,"32FC1")
                        except CvBridgeError as e:
                            print e
                        timestr = "%.6f" %  msg.header.stamp.to_sec()
                        #%.6f表示小数点后带有6位，可根据精确度需要修改；
                        image_name = timestr+ ".png" #图像命名：时间戳.jpg
                        cv2.imwrite(d_path+image_name, cv_image)  #保存；
                        print(d_path+image_name);


if __name__ == '__main__':

    #rospy.init_node(PKG)

    try:
        image_creator = ImageCreator()
    except rospy.ROSInterruptException:
        pass
