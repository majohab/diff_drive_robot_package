import os

from ament_index_python.packages import get_package_share_directory


from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, SetEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, EnvironmentVariable


from launch_ros.actions import Node
from scripts import GazeboRosPaths

package_name='diff_drive_robot_package'

def generate_launch_description():

    # Check if odom tf should be published
    publish_odom = LaunchConfiguration('publish_odom') # only relevant if ros2_control=true

    # set paths
    model_path, plugin_path, media_path = GazeboRosPaths.get_paths()
    print(f"The following gazebo paths where detected: model_path: {model_path}, plugin_path: {plugin_path}, media_path: {media_path}")

    # set env variables
    SetEnvironmentVariable(name='GAZEBO_MODEL_PATH', value=[EnvironmentVariable('GAZEBO_MODEL_PATH'), model_path])
    SetEnvironmentVariable(name='GAZEBO_PLUGIN_PATH', value=[EnvironmentVariable('GAZEBO_PLUGIN_PATH'), plugin_path])
    SetEnvironmentVariable(name='GAZEBO_RESOURCE_PATH', value=[EnvironmentVariable('GAZEBO_RESOURCE_PATH'), media_path])

    # launch rsp
    rsp = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory(package_name),'launch','description.launch.py'
                )]), 
                launch_arguments={'use_sim_time': 'true', 'use_ros2_control': 'true', 'publish_odom': publish_odom}.items() # xacro parameters can be set here
    )

    # gazebo
    gazebo_params_file = os.path.join(get_package_share_directory(package_name),'config','gazebo_params.yaml')
    gazebo = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')]),
                launch_arguments={'extra_gazebo_args': '--ros-args --params-file ' + gazebo_params_file}.items()
             )

    # Run the spawner node from the gazebo_ros package. 
    spawn_entity = Node(package='gazebo_ros', executable='spawn_entity.py',
                        arguments=['-topic', 'robot_description',
                                   '-entity', 'diff_drive_robot'],
                        output='screen')

    diff_drive_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["diff_cont"],
    )

    joint_broad_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["joint_broad"],
    )

    # Launch them all!
    return LaunchDescription([
        rsp,
        gazebo,
        spawn_entity,
        diff_drive_spawner,
        joint_broad_spawner,
    ])