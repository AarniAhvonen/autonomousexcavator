## Softwares/Platforms
SOLIDWORKS 2021, Creo Parametric 6.0.20

LabView 2017/2019

PyCharm/VSC

Python 3.10.5

PyQt5

ROS Noetic Ninjemys/Gazebo/RViz
Linux Ubuntu 20.04


## Installation
Clone the repo
    ```sh
    git clone https://github.com/AarniAhvonen/autonomousexcavator.git
    ```

## ROS (simulation only)
### Install ROS
The version of ROS we used is Noetic, and the operation system we used is Linux Ubuntu 20.04.

To install ROS on your local workstation, please access this page on ROS wiki:

http://wiki.ros.org/noetic/Installation/Ubuntu

### Install moveit
Install moveit and setup it according to the official tutorial:

https://ros-planning.github.io/moveit_tutorials/doc/getting_started/getting_started.html#install-ros-and-catkin

### Download related packages
1. Go the repo
    ```
    cd $Your_repository_path
    ```
2. Copy the packages:
    ```
    cp -rf jcb_description $Your_ros_workstation_src_directory
    cp -rf jcb_moveit_config $Your_ros_workstation_src_directory
    ```
3. Build the packages:
    ```
    roscd && cd ..
    catkin build / catkin_make
    source devel/setup.bash(depending on your shell setting, commonly could be sh, bash, or zsh)
    ```

### Run model in the world of simulation
Run the model:

    roslaunch jcb_moveit_config demo_gazebp.launch

### Run interface (planning path with specific positions)
Open up the interface:

    roscd jcb_moveit_config
    cd scripts
    python3 excavatorprogram2.py

A interface like this should be seen:

![Interface for planning the path][interface-screenshot]

Input the values:

    Example values: -x -1.6 -y 0 -z 1.2 -pitch -2 -roll 0 -yaw 0

Click "Send", and check the result

### Planning path with Rviz interface
A interface like this in the view of Rviz should be seen:

![Interface for planning the path][rviz-screenshot]

The is a module called "MotionPlanning". After setting up the goal state, one can plan and execute 
the planned path via pressing the button "plan" and "execute".

The simulated actions could also be seen in the view of Gazebo after excuting the planned path.


## ROS (with excavator)

### Install ROS
The version of ROS we used is Noetic, and the operation system we used is Linux Ubuntu 20.04.

To install ROS on your local workstation, please access this page on ROS wiki:

http://wiki.ros.org/noetic/Installation/Ubuntu

### Install moveit
Install moveit and setup it according to the official tutorial:

https://ros-planning.github.io/moveit_tutorials/doc/getting_started/getting_started.html#install-ros-and-catkin

### Download related packages
1. Go the repo
    ```
    cd $Your_repository_path
    ```
2. Copy the packages:
    ```
    cp -rf jcb_description $Your_ros_workstation_src_directory
    cp -rf jcb_moveit_config $Your_ros_workstation_src_directory
    ```
3. Build the packages:
    ```
    roscd && cd ..
    catkin build / catkin_make
    source devel/setup.bash(depending on your shell setting, commonly could be sh, bash, or zsh)
    ```

### Run model in the world of simulation
Run the model:

    roslaunch jcb_moveit_config demo_gazebp.launch

### Run interface
Open up the interface:

    roscd jcb_moveit_config
    cd scripts
    python3 excavatorprogram2.py

A interface like this should be seen:

![Interface for planning the path][interface-screenshot]

Input the values:

    Example values: -x -1.6 -y 0 -z 1.2 -pitch -2 -roll 0 -yaw 0

### Let the robot in simulation world goes to the same position 
1. Go the repo
    ```
    cd $Your_repository_path
    ```
2. Copy the folder with essential python codes (not necessary)
    ```
    cp -rf python_scripts_linux $some_path_contain_your_python_projects
    ```
3. Run python code
    ```
    cd $the_path_of_python_scripts_linux
    python3 init_recieve.py
    ```
4. Open a new terminal
    ```
    roscd jcb_moveit_config
    cd scripts
    python3 refractor.py
    ```
5. Plan path with the interface

    Wait for the robot in the simulation world moves to the positoin in real world, and the "Client Connected" appears in the terminal that run refractor.py

    Click the button of "send" in interface window.

[interface-screenshot]: images/interface.png
[rviz-screenshot]: images/excavator_rviz.png

# CAD/URDF
Previous CAD models created in Creo were used in the assembly of the excavator. URDF files were generated with simplyfying the assembly and utilizing SolidWorks to URDF exporter which can be found here:
http://wiki.ros.org/sw_urdf_exporter
