# L3_drivingPatterns.py
# Team Number: group 1
# Hardware TM: Chase Elliott
# Software TM: Cooper Elliott
# Date: 3/3/2021

# Code purpose: This program creates a path that the robot moves in. 
# The path created is in a S shape that is made up of nine movements

# indicate d1 and d2 distances: 

# Import Internal Programs
import L2_speed_control as sc
import L2_inverse_kinematics as inv

# Import External programs
import numpy as np
import time

def task2():
	myVelocities = np.array([1, 0]) #input your first pair
	myPhiDots = inv.convert(myVelocities)
	sc.driveOpenLoop(myPhiDots)
	time.sleep(2) # input your duration (s)
	print("Move forward D1")
	
	myVelocities = np.array([0, 1]) #input your 2nd pair
	myPhiDots = inv.convert(myVelocities)
	sc.driveOpenLoop(myPhiDots)
	time.sleep(0.789) # input your duration (s)
	print("trun left 90 degrees")
	
	myVelocities = np.array([1, 0]) #input your 3rd pair
	myPhiDots = inv.convert(myVelocities)
	sc.driveOpenLoop(myPhiDots)
	time.sleep(5) # input your duration (s)
	print("Move forward D2")
	
	myVelocities = np.array([0, 1]) #input your 4th pair
	myPhiDots = inv.convert(myVelocities)
	sc.driveOpenLoop(myPhiDots)
	time.sleep(0.789) # input your duration (s)
	print("trun left 90 degrees")
	
	myVelocities = np.array([1, 0]) #input your 5th pair
	myPhiDots = inv.convert(myVelocities)
	sc.driveOpenLoop(myPhiDots)
	time.sleep(2) # input your duration (s)
	print("Move forward D1")
	
	myVelocities = np.array([0, -1]) #input your 6th pair
	myPhiDots = inv.convert(myVelocities)
	sc.driveOpenLoop(myPhiDots)
	time.sleep(0.789) # input your duration (s)
	print("trun right 90 degrees")
	
	myVelocities = np.array([1, 0]) #input your 7th pair
	myPhiDots = inv.convert(myVelocities)
	sc.driveOpenLoop(myPhiDots)
	time.sleep(5) # input your duration (s)
	print("Move forward D2")
	
	myVelocities = np.array([0, -1]) #input your 8th pair
	myPhiDots = inv.convert(myVelocities)
	sc.driveOpenLoop(myPhiDots)
	time.sleep(0.789) # input your duration (s)
	print("trun right 90 degrees")
	
	myVelocities = np.array([1, 0]) #input your 9th pair
	myPhiDots = inv.convert(myVelocities)
	sc.driveOpenLoop(myPhiDots)
	time.sleep(2) # input your duration (s)
	print("Move forward D1")
	
while 1:
    task2()
    time.sleep(0.2)
