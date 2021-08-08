import pybullet as p
import time
import pybullet_data
physicsClient = p.connect(p.GUI)#or p.DIRECT for non-graphical version
p.setAdditionalSearchPath(pybullet_data.getDataPath()) #optionally
p.setGravity(0,0,0)
planeId = p.loadURDF("plane.urdf")
StartPos = [0,0,1]
StartOrientation = p.getQuaternionFromEuler([0,0,0])
boxId = p.loadURDF("r2d2.urdf",StartPos, StartOrientation)
for i in range (10000):
    p.stepSimulation()
    time.sleep(1./240.)
Pos, Orn = p.getBasePositionAndOrientation(boxId)
print(Pos,Orn)
p.disconnect()