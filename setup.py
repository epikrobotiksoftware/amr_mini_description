from setuptools import setup
import os
from glob import glob
from setuptools import setup

package_name = 'amr_mini_description'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.py')),
        (os.path.join('share', package_name), glob('rviz/*')),
        (os.path.join('share', package_name+'/urdf'),
         glob('urdf/*.xacro')),
        (os.path.join('share', package_name + '/urdf/urdf_include'),
         glob('urdf/urdf_include/*')),
        (os.path.join('share', package_name+'/AmrMini_models/Amr_mini/meshes'),
         glob('AmrMini_models/Amr_mini/meshes/*')),
        (os.path.join('share', package_name+'/models/world_folder'),
            glob('models/world_folder/*')),
        (os.path.join('share', package_name+'/models/amr_mini'),
            glob('models/amr_mini/*')),
        (os.path.join('share', package_name+'/worlds'),
         glob('worlds/*')),
        (os.path.join('share', package_name+'/config'),
         glob('config/*')),

    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mkutan',
    maintainer_email='mkutan@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'joint_state_publisher_gui=joint_state_publisher_gui.joint_state_publisher:main'
        ],
    },
)
