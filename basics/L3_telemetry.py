# L3_telemetry.py

# Group 1
# Members:
#   Chase Elliott
#   Cooper Elliott

# Date: 02-28-2021

# This program grabs data from the onboard Magnometers, converts the data into 
# useful degree values, then determines the cardinal direction of the robot
# This code also produces two text files that contain the degree values and 
# cardinal direction of the robot. 


# This program grabs data from the onboard sensors and log data in files
# for NodeRed access and integrate into a custom "flow".
# Access nodered at 192.168.8.1:1880 (by default, it's running on the Blue)

# Import Internal Programs
import L1_mpu as mpu
import L2_log as log
import L1_adc as adc
import L1_bmp as bmp
import L2_heading as heading

# Import External programs
import numpy as np
import time

# Run the main loop
while True:
    # accel = mpu.getAccel()                          # call the function from within L1_mpu.py
    # (xAccel) = accel[0]                             # x axis is stored in the first element
    # (yAccel) = accel[1]                             # y axis is stored in the second element
    # (zAccel) = accel[2]
    # (Volt) = adc.getDcJack()
    # (TC) = bmp.temp()
    # (Press) = bmp.pressure()
    # (alt) = bmp.altitude()
    

    (axes) = heading.getXY()                        #gets values from the axes and determines 
    (axesScaled) = heading.scale(axes)              #the heading degree of the scuttle
    (h) = heading.getHeading(axesScaled)
    (headingDegrees) = round(h*180/np.pi, 2)
    
    if -10 <= headingDegrees:                        #Cardnal direction north
        if headingDegrees <= 10:
            (Cardnal) = "North"
            
    if headingDegrees >= 170:                        #Cardnal direction south
        (Cardnal) = "South"
    if headingDegrees <= -170:
        (Cardnal) = "South"
            
    if -100 <= headingDegrees:                        #Cardnal direction East
        if headingDegrees <= -80:
            (Cardnal) = "East"
            
    if  80 <= headingDegrees:                        #Cardnal direction West
        if headingDegrees <= 100:
            (Cardnal) = "West"
    
    if 10 <= headingDegrees:                        #Cardnal direction northwest
        if headingDegrees < 80:
            (Cardnal) = "Northwest"
    
    if -80 < headingDegrees:                        #Cardnal direction northeast
        if headingDegrees < -10:
            (Cardnal) = "Northeast"
            
    if 100 < headingDegrees:                        #Cardnal direction southwest
        if headingDegrees < 170:
            (Cardnal) = "Southwest"
    
    if -170 < headingDegrees:                        #Cardnal direction southeast
        if headingDegrees < -100:
            (Cardnal) = "Southeast"
    
   
    
    
    # print("x axis:", xAccel, "y axis:", yAccel,"z axis:", zAccel)
    # print("Barrel Voltage:",Volt, "Temperature:", TC, "Pressure:", Press, "Altitude:", alt)     # print the two values
    print("Heading Degree:",headingDegrees, "Direction:", str(Cardnal))
    
    #axes = np.array([xAccel, yAccel)               # store just 2 axes in an array
    #log.NodeRed2(axes)                              # send the data to txt files for NodeRed to access.
    # log.uniqueFile(xAccel,"xAccel.txt")           # another way to log data for NodeRed access
    # log.uniqueFile(yAccel,"yAccel.txt")
    # log.uniqueFile(zAccel,"zAccel.txt") 
    # log.uniqueFile(Volt,"BarrelVolt.txt")
    # log.uniqueFile(TC,"Temp.txt")
    # log.uniqueFile(Press,"Pressure.txt")
    # log.uniqueFile(alt,"Altitude.txt")
    log.uniqueFile(headingDegrees,"HeadingDeg.txt")
    log.stringTmpFile(Cardnal,"Direction.txt")
    # log.tmpFile(xAccel,"xAccel.txt")              # another way to lof data for NodeRed access
    # log.tmpFile(yAccel,"yAccel.txt")
    time.sleep(0.2)
