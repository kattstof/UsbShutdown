__author__ = 'kattstof'
#!python3
"""UsbShutdown: an anti-forensic tool that shuts down your windows based computer when an usb device is attached
If you run linux try https://github.com/hephaest0s/usbkill"""
import time, os, smtplib
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
    usb_letter = input('Please enter usb letter to search for*default F*:*') #ask for letter
    email = input('Do you want to turn on email notification Y/N?') # ask for email notification
    if usb_letter == '': # if user didnt supply letter assume F
        if email == 'y': # if user wants email notification
            def email(): # define email 'y' function
                add = input('enter gmail address') # ask for email
                password = input('enter gmail pass') # ask for password
                while True: # run in loop
                    if os.system("cd " +"F" +":") == 0: # if cd successful
                        server = smtplib.SMTP('smtp.gmail.com', 587) #set gmail
                        server.ehlo() #set gmail
                        server.starttls() #set gmail
                        server.ehlo() # set gmail
                        server.login(add, password) # login to gmail
                        msg = "UsbShutdown Critical Alert: unknown activity caused a shutdown to occur" #email this message
                        server.sendmail(add, add, msg) # send email to self
                        os.system('shutdown /p /f') #shutdown
                else: # if cd unseccesful
                    print('Searching') # print message
                    time.sleep(3) # retry every 3 seconds
            email()
        elif email == 'n': # if user doesnt want email notifications
            def noemail(): #define email 'n' function
                while True: # run in loop
                    if os.system("cd " +"F" +":") == '0': #cd into f directory
                        os.system('shutdown /p /f') # if cd successful shut down
                    else: # if cd unsuccessful
                        print('searching') #print messages
                        time.sleep(3) #retry every 3 seconds
            noemail()
    else: # if user input letter use user input
        if email == 'y':
            NegEmail()
elif main_choice == '2': # if main menu option is 2
    usb_letter = input('Enter letter to monitor:') # ask for letter to monitor
    if usb_letter == '': # if input is empty assume letter F
        email = ("Do you want to turn on email notifications?Y/N: ") # ask for email notifications
        if email == 'y': # if user wants email notifications
            email()
        elif email == 'n': #if user doesnt want email notifications
            noemail()

    else: # if user supplied letter use supplied letter
        email = input ('Do you want to turn on email notifications?Y/N:') # ask for email notifications
        if email == 'y': # if user wants email notifications
            email()
        elif email == 'n': # if user doesnt want email notifications
           noemail()
