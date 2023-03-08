This package takes amr mini robot package.

Usage:

- Clone laser relay package

        https://github.com/epikrobotiksoftware/Laser-Relay.git

- Go your workspace. Build package and install requirements.

        colcon build && source install/setup.bash
        cd src/amr_mini_description/
        python3 requirements.py

- Open the model.sdf file in the amr_mini folder under the models folder and edit frond lidar and Back lidar joint. change type and remove axis.

  Like this:

              <joint name='front_lidar_joint' type='fixed'>
                  <pose relative_to='base_footprint'>0.34 0.22 0.27 0 -0 0</pose>
                  <parent>base_footprint</parent>
                  <child>front_lidar_laser_link</child>
              </joint>

- Go your workspace

        colcon build && source install/setup.bash
        ros2 launch amr_mini_description amr_mini.launch.py
