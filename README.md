# diff_drive_robot_package
Just a simple diff drive robot package with the additional resources to be simulated in gazebo.

## Usage

1. install nessecary dependencies
```
rosdep install --from-paths src --ignore-src -r -y
```
2. build 
```
colcon build
```
3. launch
There are two launch files:
- [description](./launch/description.launch.py) just starts rsp
- [sim](./launch/sim.launch.py) starts gazebo and rsp 
```
ros2 launch <launch file>.launch.py
```

## Sources
The package is mainly derived from the package of [joshnewans](https://github.com/joshnewans) from Articulated Robotics from his series on [Making a Mobile Robot with ROS](https://articulatedrobotics.xyz/mobile-robot-full-list/). Which is a very helpful series for beginners that want to get into building robots with ros. 

## Problems that occured
- <b> gzserver crashes while loading camera plugin </b> <br>
    Error:
    ``` 
    gzclient: /usr/include/boost/smart_ptr/shared_ptr.hpp:728: typename     boost::detail::sp_member_access<T>::type boost::shared_ptr<T>::operator->() const [with T =     gazebo::rendering::Camera; typename boost::detail::sp_member_access<T>::type =  gazebo::rendering::Camera*]: Assertion `px != 0' failed.
    ```
    Solution: 
    ```
    . /usr/share/gazebo/setup.sh
    ```