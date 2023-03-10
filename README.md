This package takes amr mini robot package.

Usage:

- Clone laser relay package in your workspace for merge laser

        https://github.com/epikrobotiksoftware/Laser-Relay.git

- Clone camera plugin in your workspace for using realsense camera.
  Note: Don't forget chancing branch for ros2-foxy

          https://github.com/pal-robotics/realsense_gazebo_plugin.git

- Go your workspace. Build package and install requirements.

        colcon build && source install/setup.bash

        rosdep install --from-paths src --ignore-src -r -y

- Convert your urdf to sdf for gazebo.for this go to your package.

                cd src/amr_mini_description/
                python3 requirements.py

- Open the model.sdf file in the amr_mini folder under the models folder and edit frond lidar and back lidar joint. You need to change "type".

  Like this:

        line:542    <joint name='back_lidar_joint' type='fixed'>
                            .
                            .
                            .
                     </joint>




        line: 902   <joint name='front_lidar_joint' type='fixed'>
                        .
                        .
                        .
                    </joint>

- Go your workspace

        colcon build && source install/setup.bash
        ros2 launch amr_mini_description amr_mini.launch.py

* NOTE: If you use JoyStıck and TwistMux. You need to chance topic of Joystick's "cmd_vel" topic. Replace "cmd_vel" topic with " cmd_vel_joy "
