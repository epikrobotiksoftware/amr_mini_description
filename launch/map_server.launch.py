#!/usr/bin/env python3

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
import launch_ros.actions


def generate_launch_description():
    use_sim_time = os.environ.get('USE_SIM_TIME', True)
    map_yaml_file = os.path.join(get_package_share_directory(
        'amr_mini_description'), 'maps/my_map_save.yaml')

    map_server_cmd = Node(
        package='nav2_map_server',
        executable='map_server',
        output='screen',
        parameters=[{'yaml_filename': map_yaml_file,
                    'use_sim_time': use_sim_time}]
        # parameters=[map_config_path,
        #             ]  # both work
    )

    lifecycle_nodes = ['map_server']

    autostart = True

    start_lifecycle_manager_cmd = launch_ros.actions.Node(
        package='nav2_lifecycle_manager',
        executable='lifecycle_manager',
        name='lifecycle_manager',
        output='screen',
        emulate_tty=True,
        parameters=[{'use_sim_time': use_sim_time},
                    {'autostart': autostart},
                    {'node_names': lifecycle_nodes}])

    return LaunchDescription([
        map_server_cmd,
        start_lifecycle_manager_cmd
    ])
