# URDF Model
The urdf model is abasic diff drive robot. In the following a few important things should be mentioned.

## Structure
The model is split into a few xacro files:
- the [core file](./core.xacro) contains the body of the robot (chassis, wheels...)
- the [robot urdf](./robot.urdf.xacro) is the main file which includes all others
- under [assets](./assets/) is the control and inertia of the robot defined, there are files for ros2_control and the gazebo file (simulated control) you can switch in the launch file
- under [sensors](./sensors/) there are all available sensors which can be added to the robot. You have to uncomment them in the [robot urdf](./robot.urdf.xacro).

## Control
! the launch file lets you switch which control you want to use. In the [description launch file](../launch/description.launch.py) the parameters are defined.

## Senors
The following sensors are available:
- [camera](./sensors/camera.xacro)
- [depth camera](./sensors/depth_camera.xacro)
- [lidar](./sensors/lidar.xacro) (standard is a 3D lidar, you can change that in the config)

