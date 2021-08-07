import pybullet as p
import pybullet_data
import os
import time
import math

file_name = "2R_Robotic_Arm.urdf"  # Should be present in the same directory of this code.
p.connect(p.GUI)
p.loadURDF(os.path.join(pybullet_data.getDataPath(), "plane.urdf"), 0, 0, 0)
orn = p.getQuaternionFromEuler([0, 0, 0])
robot = p.loadURDF(file_name, [0, 0, 0], orn)
p.createConstraint(parentBodyUniqueId=robot, parentLinkIndex=0, childBodyUniqueId=-1,         # For fixing the robot base_plate to origin.
                   childLinkIndex=-1, jointType=p.JOINT_POINT2POINT, jointAxis=[1, 0, 0],
                   parentFramePosition=[0, 0, 0], childFramePosition=[0, 0, 0])
p.setGravity(0, 0, -10)

l1 = 1  # the length of link-1,from the urdf
l2 = 1  # the length of link-2,from the urdf


def Forward_Kinematics(angle_1, angle_2):
    # Since we are working in Y-Z plane, respective equations give the y and z cordinates of the end-effector, for the corresponding angle_1 and angle_2.
    global l1, l2
    y = (l1 * math.cos(angle_1)) + (l2 * math.cos((angle_1 + angle_2)))
    z = (l1 * math.sin(angle_1)) + (l2 * math.sin(angle_1 + angle_2))
    print("\nPosition of End-Effector : ")
    print(f"y : {y:.2f}, z : {z:.2f}")


angle_1, angle_2 = [0, math.pi/2]
Forward_Kinematics(angle_1, angle_2)

while True:
    p.setJointMotorControl2(bodyIndex=robot,
                            jointIndex=0,
                            controlMode=p.POSITION_CONTROL,
                            targetPosition=angle_1,
                            force=2000)

    p.setJointMotorControl2(bodyIndex=robot,
                            jointIndex=1,
                            controlMode=p.POSITION_CONTROL,
                            targetPosition=angle_2,
                            force=2000)
    p.stepSimulation()
    time.sleep(1. / 240.)
