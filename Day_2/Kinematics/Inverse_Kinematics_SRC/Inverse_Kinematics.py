import pybullet as p
import pybullet_data
import os
import time
import math

file_name = "2R_Robotic_Arm.urdf"
p.connect(p.GUI)
p.loadURDF(os.path.join(pybullet_data.getDataPath(), "plane.urdf"), 0, 0, 0)
orn = p.getQuaternionFromEuler([0, 0, 0])
robot = p.loadURDF(file_name, [0, 0, 0], orn)
p.createConstraint(parentBodyUniqueId=robot, parentLinkIndex=0, childBodyUniqueId=-1,
                   childLinkIndex=-1, jointType=p.JOINT_POINT2POINT, jointAxis=[1, 0, 0],
                   parentFramePosition=[0, 0, 0], childFramePosition=[0, 0, 0])

l1 = 1
l2 = 1

def Inverse_kinematics(target):
    global l1, l2
    z, y = target

    angle_2 = math.acos(((y ** 2 + z ** 2) - l1 ** 2 - l2 ** 2) / (2 * l1 * l2))
    angle_1 = math.atan(y / z) - (math.atan((l2 * math.sin(angle_2)) / (l1 + l2 * math.cos(angle_2))))

    return angle_1, angle_2


# Equation of circle we will be using (y-1)^2 + (z-0.5)^2 = (0.5)^2
theta = 0
r = 0.5

y_old = 1.5
z_old = 0.5

use_custom = False  # Switch to True, for using custom Inverse_Kinematics function.

while True:

    y_new = r * math.cos(theta) + 1
    z_new = r * math.sin(theta) + 0.5

    if use_custom:
        angle_1, angle_2 = Inverse_kinematics([z_new, y_new])
    else:
        angle_1, angle_2 = p.calculateInverseKinematics(robot, 2, [0, y_new, z_new])

    p.addUserDebugLine([0, y_old, z_old], [0, y_new, z_new], [1,0,0])

    y_old = y_new
    z_old = z_new

    theta += 0.05


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
