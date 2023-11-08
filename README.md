# Control of Mobile Robots
## Homework1 : ROS basics

### Notater

ROS
------------------------
rqt_graph
file:///C:/Users/M4RTI/Downloads/ROS_Cheat_Sheet_Indigo.pdf
https://www.youtube.com/watch?v=jWtkzDbez9M&list=PLLSegLrePWgIbIrA4iehUQ-impvIXdd9Q&index=5

NOTE:
- Husk Source, skriv inn i bashrc
- kan ikke kjøre flere noder med samme navn

roscore må alltid kjøre for å kunen kjøre node

rosrun navn_mappe navn_kode.py

catkin_make når ny package (mappe er laget)
catkin_create_pkg navn_mappe avhengigheter, kalt fra catkin_ws/src
catkin_make etter node lagt til!
rosrun navn_mappe navn_kode.py

rostopic 
rostopic info /chatter eks: /turtle1/cmd_vel
rostmsg show Type
rostopic echo /chatter eks: turtle1/Pose

import ny datatype til msg => må legge til ny dependencie i package.xml

rosservice list
rosservice info /add_two_ints
gir node, type og args
rosservice call /add_two_ints "a: 2 B: 10"
output-> sum: 12
- brukt til beregning / endring av innstillinger
- må kjøre en service node

rossrv show rospy_tutorials/AddTwoInts
