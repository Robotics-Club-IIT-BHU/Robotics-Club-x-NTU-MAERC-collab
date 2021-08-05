import pybullet as p
import pybullet_data
import time

p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.loadURDF("plane.urdf")

p.setGravity(0, 0, -10)

huskypos = [2, 0, 0.1]
husky = p.loadURDF("husky/husky.urdf", huskypos[0], huskypos[1], huskypos[2])

numJoints = p.getNumJoints(husky)
print (numJoints)
for joint in range(numJoints):
    print(p.getJointInfo(husky, joint))
targetVel = -5  # rad/s
maxForce = 100  # Newton

for joint in range(2, 6):
    p.setJointMotorControl(husky, joint, p.VELOCITY_CONTROL, targetVel, maxForce)
for step in range(2000):
    p.stepSimulation()

targetVel = 5
for joint in range(2, 6):
    p.setJointMotorControl(husky, joint, p.VELOCITY_CONTROL, targetVel, maxForce)
for step in range(2000):
    p.stepSimulation()




