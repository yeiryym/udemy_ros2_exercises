#!/usr/bin/env python3

import rclpy
from rclpy.node import Node 
from std_msgs.msg import Float32 # import data type 

WHEEL_RADIUS = 12.5 / 100 # Cm to m 


class SpeedCalculator(Node): # initialize class node 
	def __init__(self):
		super().__init__("speed_calc_node") # initializing node, "name of node"
		self.sub = self.create_subscription(Float32, "rpm", self.calculate_speed, 10) # (msg type, topic subscribed to, callback function?, rate)
		self.pub = self.create_publisher(Float32, "rpm", 10)

	def calculate_speed(self,rpm_msg): # rpm_msg is variable where the data is being stored 
		speed = rpm_msg.data * WHEEL_RADIUS * 2 * 3.14159 / 60  # Speed in m/s
		speed_msg = Float32()  # Variable for the data 
		speed_msg.data = float(speed) # Load in the actual data "speed"
		self.pub.publish(speed_msg) # Publish the data 
        



def main(args=None): 
	rclpy.init()
	speed_calc_node = SpeedCalculator()
	print("Speed Calculator Node Started")

	try: 
		rclpy.spin(speed_calc_node)
	except KeyboardInterrupt: 
		print("Terminating Node...")
		speed_calc_node.destroy_node()

if __name__ == '__main__':
	main()