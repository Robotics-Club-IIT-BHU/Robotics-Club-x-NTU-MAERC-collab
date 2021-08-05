import pybullet as p
import time
import math

import pybullet_data

p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.loadURDF("plane.urdf")

cubeId_1 = p.loadURDF("cube.urdf", 0, 0, 1)
cubeId_2 = p.loadURDF("cube.urdf", 1, 0, 1)

p.setGravity(0, 0, 0)

# FIXED JOINT
# pid_1 = p.createConstraint(cubeId_1, -1, -1, -1, p.JOINT_POINT2POINT, [0, 0, 0], [0, 0, 0], [0, 0, 1])
# cid_1 = p.createConstraint(cubeId_1, -1, cubeId_2, -1, p.JOINT_FIXED, [0, 0, 0], [0.5,0,1], [-0.5, 0, 1])

# POINT2POINT JOINT
# pid_1 = p.createConstraint(cubeId_1, -1, -1, -1, p.JOINT_FIXED, [0, 0, 0], [0, 0, 0], [0, 0, 1])
# cid_1 = p.createConstraint(cubeId_1, -1, cubeId_2, -1, p.JOINT_POINT2POINT, [0, 0, 0], [0.5,0,0.5], [-0.5, 0, 0.5])

# PRISMATIC JOINT
# pid_1 = p.createConstraint(cubeId_1, -1, -1, -1, p.JOINT_POINT2POINT, [0, 0, 0], [0, 0, 0], [0, 0, 1])
# cid_1 = p.createConstraint(cubeId_1, -1, cubeId_2, -1, p.JOINT_PRISMATIC, [0, 0, 0], [0.5,0,1], [-0.5, 0, 1])


for i in range(10000):
    p.stepSimulation()
    time.sleep(0.001)
