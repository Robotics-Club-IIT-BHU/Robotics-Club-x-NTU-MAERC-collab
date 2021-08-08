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
