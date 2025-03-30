import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class TurtleBotController(Node):
    def __init__(self):
        super().__init__('turtlebot_controller')
        self.pub = self.create_publisher(Twist, '/cmd_vel', 10)

    def move_forward(self, distance=1.0, speed=0.2):
        duration = distance / speed
        twist = Twist()
        twist.linear.x = speed
        self.pub.publish(twist)
        self.get_logger().info(f'Moving forward {distance} meters')
        time.sleep(duration)
        twist.linear.x = 0.0
        self.pub.publish(twist)

    def turn(self, angle_deg=90, angular_speed=0.5):
        duration = abs(angle_deg) / (angular_speed * 57.2958)
        twist = Twist()
        twist.angular.z = angular_speed if angle_deg > 0 else -angular_speed
        self.pub.publish(twist)
        self.get_logger().info(f'Turning {angle_deg} degrees')
        time.sleep(duration)
        twist.angular.z = 0.0
        self.pub.publish(twist)

def main():
    rclpy.init()
    controller = TurtleBotController()
    rclpy.spin(controller)
    controller.destroy_node()
    rclpy.shutdown()
