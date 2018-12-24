#==============================================================================
# AutoPinMap.py
# Purpose: Program to automatically read in a list of Twitter links, navigate
#          the web to each link, extract data required in a GoogleDoc, and then
#          insert data into the GoogleDoc. End goal is to populate a map with
#          coordinates and other information related to Tweet.
#
# Warning: Program must be configured properly and used as described in the
#          README.txt file. Not doing so can cause undesirable effects, as
#          program will move the mouse and input key strokes automatically.
#          Ensure that coordinates and colours have been configured properly.
#          mouseNow.py can be used to assist in editing the config.txt file.
#
# Created by Liam Gowan, November 2018.
#==============================================================================

pyautogui and pyperclip modules are required to run program. "allLinks.txt" and "config.txt" files must be filled in correctly.

"allLinks.txt" must contain link to Google Forms on line 1, and Twitter links on all other files.

"config.txt" must be filled with proper screen locations and colours. To make this easier, use mouseNow.py, which displays screen location and corresponding RGB values.