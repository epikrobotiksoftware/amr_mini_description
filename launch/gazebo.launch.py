#!/usr/bin/env python3

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch_ros.actions import Node

from launch import LaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    #############################################################
    use_sim_time = os.environ.get('USE_SIM_TIME', True)
    world_file_name = 'world.model'
    world = os.path.join(get_package_share_directory(
        'amr_mini_description'), 'worlds', world_file_name)

    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')

    # spawn_entity = Node(package='gazebo_ros', executable='spawn_entity.py',
    #                     arguments=["-topic", "/robot_description",
    #                                "-entity", "amr_mini_description"],
    #                     output='screen')

    gzserver = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_gazebo_ros, 'launch', 'gzserver.launch.py')
        ),
        launch_arguments={'world': world}.items(),
    )

    gzclient = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_gazebo_ros, 'launch', 'gzclient.launch.py')
        ),
    )

    return LaunchDescription([
        # ExecuteProcess(
        #     cmd=['gazebo', '--verbose', world,
        #          '-s', 'libgazebo_ros_factory.so'],
        #     output='screen'),
        # spawn_entity,
        gzserver,
        gzclient,
    ])
