import os
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    use_sim_time = os.environ.get('USE_SIM_TIME', True)

    initialpose = Node(
        package='amr_mini_description',
        executable='initialpose_pub',
        name='initialpose_pub',
        output='screen'
    )

    return LaunchDescription([
        initialpose
    ])
