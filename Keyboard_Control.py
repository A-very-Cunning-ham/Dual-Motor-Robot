# sudo python3 test.py
import time

import Robot

import keyboard

LEFT_TRIM   = 0
RIGHT_TRIM  = 0

robot = Robot.Robot(left_trim=LEFT_TRIM, right_trim=RIGHT_TRIM)

try:
    while True:
        
        if keyboard.is_pressed("up"):
            print("Driving forwards")
            robot.forward(150)
        elif keyboard.is_pressed("right"):
            print("Driving right")
            robot.right(150)
        elif keyboard.is_pressed("left"):
            print("Driving left")
            robot.left(150)
        elif keyboard.is_pressed("down"):
            print("Driving back")
            robot.backward(150)
        elif keyboard.is_pressed("esc"):
            print('Exiting...')
            quit()
        else:
            robot.stop()
            
        time.sleep(0.01)
        
except KeyboardInterrupt:
    print('Interrupted')
    robot.stop()
