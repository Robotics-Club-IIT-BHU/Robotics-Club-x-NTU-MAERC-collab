'''

Task 2 -

This problem aims to experimentally show you the importance of the Integral term for removing the steady state error.

A PID controller has been implemented to adjust the altitude of the drone.
You can adjust the PID gain throught the track-bars which will appear when you run the code.

Experiment with the PID gains and observe what effect they have on the drone's motion and can you relate them with what you have learnt so far.

Find the ideal PID gains such that the drone reaches the height of 3 meters without much fluctuation and as fast/stably as possible.

Observe why it is almost impossible to control the drone perfectly with using an additional integrating term.

The code is not necessary to go through, but understanding the code will benefit while doing the Task 3 and further weeks. That's why the code has been well-commented.


INSTRUCTIONS -
    Select the simulation window and Press ENTER to execute
'''



import numpy as np 
import pybullet as p 
import time
import math
import cv2

p_id = p.connect(p.GUI)               #Loading the simulation
p.setGravity(0, 0, -10)               #Setting the gravity

plane = p.loadURDF("src/plane.urdf")     #Loading the plane
dronePos = [0,0,0.2]                     #Initial Position of the drone
drone = p.loadURDF("src/quadrotor.urdf", dronePos)      #Loading the drone


def callback():            #Dummy function for the track-bars
    pass

#P-D gains to be adjusted
cv2.namedWindow('controls')                   #Creating Track-Bars that can be used to adjust the PID values in real time.
cv2.createTrackbar('P', 'controls', 0, 500, callback)       #Setting the lower and upper limits on track-bars
cv2.createTrackbar('I', 'controls', 0, 500, callback)       #Creating three different track-bars for each P-I-D
cv2.createTrackbar('D', 'controls', 0, 500, callback)

P=cv2.getTrackbarPos('P', 'controls')/10                 #Loading the PID constants from the trackbars
I=cv2.getTrackbarPos('I', 'controls')/1000
D=5*cv2.getTrackbarPos('D', 'controls')
#press escape key to execute
k=cv2.waitKey(1) & 0xFF                                 #This is needed to keep the track-bars active in real time
#P, D = 0.1, 0.5


desired_state = 3             #This is the desired state that we want the drone to reach. That is a height of 3 meters


#Select the simulation window and Press ENTER to execute


t=0
while(True):
    if t == 0:
        p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
        p.resetDebugVisualizerCamera(cameraDistance=3.5,
                                    cameraYaw= 0,
                                    cameraPitch= 0,
                                    cameraTargetPosition = [0.0,0.0,desired_state] )
    k=cv2.waitKey(1)        #This is written to make the taskbars operate in real time
    keycode = p.getKeyboardEvents()       #Getting the keyboard events through PyBullet
    if keycode.get(p.B3G_RETURN) == 1:        #If ENTER key is pressed then the simulation executes
        integral = 0                          #Reseting all the gains to 0 at the start of the simulation
        derivative = 0
        prev_error = 0
        t = 0                               #Also setting the time to 0
        p.resetSimulation()                #Reseting the simulation
        p.setGravity(0, 0, -10)     

        plane = p.loadURDF("src/plane.urdf")        #Loading the plane and drone again
        dronePos = [0,0,0.1]
        drone = p.loadURDF("src/quadrotor.urdf", dronePos)
        state = p.getBasePositionAndOrientation(drone)[0][2]    #Getting the state to calculate error. In this case, it is the height of the drone
        p.createConstraint(drone, -1, -1, -1, p.JOINT_PRISMATIC, [0,0,1], [0,0,0], [0,0,0])  #Contraining the drone to move along Z-axis only
        p.stepSimulation()                #Stepping the simulation by a step

        while(True):
            P=cv2.getTrackbarPos('P', 'controls')/10     #Get P from trackbar, dividing P by 10 to get it into range of 0-50 from 0-500 as desired value is in range of 0-50 and track-bar return values between 0-500
            I=cv2.getTrackbarPos('I', 'controls')/1000    #Get I from trackbar, dividing I by 10000 to get it into range of 0-0.05 from 0-500 as desired value is in range of 0-0.05 and track-bar return values between 0-500
            D=5*cv2.getTrackbarPos('D', 'controls')       #Get D from trackbar, desired value is in range of 0-500 only

            '''
            Divinding factors are determined experimentally, we let track-bars have values from 0-500 
            and divide the value we get from them to get adjust them to the required range
            For example, if track-bar is at 100, but I should be around 0.01, so we divide by 10000 to get the final value in desired range.
            This is done as track-bars only support integer values
            '''

            k=cv2.waitKey(1)       #This is necessary to keep the track-bars active
            t+=0.01                 #Keeping track of time into the simulation
            state = p.getBasePositionAndOrientation(drone)[0][2]        #Getting the state, i.e. the current altitude of the drone
            error = state - desired_state                             #The error is the difference between current state and desired state
            derivative = error - prev_error             #The D term is the difference in current error and prev error, As the simulation is called at regular intervals, we don't divide by time. It gives us the rate at which the error is changing.
            prev_error = error                      #Updating the prev error for using in next loop
            if(p.getBaseVelocity(drone)[0][2]<0.01):        #Integrating/Summing the error for I gain only when drone is almost stationary, as we only want the steady state error for integration term.
                integral += error           #Summing up the error

            pid = P * error + D * derivative + I * integral    #Calculating the upthrust to be given to the drone by multiplying error with different gains and adding
            action = -pid                                   #Action is the negative of our gain , This is experimental
            print("The height is {}".format(state))

            p.applyExternalForce(drone, -1, [0,0,action], [0,0,0], p.WORLD_FRAME)   #Applying the resultant force as an upthrust on the drone.
            p.stepSimulation()              #Stepping the simulation

            time.sleep(1./240.)
            keycode = p.getKeyboardEvents()       #Getting the keyboard events through PyBullet
            if keycode.get(p.B3G_RETURN) == 1:    #Reseting the simulation when Enter is pressed
                print("Episode finished after {} timesteps".format(t+1))
                p.resetSimulation()
                p.setGravity(0, 0, -10)

                plane = p.loadURDF("src/plane.urdf")
                dronePos = [0,0,0.2]
                drone = p.loadURDF("src/quadrotor.urdf", dronePos)
                p.stepSimulation()
                break


