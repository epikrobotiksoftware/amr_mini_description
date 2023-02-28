import os
from launch import LaunchDescription
from launch_ros.actions import Node
from launch import LaunchDescription


def generate_launch_description():
    use_sim_time = os.environ.get('USE_SIM_TIME', True)

    merge_laser_scan = Node(
        package='amr_mini_description',
        executable='merge_laser_scan',
        name='merge_laser_scan',
        output='screen',
        parameters=[{'use_sim_time': use_sim_time}],
        arguments={'front_lidar_amr_mini_laser', 'back_lidar_amr_mini_laser'}
    )

    return LaunchDescription([
        merge_laser_scan
    ])
