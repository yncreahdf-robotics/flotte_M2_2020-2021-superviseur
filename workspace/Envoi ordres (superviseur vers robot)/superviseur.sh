#!/bin/bash

echo "launching launch file"

source /opt/ros/kinetic/setup.bash
source /home/nassima/catkin_ws/devel/setup.bash

roslaunch superviseur superviseur.launch
