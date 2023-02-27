#!/usr/bin/env python3

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, ExecuteProcess
from launch_ros.actions import Node
import xacro
from launch import LaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
import time


def generate_launch_description():

    params_file_dir = os.path.join(
        get_package_share_directory('amr_mini_description'), 'config', 'mapper_params_online_async.yaml')

    launch_file_dir = os.path.join(
        get_package_share_directory('slam_toolbox'), 'launch')
    # slam_toolbox = Node(
    #     package='slam_toolbox',
    #     executable='async_slam_toolbox_node',
    #     name='slam_toolbox',
    #     output='screen',
    #     parameters=[params_file_dir,
    #                 {'use_sim_time': use_sim_time}]
    # )

    map_server = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [launch_file_dir, '/online_async_launch.py']),
        launch_arguments={'use_sim_time': 'true',
                          'params_file': params_file_dir}.items(),
    )

    return LaunchDescription([
        # slam_toolbox,
        map_server,
    ])
