#!/usr/bin/python3

# Script Name:                      opschallenge43.py
# Author Name:                      Tianna Farrow
# Date of Latest Revision:          03/06/24
# Purpose:                          use Python to develop a custom Nmap scanner that can later be combined with other Python scripts to create a pentester toolkit.
# Execution                         python3 opschallenge43.py 
# Additional Resources:             https://docs.python.org/3/library/socket.html; https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-44/challenges/DEMO.md

#!/usr/bin/python3

import socket

sockmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
timeout = 10  # TODO: Set a timeout value here.
sockmod.settimeout(timeout)

hostip = input("Enter the host IP: ")  # TODO: Collect a host IP from the user.
portno = int(input("Enter the port number: "))  # TODO: Collect a port number from the user, then convert it to an integer data type.

def portScanner(portno):
    if sockmod.connect_ex((hostip, portno)) == 0:  # TODO: Replace "FUNCTION" with the appropriate socket function call as found in the socket docs
        print("Port open")
    else:
        print("Port closed")

portScanner(portno)