from launch import LaunchDescription
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import IncludeLaunchDescription

package_name = "diff_drive_robot_package"

def generate_launch_description():
    robot_localization_dir = get_package_share_directory(package_name)
    parameters_file_path = os.path.join(robot_localization_dir, 'config', 'localization.yaml')
    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([os.path.join(
                get_package_share_directory(package_name),'launch','sim.launch.py'
            )]), 
            launch_arguments={'publish_odom': 'false'}.items() # xacro parameters can be set here
        ),
        Node(
            package='robot_localization', 
            executable='ekf_node', 
            name='ekf_filter_node_odom',
	        output='screen',
            parameters=[parameters_file_path],
            remappings=[('odometry/filtered', 'odometry/local')]           
            ),
        #Node(
        #    package='robot_localization', 
        #    executable='ekf_node', 
        #    name='ekf_filter_node_map',
	    #    output='screen',
        #    parameters=[parameters_file_path],
        #    remappings=[('odometry/filtered', 'odometry/global')]
        #),           
        Node(
            package='robot_localization', 
            executable='navsat_transform_node', 
            name='navsat_transform',
	        output='screen',
            parameters=[parameters_file_path],
            remappings=[('imu/data', 'imu/data'),
                        ('gps/fix', 'gps/fix'), 
                        ('gps/filtered', 'gps/filtered'),
                        ('odometry/gps', 'odometry/gps'),
                        ('odometry/filtered', 'odometry/global')]        
            )     
])