import os
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    use_sim_time = os.environ.get('USE_SIM_TIME', True)

    goalPose_node = Node(
        package='amr_mini_description',
        executable='goalPose_pub',
        name='goalPose_pub',
        output='screen'
    )

    return LaunchDescription([
        goalPose_node
    ])
