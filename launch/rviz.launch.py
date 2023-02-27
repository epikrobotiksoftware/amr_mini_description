#!/usr/bin/env python3

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch import LaunchDescription


def generate_launch_description():
    rviz2_file_name = os.environ.get('RVIZ_FILE_NAME', 'amr_mini.rviz')
    rviz_config = os.path.join(get_package_share_directory(
        'amr_mini_description'), rviz2_file_name)

    rviz_node = Node(package="rviz2",
                     executable="rviz2",
                     name="rviz2",
                     arguments=["-d", rviz_config])
    return LaunchDescription([
        rviz_node
    ])
