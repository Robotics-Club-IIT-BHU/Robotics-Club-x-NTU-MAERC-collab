import pybullet as p
import time
import pybullet_data
physicsClient = p.connect(p.GUI)#or p.DIRECT for non-graphical version
p.setAdditionalSearchPath(pybullet_data.getDataPath()) #optionally
planeId = p.loadURDF("plane.urdf")
p.setGravity(0,0,-10)
StartOrientation = p.getQuaternionFromEuler([0,0,0])
a=0
b=1

for i in range (10000):

       y=a+b
       print (y)
      
       for n in range(y):
            StartPos=[n,0,5]
            n= p.loadURDF("sphere.urdf",StartPos, StartOrientation)
       for m in range(250):
        p.stepSimulation()
        time.sleep(1/240)
        m=m+1
        
      
       for n in range(y):
           p.removeBody(n+1)
       
       if i!=249:   
        a=b
        b=y
 
           
    
   

p.disconnect()
