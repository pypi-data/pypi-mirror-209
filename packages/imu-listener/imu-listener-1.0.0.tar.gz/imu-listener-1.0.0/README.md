# IMU Listener

ROS package for receiving IMU data from a RealSense camera using rospy.

## Installation

This package requires the following dependencies:
- rospy
 --[This packages is also installed when you install ros in your system]


## Usage

To use the IMU Listener package, follow these steps:

1. Set the IMU topic by modifying the `imu_topic` variable in the `imu_listener.py` file.

2. Run the package.


The IMU Listener will start subscribing to the specified IMU topic and display the received orientation data.

You can customize the `imu_callback` method in the `ImuListener` class to process the IMU data according to your requirements.

## License

This package is distributed under the MIT License. See the [LICENSE](LICENSE) file for more information.


