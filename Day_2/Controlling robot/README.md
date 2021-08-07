# Robot Motion Control

Until now we havent addressed one of the primary control needs of a mobile robot, which is to control the indepedent joints of the robots.Motors as we all are aware of, are machines that induce some form of motion, by creating a torque in the case of rotational motors and a force in the case of linear motor/actuators.Thus,motors are the motion causing elements of a robot.However, in simulation the details,specifications and design of a given motor type is insignificant and we only need the physical properties of that motor we want to mimic.             
                                   <p align="center">
                                   <img src="https://user-images.githubusercontent.com/88087656/128511757-72278964-4ee9-408b-9b1f-def5eb93ba8c.gif" width="450" height="450" />
                                   </p>
        
                                 
So, every motor in Pybullet is characterized by the maximum velocity and maximum force (it is generalized velocity and force as in lagrangian mechanics and hence it is angular velocity and torque in rotational motors) it can exert.Every joint by default has a motor attached to it and hence we just need to give the motor's desired position / velocity / torque to control them.

#### Controlling the robot state in Pybullet basically involves-
- Obtaining joint information/ Reading joint State
- Determining the control action
- Setting the desired control mode

## Querying robot Info and configuration in PyBullet

Here are some important functions which are used in getting the details of links, joints and the state of robot. Each link has well documented input parameters and outputs.<br />
                                     <p align="center">
                                     [Base, Joint, Links](https://docs.google.com/document/d/10sXEhzFRSnvFcl3XxNGhnD4N2SedqwdAvK3dsihxVUA/preview#heading=h.e27vav9dy7v6)<br />
                                     [getnumJoints,getJointInfo](https://docs.google.com/document/d/10sXEhzFRSnvFcl3XxNGhnD4N2SedqwdAvK3dsihxVUA/preview#heading=h.la294ocbo43o) <br />
                          [getJointState, resetJointState](https://docs.google.com/document/d/10sXEhzFRSnvFcl3XxNGhnD4N2SedqwdAvK3dsihxVUA/preview#heading=h.p3s2oveabizm) <br />
  [getLinkState](https://docs.google.com/document/d/10sXEhzFRSnvFcl3XxNGhnD4N2SedqwdAvK3dsihxVUA/preview#heading=h.3v8gjd1epcrt) <br />
  [getBaseVelocity](https://docs.google.com/document/d/10sXEhzFRSnvFcl3XxNGhnD4N2SedqwdAvK3dsihxVUA/preview#heading=h.4vxw9j7piyjd) <br />
                                     </p>   
                                     
# Time to Control !                             
We can control a robot by setting a desired control mode for one or more joint motors. During the stepSimulation the physics engine will simulate the motors to reach the given target value that can be reached within the maximum motor forces and other constraints. 
                                    
#### We have to our rescue [setJointMotorControl2](https://docs.google.com/document/d/10sXEhzFRSnvFcl3XxNGhnD4N2SedqwdAvK3dsihxVUA/preview#heading=h.jxof6bt5vhut)
setMotorControl2 is an import function which is used to control the motors in our robot by providing the desired velocity and max force to use to reach the desired velocity

### Modes of Control-
* Position control mode
* Velocity control mode
* Torque control mode

##### POSITION_CONTROL 
This happens when the joint motor is enabled as well as the control loop.You simply need to specify the position you want a particular joint (specified by joint unique ID) to be at. 

For example- Take the case of a 2R robot arm <p align="center">
![2r_arm](https://user-images.githubusercontent.com/88087656/128523942-1121220e-7486-4950-a6c7-faaf451c0432.png)
<p />

Here theta_1 and theta_2 can be set as desired for both the joints.
###### CAUTION- The position needs to be in radians since the joints here are revolute. We can use position in meters for prismatic joint.
You can refer to the demo code attached to understand this mode better.

##### VELOCITY_CONTROL
Here joint motor is on or enabled while the control loop is disabled. You can feed in the desired velocity along with the torque limits .When that maximum torque/force is very high, the target velocity is instantaneously reached and the joint operates in velocity control, otherwise it operates at the specified torque/force until the desired target velocity is reached. <p align="center">
<img src="https://user-images.githubusercontent.com/88087656/128541414-9432d1c0-e031-44f0-b544-d6da7edca863.gif" width="350" height="300"/>
 <p />
 
 Now try to perform velocity control over a husky. You can take reference of the helper code attached in case you get stuck.
 
 ##### TORQUE_CONTROL
 Torque control mode makes motor a torque or force transducer.You can set the desired torque/force to be applied on a joint at each simulation step. Be cautious with this control since  simulating the correct forces relies on very accurate URDF/SDF file parameters and system identification (correct masses, inertias, center of mass location, joint friction etc).
 
 For an in depth understanding of these modes you can refer [here](https://www.coppeliarobotics.com/helpFiles/en/jointDescription.htm)
 
 ### Do we need to call the function multiple times??
 
 Definitely not! For a multi-joint system we can use [setJointMotorControlArray](https://docs.google.com/document/d/10sXEhzFRSnvFcl3XxNGhnD4N2SedqwdAvK3dsihxVUA/preview#heading=h.jxof6bt5vhut) which would reduce the calling overhead by performing control over multiple joints together.<p align="center"/>
<img src="https://user-images.githubusercontent.com/88087656/128605124-57764516-63d4-4f5c-b15b-d1e1ddc8ad06.jpg" width="350" height="300"/>
</p>

# External Force/Torque:
Q.Why do we really need to simulate a external force on the robot ??

Ans: To kick robots and bully them and have fun !! why,else ?:-)<p align="center"/>
![](https://camo.githubusercontent.com/78e5c9e3a709d1dc825ed5153602d8f128422aa924b475175bbf54610761d3e0/68747470733a2f2f6d656469612e67697068792e636f6d2f6d656469612f3372675842494e65706165715372314f664b2f67697068792e676966)
</p>
Well on a serious note,one of the key challenge to overcome in transfering a robot from simulation to reality is the undezireable and unpredictable disturbance caused in the real world.The source of these disturbances that hinders the motion of our robot is generally a force or torque.Thus, as robotic professionals it is important that we make robot controllers that are robust,agile and versatile.So, we should learn to simulate such undezirable conditions in our simulations aswell.

The function(s) that enables you to design such forces are designed below:<p align="center"/>
[applyExternalForce/Torque](https://docs.google.com/document/d/10sXEhzFRSnvFcl3XxNGhnD4N2SedqwdAvK3dsihxVUA/preview#heading=h.mq73m9o2gcpy)
</p>

# Constraints:
Constraints limit the movement of two rigid bodies in relation to each other, or the movement of one body in relation to the global world space. Another often used term word for constraints is joint.There might be scenarios where we need to apply constraints in between the robot and a unit in the environment and simulate such constrained conditions.<p align="center"/>
<img src="https://forum-files-playcanvas-com.s3.dualstack.eu-west-1.amazonaws.com/original/2X/a/a9f5d9f46af0846fbee00c8e73f86885d907a403.gif">
</p>
We create bodies as a tree-structures without loops. 







                                                
 
                                                 
                                                 
                                                 
                                                 

