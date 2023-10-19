from setuptools import find_packages, setup
from os.path import join
from glob import glob

package_name = 'diff_drive_robot_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (join('share', package_name, 'launch'), glob(join('launch', '*launch.[pxy][yma]*'))),
        (join('share', package_name, 'urdf'), glob('urdf/**/*.xacro', recursive=True)),
        (join('share', package_name, 'config'), glob('config/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='majohab',
    maintainer_email='todo@todo.com',
    description='The description of a basic diff drive robot',
    license='BSD-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
