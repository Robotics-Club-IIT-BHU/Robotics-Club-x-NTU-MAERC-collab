# Robot Motion Control

Until now we havent addressed one of the primary control needs of a mobile robot, which is to control the indepedent joints of the robots.Motors as we all are aware of, are machines that induce some form of motion, by creating a torque in the case of rotational motors and a force in the case of linear motor/actuators.Thus,motors are the motion causing elements of a robot.However, in simulation the details,specifications and design of a given motor type is insignificant and we only need the physical properties of that motor we want to mimic.


So, every motor in Pybullet is characterized by the maximum velocity and maximum force (it is generalized velocity and force as in lagrangian mechanics and hence it is angular velocity and torque in rotational motors) it can exert.Every joint by default has a motor attached to it and hence we just need to give the motor's desired position / velocity / torque to control them.setMotorControl2 is an import function which is used to control the motors in our robot by providing the desired velocity and max force to use to reach the desired velocity

#### Controlling the robot state in Pybullet basically involves-
- Obtaining joint information/ Reading joint State
- Determining the control action
- Setting the desired control mode




                                                
 
                                                 
                                                 
                                                 
                                                 

