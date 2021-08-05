import pybullet as p
import pybullet_data
import time

p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

planeId=p.loadURDF("plane.urdf", useFixedBase=True)
sphereId=p.loadURDF("sphere_small.urdf", basePosition=[0, 0, 5])

p.changeDynamics(sphereId,
                -1, 
                lateralFriction=0, 
                restitution=1, 
                linearDamping=0)

p.changeDynamics(planeId, 
                -1, 
                lateralFriction=0, 
                restitution=1, 
                linearDamping=0)

getInfo = p.getDynamicsInfo(sphereId, -1)
print(getInfo)

p.setGravity(0, 0, -9.8)

while(1):
    p.stepSimulation()
    time.sleep(1/120)
