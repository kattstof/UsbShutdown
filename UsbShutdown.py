__author__ = 'kattstof'
#!python3
"""UsbShutdown: an anti-forensic tool that shuts down your windows based computer when an usb device is attached
If you run linux try https://github.com/hephaest0s/usbkill"""
import time
import os

from colorama import Fore, init


init(convert=True)
print(Fore.MAGENTA+"           _           _           _      _")
print(Fore.MAGENTA+"          | |         | |         | |    | |")
print(Fore.MAGENTA+" _   _ ___| |__    ___| |__  _   _| |_ __| | _____      ___ __")
print(Fore.MAGENTA+"| | | / __| '_ \  / __| '_ \| | | | __/ _` |/ _ \ \ /\ / / '_ \"")
print(Fore.MAGENTA+"| |_| \__ \ |_) | \__ \ | | | |_| | || (_| | (_) \ V  V /| | | |")
print(Fore.MAGENTA+" \__,_|___/_.__/  |___/_| |_|\__,_|\__\__,_|\___/ \_/\_/ |_| |_|")
print(Fore.CYAN+"1) Monitor For USB insertion")
print(Fore.CYAN+"2) Monitor For USB Detachment")
main_choice = input("Enter your choice:")
if main_choice == '1': # if main menu option is 1
    print('Please enter usb letter to search for*default F*:*') #ask for letter
    usb_letter = input() #Asks user for letter of next usb letter to be assigned
    if usb_letter == '': #if no letter is entered run with default letter F
        while True: #run in a loop
            if os.system("cd " +"F" +":") == 0: # cd's into letter directory
                print('Searching for unknown usb devices')
                os.system('shutdown /p /f') # if cd is successful, shut down
            else:
                print(Fore.GREEN+'Searching for unknown usb devices...') #if cd is unsuccesful , print message and retry
                time.sleep(5) #retry every 5 secons
    else:
        while True: # if user entered letter use user input1
            if os.system("cd " +"usb_letter" +":") == 0: # cd's into user entered letter directory
                os.system('shutdown /p /f') # if cd successful, shutdown
            else:
                print('Searching for unknown usb devices...') # if cd is unsuccesful print message and retry
                time.sleep(1) #retry every 5 seconds
if main_choice == '2': # if main menu option is 2
    print('Enter USB letter to monitor*default F*:') #ask for letter
    usb_letter = input() # ask for user input
    if usb_letter == '': # if input is empty assume letter F
        while True: #run in a loop
            if os.system("cd " +"F" +":") == 0: # cd's into letter directory
                print('everything looks good') # if cd succesful print mesage
            else:# if cd unseccessful
                os.system('shutdown /p /f') #shutdown
    else: # if user input letter use user input
        if os.system("cd " +"usb_letter" +":") == 0: # cd into letter directory
            print('everything looks good') # if cd successful print message
            time.sleep(3)
        else: #if cd unseccessful
            os.system('shutdown /p /f') # shutdown


