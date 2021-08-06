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
Here joint motor is on or enabled while the control loop is disabled. You can feed in the desired velocity along with the torque limits .When that maximum torque/force is very high, the target velocity is instantaneously reached and the joint operates in velocity control, otherwise it operates at the specified torque/force until the desired target velocity is reached.







                                                
 
                                                 
                                                 
                                                 
                                                 

