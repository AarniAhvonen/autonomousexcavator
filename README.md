# JCB mini excavator
Best excavator in the world

## Programs used
SOLIDWORKS 2021, Creo Parametric 6.0.20

LabView 2017/2019

PyCharm/VSC
Python 3.10.5
PyQt5

ROS Noetic Ninjemys/Gazebo/RViz
Linux Ubuntu 20.04
Teams


## Installation
Clone the repo
    ```sh
    git clone https://github.com/AarniAhvonen/autonomousexcavator.git
    ```


## ROS

### Install ROS
The version of ROS we used is Noetic, and the operation system we used is Linux Ubuntu 20.04.

To install ROS on your local workstation, please access this page on ROS wiki:

http://wiki.ros.org/noetic/Installation/Ubuntu

### Install moveit
Install moveit and setup it according to the official tutorial:

https://ros-planning.github.io/moveit_tutorials/doc/getting_started/getting_started.html#install-ros-and-catkin

### Download related packages
1. Go the repo
    ```sh
    cd $Your_repository_path
    ```
2. Copy the packages:
    ```sh
    cp -rf jcb_description $Your_ros_workstation_src_directory
    cp -rf jcb_moveit_config $Your_ros_workstation_src_directory
    ```
3. Build the packages:
    ```sh
    roscd && cd ..
    catkin build / catkin_make
    source devel/setup.bash(depending on your shell setting, commonly could be sh, bash, or zsh)
    ```

### Run model in the world of simulation
Run the model:
    ```sh
    roslaunch jcb_moveit_config demo_gazebp.launch
    ```

### Prepare interface
Get the interface:
    ```sh
    roscd jcb_moveit_config
    cd scripts
    python3 excavatorprogram2.py
    ```
A interface like this should be seen:
![Interface for planning the path][interface-screenshot]

Input the values:
    ```sh
    Example values: -x -1.6 -y 0 -z 1.2 -pitch -2 -roll 0 -yaw 0
    ```

### Let the robot in simulation world goes to the same position 
1. Go the repo
    ```sh
    cd $Your_repository_path
    ```
2. Copy the folder with essential python codes (not necessary)
    ```sh
    cp -rf python_scripts_linux $some_path_contain_your_python_projects
    ```
3. Run python code
    ```sh
    cd $the_path_of_python_scripts_linux
    python3 init_recieve.py
    ```
4. Open a new terminal
    ```sh
    roscd jcb_moveit_config
    cd scripts
    python3 refractor.py
    ```

### Plan path with the interface
Wait for the robot in the simulation world moves to the positoin in real world, and the "Client Connected" appears in the terminal that run refractor.py

Click the button of "send" in interface window.

[interface-screenshot]: images/interface.png

## CAD
Previous CAD models created in Creo were used in the assembly of the excavator. 
### URDF
URDF files were generated with simplyfying the assembly and utilizing SolidWorks to URDF exporter which can be found here:

http://wiki.ros.org/sw_urdf_exporter
