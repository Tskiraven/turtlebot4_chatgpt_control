from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlebot4_chatgpt_control',
            executable='terminal_control',
            output='screen'
        )
    ])
