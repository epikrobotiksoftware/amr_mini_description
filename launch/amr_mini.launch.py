#!/usr/bin/env python3

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch_ros.actions import Node
import xacro
from launch import LaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    #############################################################
    use_sim_time = os.environ.get('USE_SIM_TIME', True)

    pkg_dir = get_package_share_directory('amr_mini_description')

    xacro_file_name = os.environ.get('XACRO_FILE_NAME', 'amr_mini.xacro')
    xacro_urdf_path = os.path.join(get_package_share_directory(
        'amr_mini_description'), 'urdf', xacro_file_name)
    robot_description_config = xacro.process_file(xacro_urdf_path)
    robot_desc = robot_description_config.toxml()
    #############################################################

    robot_state_publisher = Node(package='robot_state_publisher',
                                 executable='robot_state_publisher',
                                 parameters=[{'use_sim_time': use_sim_time,
                                              'robot_description': robot_desc}])

    joint_state_publisher = Node(package='joint_state_publisher',
                                 executable='joint_state_publisher',
                                 name='joint_state_publisher',
                                 parameters=[
                                     {'use_sim_time': use_sim_time}],
                                 )

    # rqt_robot_steering = Node(package='rqt_robot_steering',
    #                           executable='rqt_robot_steering',
    #                           name='rqt_robot_steering',
    #                           output='screen',
    #                           #   parameters=[{'use_sim_time': use_sim_time, 'robot_description': robot_desc}]
    #                           )

    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            pkg_dir + '/launch/gazebo.launch.py'))

    rviz_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            pkg_dir + '/launch/rviz.launch.py'))

    robot_localization_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            pkg_dir + '/launch/robot_localization.launch.py'))

    merge_laser_scan_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            pkg_dir + '/launch/merge_lidar.launch.py'))

    mapping_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            pkg_dir + '/launch/mapping.launch.py'))

    amcl_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            pkg_dir + '/launch/amcl.launch.py'))

    return LaunchDescription([
        DeclareLaunchArgument(name='model', default_value=robot_desc,
                              description='Absolute path to robot urdf file'),

        gazebo_launch,
        joint_state_publisher,
        robot_state_publisher,
        robot_localization_launch,
        # rqt_robot_steering,
        merge_laser_scan_launch,
        rviz_launch,
        # mapping_launch,
        amcl_launch,
    ])
    #############################################################
