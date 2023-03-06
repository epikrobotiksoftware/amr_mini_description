#!/usr/bin/env python3

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

# dsadasdasdsadsadasd


def generate_launch_description():

    use_sim_time = True

    pkg_dir = get_package_share_directory('amr_mini_description')
    map_server = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            pkg_dir + '/launch/map_server.launch.py'))

    amcl = Node(
        package='nav2_amcl',
        executable='amcl',
        output='screen',
        parameters=[
            {'use_sim_time': use_sim_time}]
    )

    lifecycle_nodes = ['amcl']
    autostart = True

    start_lifecycle_manager = Node(
        package='nav2_lifecycle_manager',
        executable='lifecycle_manager',
        name='lifecycle_manager',
        output='screen',
        emulate_tty=True,
        parameters=[{'use_sim_time': use_sim_time},
                    {'autostart': autostart},
                    {'node_names': lifecycle_nodes}])

    return LaunchDescription([
        map_server,
        amcl,
        start_lifecycle_manager
    ])
