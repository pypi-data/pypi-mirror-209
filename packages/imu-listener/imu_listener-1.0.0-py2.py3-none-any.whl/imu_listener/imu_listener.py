#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Imu


class ImuListener:
    def __init__(self, imu_topic):
        self.imu_topic = imu_topic
        self.orientation_data = None
        self.angular_velocity_data = None
        self.linear_acceleration_data = None

        rospy.init_node('imu_listener', anonymous=True)
        rospy.Subscriber(self.imu_topic, Imu, self.imu_callback)
        rospy.spin()

    def imu_callback(self, data):
        # Extract and store the IMU data
        self.orientation_data = data.orientation
        self.angular_velocity_data = data.angular_velocity
        self.linear_acceleration_data = data.linear_acceleration

        # Process the IMU data here
        # Example: Print the orientation data
        rospy.loginfo("Orientation: x=%f, y=%f, z=%f",
                      self.orientation_data.x,
                      self.orientation_data.y,
                      self.orientation_data.z)


if __name__ == '__main__':
    imu_topic = '/imu/data'  # Set the IMU topic here
    imu_listener = ImuListener(imu_topic)
