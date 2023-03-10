import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    use_sim_time = os.environ.get('USE_SIM_TIME', True)

    twist_mux_params = os.path.join(get_package_share_directory(
        'amr_mini_description'), 'config', 'twist_mux.yaml')
    twist_mux = Node(
        package="twist_mux",
        executable="twist_mux",
        parameters=[twist_mux_params, {
            'use_sim_time': use_sim_time}],
        remappings=[('/cmd_vel_out', '/amr_mini_description/cmd_vel')]
    )

    return LaunchDescription([
        twist_mux,
    ])
