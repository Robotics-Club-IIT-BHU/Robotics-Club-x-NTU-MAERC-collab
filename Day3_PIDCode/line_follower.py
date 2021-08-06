'''
Task 3 - 

A car is loaded. You have to develop a PID controller for that car such that it runs along the line y = 0.
The line is also visible on the plane.
Callibrate the PID gains such that car gets to the line as fast as possible and follows it without much disturbance.
Refer to the past two taks and their codes for hints.

INSTRUCTIONS -
    Select the simulation window and Press ENTER to execute

'''

import numpy as np 
import pybullet as p 
import time
import math
import cv2

p_id = p.connect(p.GUI) #Loading the simulation
p.setGravity(0, 0, -10) #Setting the gravity

plane = p.loadURDF("src/plane.urdf") #Loading the plane
carPos = [0,3,0.1] #This is where the car will spawn, this is constant. 

m = 0   #Declaring the slope of the required line y = mx + c
c = 0   #Declaring the contsnat of the reuired line  y = mx + c
angle = math.atan(m)

car = p.loadURDF("src/car/car1.urdf", carPos, p.getQuaternionFromEuler([0,0,angle])) 
#Loading the car with head parallel to the given line


def printLine(m, c):  #This functions draws a line that we need to follow
    angle = math.atan(m)
    z = 0.02
    origin = [0,c,z]
    line = p.loadURDF("src/line.urdf", origin, p.getQuaternionFromEuler([0,0,angle]))

printLine(m, c)  #Calling the function to print the line


num = p.getNumJoints(car)  #Getting the total number of joints in the car
for i in range(num):
    print(p.getJointInfo(car, i))
    #Printing the information of each joint to get the motor joints


#These are the 4 motor joints that we need to manipulate, we declare them here.

fl = 2        #Front Left wheel        
fr = 3        #Front Right wheel
bl = 4        #Back Left wheel
br = 5        #Back Right wheel

p.setJointMotorControlArray(car, [fl, bl, fr, br], p.VELOCITY_CONTROL, forces = [0,0,0,0])   #This is done to enable torque control in wheels of the car
p.stepSimulation()



'''
Above this is the loading code, make no changes to it
Below this is the code that you need to work with.
'''
def callback():#Dummy function for the track-bars
    pass


cv2.namedWindow('controls')
#Creating Track-Bars that can be used to adjust the PID values in real time.

#Setting the lower and upper limits on track-bars
cv2.createTrackbar('P', 'controls', 0, 500, callback)
cv2.createTrackbar('I', 'controls', 0, 500, callback)
cv2.createTrackbar('D', 'controls', 0, 500, callback)

#Creating three different track-bars for each P-I-D
#And Loading the PID constants from the trackbars
P=cv2.getTrackbarPos('P', 'controls')/10 
I=cv2.getTrackbarPos('I', 'controls')/1000
D=5*cv2.getTrackbarPos('D', 'controls')

#press escape key to execute
k=cv2.waitKey(1) & 0xFF #This is needed to keep the track-bars active in real time
# Basically cv2.waitKey(1) returns a 32-bit integer and 0xFF makes first 24 numbers = 0 to cpompare the last 8 bits(i.e. number between 0-255) in order to verify input from our keyboard.

#Declare the desired_state and base_torque globally
desired_state = 0  #Set Value Yourself
base_torque = 10   #Set Value Yourself


def moveCar(base_torque, action):  #Enter the motor control here to move the car, give base torque and action calculated as input
    
    '''
    2=Front left
    3=Front Right
    4=Rear Left
    5=Rear Right
    '''
    
    mode=p.TORQUE_CONTROL

    left=base_torque+action
    right=base_torque-action

    print("reqd_torque_left=",left)
    print("reqd_torque_right=",right)

    p.setJointMotorControl2(car,jointIndex=2,controlMode=mode,force=left)
    p.setJointMotorControl2(car,jointIndex=3,controlMode=mode,force=right)
    p.setJointMotorControl2(car,jointIndex=4,controlMode=mode,force=left)
    p.setJointMotorControl2(car,jointIndex=5,controlMode=mode,force=right)
    #Use differential drive to nullify the error
    #The differential drive must increase or decrease the speed of the tyres about a constant base torque using gains


#Reseting all the gains to 0 at the start of the simulation
integral = 0 
derivative = 0
prev_error = 0

def calc_error(): #You can calculate the error and required action using this function

    global integral
    global derivative
    global prev_error
    P=cv2.getTrackbarPos('P', 'controls')/10 #Get P from trackbar, dividing P by 10 to get it into range of 0-50 from 0-500 as desired value is in range of 0-50 and track-bar return values between 0-500
    I=cv2.getTrackbarPos('I', 'controls')/10000 #Get I from trackbar, dividing I by 10000 to get it into range of 0-0.05 from 0-500 as desired value is in range of 0-0.05 and track-bar return values between 0-500
    D=10*cv2.getTrackbarPos('D', 'controls') #Get D from trackbar, desired value is in range of 0-500 onl

    k = cv2.waitKey(1) #This is needed to keep the track-bars active in real time real time

    state = p.getBasePositionAndOrientation(car)[0][1]
    #Getting the state, i.e. the current altitude of the drone

    x=p.getBasePositionAndOrientation(car)[0][0]  
    error=state-0
    derivative = error - prev_error
     #The D term is the difference in current error and prev error, As the simulation is called at regular intervals, we don't divide by time. It gives us the rate at which the error is changing.
    prev_error = error #Updating the prev error for using in next loop

    if(error>-0.1 and error<0.1):
        integral+=error
    pid = P * error + D * derivative+I*integral
    action=pid

    return action
    
    #Calculate error by getting the car's position using getBasePositionAndOrientation() function
    #The error is upto your imagination to select. Hint : It can be a distance between the line and the car
    #After getting the error, calculate actions using PID gains.
    #Calibrate your PID gains experimentally. Refer to the earlier tasks for hints.




'''Select the simulation window and Press ENTER to execute'''

#This while loop will run until ESCAPE key is pressed, then it will start the simulation.
while(True):
    keycode = p.getKeyboardEvents() #Getting the keyboard events through PyBullet
    if keycode.get(p.B3G_RETURN) == 1:
        #As soon as any key is pressed and it's ENTER key, simulation starts
        p.resetSimulation() #Simulation is reseted
        p.setGravity(0, 0, -10)

        plane = p.loadURDF("src/plane.urdf")
        car = p.loadURDF("src/car/car1.urdf", carPos, p.getQuaternionFromEuler([0,0,angle]))   #Plane and car loaded again

        p.setJointMotorControlArray(car, [fl, bl, fr, br], p.VELOCITY_CONTROL, forces = [0,0,0,0])   
        #This is done to enable torque control in wheels of the car
        printLine(m, c)   
        #This draws a line along y = 0, which we have to follow

        while(True):
            p.resetDebugVisualizerCamera(7, -90, -45, p.getBasePositionAndOrientation(car)[0])  #This will keep the camera on the car always

            p.stepSimulation() #This steps the simulation further by 0.01 seconds approx

            #Call all the other functions inside this while loop
            
            x=p.getBasePositionAndOrientation(car)[0][0]  
        
            action=calc_error()

            x1=p.getBasePositionAndOrientation(car)[0][0]  

            if(x>x1):
                print("Wrong.......................")
                break


            moveCar(10,action)

            time.sleep(1./240.)
            print("running")
            print("action=",action)
            print("x posn=",x)
            print("x1 posn=",x1)

            keycode = p.getKeyboardEvents()
            #This will keep tracking if ENTER key is pressed again.
            if keycode.get(p.B3G_RETURN) == 1: #We end the current simulation and start a new one again if ENTER key is pressed
                print("Episode finished")                   #This is a way to re-run the simulation without re-executing the code
                p.resetSimulation()  #Reseting the simulation
                break                #Breaking out of the inner while loop

'''Note that the optimum values for P,I,D are around 27,203 and 319'''

