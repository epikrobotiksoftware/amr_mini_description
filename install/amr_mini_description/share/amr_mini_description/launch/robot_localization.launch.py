#!/usr/bin/env python3

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch import LaunchDescription


def generate_launch_description():
    #############################################################
    use_sim_time = os.environ.get('USE_SIM_TIME', True)
    robot_localization_file_path = os.path.join(get_package_share_directory(
        'amr_mini_description'), 'config/ekf.yaml')
    robot_localization_node = Node(
        package='robot_localization',
        executable='ekf_node',
        name='ekf_filter_node',
        output='screen',
        parameters=[robot_localization_file_path,
                    {'use_sim_time': use_sim_time}]
    )
    return LaunchDescription([
        robot_localization_node
    ])
