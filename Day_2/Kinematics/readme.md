# Introduction to Kinematics

Kinematics is the study of the relationship between a robot's joint coordinates and its spatial layout, and is a fundamental and classical topic in robotics. 

Kinematics can yield very accurate calculations in many problems, such as 
* Positioning a gripper at a place in space. 
* Designing a mechanism that can move a tool from point A to point B. 
* or predicting whether a robot's motion would collide with obstacles.

![Gif](https://d2t1xqejof9utc.cloudfront.net/screenshots/pics/04490c17c539d3e32fb53a4af169a531/large.gif)

# What we like to know?

Take the case of a 2R robot kept on a xy plane, Now let us say the end of the arm needs to reach a point (1,1,0) in 3D space, how would you go about solving this problem?

Logically, the questions you should ask will be,

* Whether such a configuration of the robot is possible in the first place ?(given the length of links,a1 and a2 in the figure above, joint angle limits, etc)

* If yes, what should be the individual angles required to be kept at the two joints of the arm.(q1 and q2 in the figure above)

This also gives rise to the problem that is the inverse in nature. Hence, in a nutshell, we broadly classify these two problems as two types of kinematics for a given robot namely,

* Given a value for each joint angles where will my end effector be? - answered by ***Forward Kinematics***
* Given a value, the end effector target position, what will by corresponding joint angles be to reach such a configuration? - answered by ***Inverse Kinematics***
  
Forward Kinematics and Inverse Kinematics are the tools, we'll use to tackle these problems.

![image](https://www.mathworks.com/discovery/inverse-kinematics/_jcr_content/mainParsys/image.adapt.full.medium.jpg/1623833848387.jpg)

# Forward Kinematics

Putting it in a simple way,

Forward kinematics refers to the use of the kinematic equations of a robot to compute the position of the end-effector from specified values for the joint parameters.

The forward kinematics is an “easy” problem. This means that for each set of angles, there is one and only one result, which can be calculated with no ambiguity.

For a more in-depth mathematical perspective, you can check out this video, which solves the Forward Kinematics for a 3-DOF Robot

[![Trigonometry: Forward Kinematics Example by Mr. Kruger's Mathematics](https://img.youtube.com/vi/NRgNDlVtmz0/0.jpg)](https://www.youtube.com/watch?v=NRgNDlVtmz0)



