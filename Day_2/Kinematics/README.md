# Introduction to Kinematics

### Kinematics is the study of the relationship between a robot's joint coordinates and its spatial layout, and is a fundamental and classical topic in robotics. 

***Kinematics*** can yield very accurate calculations in many problems, such as 
* Positioning a gripper at a place in space. 
* Designing a mechanism that can move a tool from point A to point B. 
* or Predicting whether a robot's motion would collide with obstacles.
<div align = "center">
  
  ![Gif](https://d2t1xqejof9utc.cloudfront.net/screenshots/pics/ecb2e695cc6aaa8f1de0fcc5030a6ae6/large.gif)
  
</div>  

# What we like to know?

Take the case of a 2R robot kept on a xy plane, Now let us say the end of the arm needs to reach a point (1,1,0) in 3D space, how would you go about solving this problem?

## Logically, the questions you should ask will be,

* Whether such a configuration of the robot is possible in the first place ?(given the length of links, joint angle limits, etc)

* If yes, what should be the individual angles required to be kept at the joints of the arm.

This also gives rise to the problem that is the inverse in nature. Hence, in a nutshell, we broadly classify these two problems as two types of kinematics for a given robot namely,

* Given a value for each joint angles where will my end effector be? - answered by ***Forward Kinematics***
* Given a value, the end effector target position, what will by corresponding joint angles be to reach such a configuration? - answered by ***Inverse Kinematics***
  
## *Forward Kinematics* and *Inverse Kinematics* are the tools, we'll use to tackle these problems.
<div align = "center">
  
  ![image](https://www.mathworks.com/discovery/inverse-kinematics/_jcr_content/mainParsys/image.adapt.full.medium.jpg/1623833848387.jpg)
  
</div>  

# Forward Kinematics

## ***Forward kinematics*** refers to the use of the kinematic equations of a robot to compute the position of the end-effector from specified values for the joint parameters.

The forward kinematics is an “easy” problem. This means that for each set of angles, there is one and only one result, which can be calculated with no ambiguity.

For a more in-depth mathematical perspective, you can check out this video, which solves the Forward Kinematics for a 3-DOF Robot Arm

<div align = "center">

  [![Trigonometry: Forward Kinematics Example by Mr. Kruger's Mathematics](https://img.youtube.com/vi/NRgNDlVtmz0/0.jpg)](https://www.youtube.com/watch?v=NRgNDlVtmz0)

</div>

## Task:

* Try the implementaion of a 2-DOF Robotic Arm on your own, using Pybullet. I have attached a helper code and the urdf, but only seek it just in case you are completely stuck.

## Optional Task:

* If you found that to be way easy, additionaly try implementing the above mentioned 3-DOF Robotic Arm in a similar fashion, by building your own 3-DOF Robotic Arm urdf file.

## Note:

* To be completely honest, I am obliged to inform that this is not the full picture, truth be told, you should be aware of the complications in higher dimensional robots, ***DH parameters, Transformation and Rotation Matrix-based approaches and other sophisticated formulations*** but this camp is motivated towards giving you an head start with all the wholesome fundamental concepts. So,it is essentially out of the scope of this course. You can always find good resources on the web, just in case you want to dive deeper.

# Inverse Kinematics

### ***Inverse kinematics*** is just opposite to forward kinematics. It refers to process of obtaining joint angles from known coordinates of end effector. 
<div align = "center">
  
  ![](https://gblobscdn.gitbook.com/assets%2F-M94B98WGo5doV6qgu8i%2F-MA1hvnJK_Pp1iSD8owY%2F-MA1xMW9CHZ1IkV1D99S%2FFK.gif?alt=media&token=97ffffa9-4b77-4e1e-9f2b-c1307b5cf78a)

</div>

It is in general very difficult to solve, and you may find that there may be ***no solution, one single solution or two solutions for the corresponding inverse kinematics***, but it has a lot to offer, once you get the solutions. It is often used for determining the optimum trajectory, motion planning, obstacle avoidance etc.

### You can refer to this video, to get a hands-on mathematical perspective on Inverse Kinematics for a 2-DOF Robot Arm.
<div align = "center">
  
   [![Inverse kinematics for a 2-joint robot arm using geometry](https://img.youtube.com/vi/IKOGwoJ2HLk/0.jpg)](https://www.youtube.com/watch?v=IKOGwoJ2HLk)

</div>
If you are bored and frustrated by all the math, equations, triangles and stuff. I'll suggest you to watch this video, where all the math and equations comes alive into action and creates a masterpiece. (I'll also recommend to follow this channel, if you are one of those people who absolutely love robotics.)

<div align = "center">
  
  [![Inverse kinematics Demo](https://img.youtube.com/vi/IN8tjTk8ExI/0.jpg)](https://www.youtube.com/watch?v=IN8tjTk8ExI)

</div>
Want to see something even more fascinating? Check this out !
<div align = "center">

  [![Inverse kinematics Demo](https://img.youtube.com/vi/lv6op2HHIuM/0.jpg)](https://www.youtube.com/watch?v=lv6op2HHIuM)

</div>

### ***All hail Inverse Kinematics !***

## Task:

* Try implementing Inverse Kinematics on your same 2-DOF Robotic Arm for moving it in a circle or any other trajectory. 
  
  ***Your creativity is your limit !.***
  
  I have once again attached a helper code, but try to work it out on your own as much as possible.

## Note:

* Both Forward and Inverse Kinematics, is not only used in Robotics, but finds many applications in ***3D Animations and Renderings*** as well.

# Pybullet In-built Inverse Kinematic Solver

As you can imagine, as our robots get much complicated, the equations get tricky to derive and are often nasty looking. This makes it very difficult to calculate the inverse kinematics from scratch. So,Pybullet has an ***inbuilt function*** for solving the Inverse Kinematics for a given robot urdf.

### Refer the documentation for help: [calculateInverseKinematics](https://docs.google.com/document/d/10sXEhzFRSnvFcl3XxNGhnD4N2SedqwdAvK3dsihxVUA/preview#heading=h.9i02ojf4k3ve)

## Optional Task:

* If you have worked out the 3-DOF Robotic Arm in the previous section. ***Why not take it for a spin?*** Get creative and trace out some cool trajectories, this time using the in-built functionality of Pybullet.

# Very well,

You are now equipped with a good amount of knowledge in the very ***fundamentals of Robotics.*** Ofcourse, things don't end here. There are lot more things to explore, learn and implement. There are resources everywhere around the web, that can help you achieve this. Our aim was to get you started, and lay down the foundation on which you can further build upon. 


### ***As you progress, Kinematics and Robotics can get you from this,***
<div align="center">

  ![](https://s3.amazonaws.com/cgcookie-rails/wp-uploads/2017/05/exercise_07_robot-arm.gif)  
</div>
  
### ***to this,*** 

<div align="center">

  ![](https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/sep-24-2019-11-37-27-1569339480.gif)

# All the Best !






