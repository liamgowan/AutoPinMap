#==============================================================================
# mouseNow.py
# Purpose: Program to print screen location of cursor, and corresponding
#          colour.
#
# Created by Liam Gowan, November 2018.
#==============================================================================
import pyautogui
import time

#Until interrupted, print location of cursor and colour once a second 
try:
    while True:
        x,y = pyautogui.position()
        positionStr = "\nX: " + str(x).rjust(4)+"Y: " + str(y).rjust(4)
        print(positionStr)
        print(pyautogui.pixel(x,y))
        time.sleep(1)
except KeyboardInterrupt:
    print("Done.")


