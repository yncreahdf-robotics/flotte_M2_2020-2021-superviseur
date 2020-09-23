# Docker ROS Superviseur Image

This is a Docker Image.

**Requirements :**
-Docker Desktop(for Windows or Mac)
-Docker Engine (for Linux)

## Getting Started !

First clone this image :
    
    docker pull docker.pkg.github.com/yncreahdf-robotics/flotte_m2_2020-2021-<yourproductname>/ros:mykinetic

Then build the image using Docker

    docker build --tag ros:mykinetic 

Next go to your wanted directory and pull your repo in this directory.

    git pull <yourrepo>

Check if you have build your network:

    docker network ls

If you have a network called ros skip the next step if not do:

    docker network create ros

Then check with:

    docker network ls


Finally run your image

    docker run --rm -it --net ros -e WORKSPACE_NAME=workspace -v $(pwd)/workspace:/root/workspace -w /root/workspace/catkin_ws ros:<yourimagename>



sudo docker login https://docker.pkg.github.com -u USERNAME -p PASSWORD


Now you are ready for next section.

## Launch

The wokspace folder contains all your dependencies.
Now you can launch all your Ros command and developp your nodes.
---------------------------

## ROS Nodes

Here is a list of the nodes :
- drive
- odom
- controller
- joy_node (from external package xbox_controller)

### drive
- **Sets up the communication** between the computer and the physical **RoboteQ drivers**. 
- Sends **commands** to control the **motors** via the drivers.
- Gets **feedbacks** from **encoders** and publishes them. 

> Based on the API provided by RoboteQ the drivers manufacturer.

### odom
**Computes** and **publishes** odometry over ROS using tf.

### controller
Translates inputs from **Xbox controller** to Twist to make the robot move.

*Useful command :*

    rosnode info <node>

---------------------------
## Useful ROS Topics

Topics are defined under a **namespace**. If you have a fleet of robots that operate on one **ROS_MASTER**, you will have those topics preceded by the name of each robot.

> **For example :** My robot is named Heron01
The following topics will be `/Heron01/...`

|Topic|message type|Publisher Node|Subscriber Node|
|---|:---|:---|:---|
|`cmd_vel`|*Twist*|controller|drive|
|`odom`|*Odometry*| odom|
|`sensor_encs`|custom|drive|odom|
|`joy`|*Joy*|joy_node (from external package)|controller|

*Useful commands :*

    rostopic list
    rostopic echo <topic>
    rostopic pub <topic> <message type> <data>

