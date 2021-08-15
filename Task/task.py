'''
Task -

A car is loaded. You have to develop a PID controller for that car such that it runs along the circular track.
The trajectory of the track is given by x^2 + y^2 = 3^2
Calibrate the PID gains such that car follows the line without much disturbance.

INSTRUCTIONS -
    Select the simulation window and Press ENTER to execute
'''

import pybullet as p
import time
import math
import cv2


def printTrack():  # This functions draws the track that we need to follow.
    theta = 0
    r = 3           # The track is a circle of radius 3 centred at origin.
    while theta <= 2 * math.pi:
        theta += 0.1
        z = 0.02
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        line = p.loadURDF("src/line.urdf", [x, y, z], p.getQuaternionFromEuler([0, 0, theta + math.pi / 2]))


p_id = p.connect(p.GUI)
p.setGravity(0, 0, -10)
plane = p.loadURDF("src/plane.urdf")
carPos = [0, 3, 0.1]
car = p.loadURDF("src/car/car1.urdf", carPos, p.getQuaternionFromEuler([0, 0, 0]))
printTrack()

num = p.getNumJoints(car)  # Getting the total number of joints in the car
for i in range(num):
    print(p.getJointInfo(car, i))  # Printing the information of each joint to get the motor joints

# These are the 4 motor joints that we need to manipulate, we declare them here.

fl = 2  # Front Left wheel
fr = 3  # Front Right wheel
bl = 4  # Back Left wheel
br = 5  # Back Right wheel

p.setJointMotorControlArray(car, [fl, bl, fr, br], p.VELOCITY_CONTROL, forces=[0, 0, 0, 0])
# This is done to enable torque control in wheels of the car
p.stepSimulation()

'''
Above this is the loading code, make no changes to it
Below this is the code that you need to work with.
'''


def callback():   # Callback for the trackbars, leave empty.
    pass

# Declaring the Trackbars, use this to tune your PID.

''' Remember trackbars can only set integer values, therefore after getting values from these trackbars,
  using cv2.getTrackbarPos(), you might have to scale up or down these values appropriately. 
 For eg. If your I gains are found to be in the range of 0 - 0.1, you will scale down the I values by 10,0000.
 For more information on trackbars, refer OpenCV documentation.
'''

cv2.namedWindow('Controls')
cv2.createTrackbar('P', 'Controls', 0, 1000, callback)
cv2.createTrackbar('I', 'Controls', 0, 1000, callback)
cv2.createTrackbar('D', 'Controls', 0, 1000, callback)

# Declare the desired_state and base_torque globally
desired_state = 0  # Set Value Yourself
base_torque = 0  # Set Value Yourself


def moveCar(base_torque, action):
    pass
    # Enter the motor control here to move the car, give base torque and action calculated as input
    # Use p.JointMotorControlArray() function in torque mode
    # Use differential drive.
    # The differential drive must increase or decrease the speed of the tyres about a constant base torque using gains


def pid_control():  # You can calculate the error and required action using this function
    pass
    # Calculate error by getting the car's position using getBasePositionAndOrientation() function
    # The error is up to your imagination to select. Hint : It can be the distance between the origin and the car
    # After getting the error, calculate and return action using the PID Equation
    # Calibrate your PID gains experimentally.


# Select the simulation window and Press ENTER to execute

while True:  # This while loop will run until ESCAPE key is pressed, then it will start the simulation.
    k = cv2.waitKey(1)
    keycode = p.getKeyboardEvents()
    if keycode.get(p.B3G_RETURN) == 1:  # As soon as any key is pressed and it's ENTER key, simulation starts
        p.resetSimulation()
        p.setGravity(0, 0, -10)
        plane = p.loadURDF("src/plane.urdf")
        car = p.loadURDF("src/car/car1.urdf", carPos, p.getQuaternionFromEuler([0, 0, 0]))  # Plane and car loaded again
        p.setJointMotorControlArray(car, [fl, bl, fr, br], p.VELOCITY_CONTROL, forces=[0, 0, 0, 0])
        printTrack()

        while True:
            p.resetDebugVisualizerCamera(7, -90, -45, p.getBasePositionAndOrientation(car)[0])  # This will keep the camera on the car always
            p.stepSimulation()  # This steps the simulation further by 0.01 seconds approx

            action = pid_control()  # Calculate actions using PID Control

            moveCar(base_torque, action) # Pass the actions into moveCar for controlling the car.

            k = cv2.waitKey(1)  # Use this while using trackbars, otherwise they won't work in real time.
            time.sleep(1. / 240.)

            keycode = p.getKeyboardEvents()  # This will keep tracking if ENTER key is pressed again.

            if keycode.get(p.B3G_RETURN) == 1:  # We end the current simulation and start a new one again if ENTER key is pressed
                print("Episode finished")  # This is a way to re-run the simulation without re-executing the code
                p.resetSimulation()  # Resetting the simulation
                break  # Breaking out of the inner while loop
