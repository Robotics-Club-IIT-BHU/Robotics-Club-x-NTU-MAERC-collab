# Some Basic Stuff

Now that your PyBullet is running, its time to define or rather redefine what a robot is !!!
<p align="center">
   <img width="400" height="300" src="https://github.com/NiranthS/Pybullet-Camp/blob/master/Part1/Subpart%202/redefine.gif">
</p>

## Universal Robot Structure
<p align="center">
   <img width="444" height="500" src="https://github.com/NiranthS/Pybullet-Camp/blob/master/Part1/Subpart%202/robo.png">
</p>


Any robot is constructed by a combination of rigid bodies and joints. These rigid bodies are called Links.These links are inter related by means of different types of joints.

**Base:**
	As the name suggests, this is the primary link of the bot to which all the other links are joined.(Link 1 in the picture)

**Parent and Child links:**
          A link is named as a parent link with respect to a joint. For instance, wrt the joint 2, Link 1 is the parent and Link 3 is a child.

**Joints:**
	Any form of motion causing inter linkages are called as Joints. Joints are broadly classified into:
* Fixed: rigid connection, no motion
* Revolute: support rotation in 1 dimension (along a single axis)
* Continuous: unlimited variant of revolute joints
* Prismatic: support translation in 1 dimension (along a single axis)
* Planar: translation in two dimensions
* Floating: unlimited motion (translation and rotation) in all 6 dimentions


**Note:** In simulations we don't consider the electronic systems required for the control of the robots rather we program a joint level controller (will be explained in future parts).

## Unified Robotic Description Format (URDF)

   The Unified Robotic Description Format (URDF) is an XML file format native to ROS that describes the robot properties like geometry, mass, inertia, collision model, etc in the form of tags which is cross platform and easy to work with. Thus the same urdf of a given robot can be used across various simulation tools.

**URDF can be generated in two ways:**
1. By compiling the model  file in ROS(Robot Operating System).
2. By directly exporting the URDF of a 3D cad model.(Only Solidworks supports it)

Since, in this camp, we try exploring a beginner friendly approach towards robot simulation we don't prefer getting into ROS and also the camp aims to concentrate more on addressing the control-related problems and not the fabrication of the robot using CAD softwares. Hence,the required URDF files will be provided along with the tasks and the creation of these files is not required for now.

**Note:** 
	Though you can't create these files, you are always free to edit a given URDF file using a simple text editor (like notepad). A more in-depth understanding is provided here

1. [ROS URDF](http://wiki.ros.org/urdf/Tutorials).
2. [A sample lecture](https://ocw.tudelft.nl/course-lectures/2-2-1-introduction-to-urdf/)

## Example Implementation:
   We have added a example urdf file of a **Visual_Robot** code and a pybullet code to visualize it.You can directly download the two files and try experimenting with it.Make sure to add the path of the urdf file in the visualizer file if both the files are not present in the same folder.
	
1. Example urdf file of a R2D2 robot:-[2_R_robot.urdf](https://github.com/Robotics-Club-IIT-BHU/Robotics-Club-x-NTU-MAERC-collab/blob/main/Day_1/Some%20Basic%20Stuff/2_R_robot.urdf)
2. PyBullet code to visualize any urdf file:-[2_R_robot.py](https://github.com/Robotics-Club-IIT-BHU/Robotics-Club-x-NTU-MAERC-collab/blob/main/Day_1/Some%20Basic%20Stuff/2_R_robot.py)
	

   1. [Robot Geometry in URDF](http://wiki.ros.org/urdf/Tutorials/Create%20your%20own%20urdf%20file)
   2. [Building a Visual Robot URDF](http://wiki.ros.org/urdf/Tutorials/Building%20a%20Visual%20Robot%20Model%20with%20URDF%20from%20Scratch)

## Robot Configuration/State:
  It becomes crucial to represent the robot in 3d space in an effective way as it greatly determines the design and performance of our controller and other higher-level control modules of the robot. 
  
**Configuration Space**: The configuration of a robot is a complete specification of the position of every point of the robot.  The n-dimensional space containing all possible configurations of the robot is called the configuration space (C-space). The configuration of a robot is represented by a point in its C-space.\

**Task Space**: Task space (or Cartesian space) is defined by the position and orientation of the end effector of a robot. Joint space is defined by a vector whose components are the translational and angular displacements of each joint of a robotic link.

for eg,

<p align="center">
 <img  width="600" height="350" src=https://github.com/NiranthS/Robo-Summer-Camp-20/blob/master/Part2/Subpart%201/c_space.jpg>
</p>

## Robot orientation and position (for mobile robot):
Another important information about a robot or specifically a **mobile robot** is its absolute **position and orientation** in the simulation world. In real-world terms, it is something like the GPS position, map cordinates, compass readings. In a nutshell, we need data to get a sense of position and localization. The term orientation, however, comes into the picture when we consider **frame** based tracking of the space over position-only 3d space. Thus, if we consider a global frame with the i,j, and k directions defined, then the amount of **inclination** about all the axes (_ie. rotation ) of a **local frame** taken on the robot gives its orientation.

## Robot Orientation Formats:

**Euler angles:** 

This the most intuitive and straight forward approach towards accounting the changes in orientation with respect to a global frame.
1. [Check this video for a better picture](https://www.youtube.com/watch?v=q0jgqeS_ACM)
2. Though these angles might look like they serve the purpose, there is a very serious problem that they hold called **gimbal lock**. The solution to this will be the next type of orientation description. More details about the problem are in the links below,
   1. [Axis Angles, Euler Angles and Gimbal Lock](https://youtu.be/Mm8tzzfy1Uw)
   2. [Gimbal lock](https://www.youtube.com/watch?v=zc8b2Jo7mno)
   3. [Apollo 13 and gimbal lock](https://www.youtube.com/watch?v=OmCzZ-D8Wdk)
  
**Quaternions:**

_Q.Well, what could be an effective soltuion for a simple angle tracking problem?_ 

_You are absolutely right if complex numbers were your answer !!_

<p align="center">
<img  width="300" height="300" src="https://media2.giphy.com/media/Cn76Lj0aEw1dm/giphy.gif"><br>
</p>


We do hear you screaming that, but hold on...Quaternion is perhaps one of the most beautiful formulations in geometry.
Rather than we explaining something that is **"simply complex"**, we leave it to this beautiful work from the channel 3Blue1Brown.

<div align="center">

[Visualizing quaternions (4d numbers) with stereographic projection](https://www.youtube.com/watch?v=d4EgbgTm0Bg)

</div>
<p align="center">
<img src="https://github.com/NiranthS/Robo-Summer-Camp-20/blob/master/Part2/Subpart%202/quat1.jpg"><br>
</p>

<p align="center">
<img src=""><br>
</p>




Now, for basic information about pybullet and how to spawn urdf please visit [User manual](https://usermanual.wiki/Document/pybullet20quickstart20guide.479068914/html) [This will be the most important core source of your information through out the camp]

For detailed explanation of urdf you can watch [URDF Video](https://youtu.be/g9WHxOpAUns)

For visualization of euler,quaternions and gimbal lock visit [Angle visualization]( https://quaternions.online/ ) Note:for gimbal lock put y angle under euler to 90 degree

For visualizing your urdf on net visit  [Visualize](https://mymodelrobot.appspot.com/5629499534213120)

For slides of this topic visit [slides](https://docs.google.com/presentation/d/114ekhkQ5Lh_5CDKcpMY0d9-vZYP8y4QwgcDUFl1UFM0/edit#slide=id.gb19371b85b_0_32020)

All the urdf and codes used in presentation are added in repository download them play with them explore!!









