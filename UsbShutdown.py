__author__ = 'kattstof'
#!python3
"""UsbShutdown: an anti-forensic tool that shuts down your windows based computer when an usb device is attached
If you run linux try https://github.com/hephaest0s/usbkill"""
import time, os
print('Please enter usb letter to search for*default F:*')
usb_letter = input() #Asks user for letter of next usb letter to be assigne
if usb_letter == '': #if no letter is entered run with default letter F
    while True:
        if os.system("cd " +"F" +":") == 0: # cd's into letter directory
            os.system('shutdown /p /f') # if cd is successful, shut down
        else:
            print('Searching for unkown usb devices...') #if cd is unsuccesful , print message and retry
            time.sleep(5) #retry every 5 secons
else:
    while True: # if user entered letter use user input
        if os.system("cd " +"usb_letter" +":") == 0: # cd's into user entered letter directory
            os.system('shutdown /p /f') # if cd successful, shutdown
        else:
            print('Searching for unknown usb devices...') # if cd is unsuccesful print message and retry
            time.sleep(5) #retry every 5 seconds
