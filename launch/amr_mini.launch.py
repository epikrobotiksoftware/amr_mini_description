#!/usr/bin/env python3

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, ExecuteProcess
from launch_ros.actions import Node
import xacro
from launch import LaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    #############################################################
    use_sim_time = os.environ.get('USE_SIM_TIME', True)
    xacro_file_name = os.environ.get('XACRO_FILE_NAME', 'amr_mini.xacro')
    rviz2_file_name = os.environ.get('RVIZ_FILE_NAME', 'amr_mini.rviz')
    world_file_name = 'my_world.model'
    print("xacro_file_name : {}".format(xacro_file_name))
    #############################################################

    xacro_urdf_path = os.path.join(get_package_share_directory(
        'amr_mini_description'), 'urdf', xacro_file_name)
    robot_description_config = xacro.process_file(xacro_urdf_path)
    robot_desc = robot_description_config.toxml()

    rviz_config = os.path.join(get_package_share_directory(
        'amr_mini_description'), rviz2_file_name)

    world = os.path.join(get_package_share_directory(
        'amr_mini_description'), 'worlds', world_file_name)
    robot_localization_file_path = os.path.join(get_package_share_directory(
        'amr_mini_description'), 'config/ekf.yaml')

    params_file_dir = os.path.join(
        get_package_share_directory('amr_mini_description'), 'config', 'mapper_params_online_async.yaml')

    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')
    launch_file_dir = os.path.join(
        get_package_share_directory('slam_toolbox'), 'launch')
    #############################################################

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

    rviz_node = Node(package="rviz2",
                     executable="rviz2",
                     name="rviz2",
                     arguments=["-d", rviz_config])

    robot_localization_node = Node(
        package='robot_localization',
        executable='ekf_node',
        name='ekf_filter_node',
        output='screen',
        parameters=[robot_localization_file_path,
                    {'use_sim_time': use_sim_time}]
    )

    merge_laser_scan = Node(
        package='amr_mini_description',
        executable='merge_laser_scan',
        name='merge_laser_scan',
        output='screen',
        parameters=[{'use_sim_time': use_sim_time}]
    )
    slam_toolbox = Node(
        package='slam_toolbox',
        executable='async_slam_toolbox_node',
        name='slam_toolbox',
        output='screen',
        parameters=[params_file_dir,
                    {'use_sim_time': use_sim_time}]
    )

    map_server = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [launch_file_dir, '/online_async_launch.py']),
        launch_arguments={'use_sim_time': 'true',
                          'params_file': params_file_dir}.items(),
    )

    # rqt_robot_steering = Node(package='rqt_robot_steering',
    #                           executable='rqt_robot_steering',
    #                           name='rqt_robot_steering',
    #                           output='screen',
    #                           #   parameters=[{'use_sim_time': use_sim_time, 'robot_description': robot_desc}]
    #                           )

    return LaunchDescription([
        DeclareLaunchArgument(name='model', default_value=robot_desc,
                              description='Absolute path to robot urdf file'),

        # ExecuteProcess(
        #     cmd=['gazebo', '--verbose', world,
        #          '-s', 'libgazebo_ros_factory.so'],
        #     output='screen'),
        # spawn_entity,

        gzserver,
        gzclient,
        joint_state_publisher,
        robot_state_publisher,
        robot_localization_node,
        # rqt_robot_steering,
        merge_laser_scan,
        rviz_node,
        map_server
        # slam_toolbox

    ])
    #############################################################
