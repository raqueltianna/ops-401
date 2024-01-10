#!/usr/bin/env python3 

# Script Name:                          uptimesensorpt1.py
# Author name:                          Tianna Farrow
# Date of latest revision:              01/09/2024
# Purpose:                              Transmit a single ICMP (ping) packet to a specific IP every two seconds, Evaluate the response as either success or failure, Assign success or failure to a status variable, For every ICMP transmission attempted, print the status variable along with a comprehensive timestamp and destination IP tested.. 
# Execution:                            python3 uptimesensorpt1.py
# Additional Resources:                 https://docs.python.org/3/library/subprocess.html; https://stackoverflow.com/questions/2953462/pinging-servers-in-python; https://stackoverflow.com/questions/35750041/check-if-ping-was-successful-using-subprocess-in-python; https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes; https://docs.python.org/3/reference/expressions.html#conditional-expressions; https://docs.python.org/3/reference/lexical_analysis.html#f-strings


import subprocess
import time
from datetime import datetime   

def ping_host(ip):
    try:
        subprocess.check_output(['ping', '-c', '1', ip], stderr=subprocess.STDOUT, text=True)
        return True
    except subprocess.CalledProcessError:
        return False
    
def main():
    ip_address = input("Enter the IP address: ")

    while True:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        status = "Network Active" if ping_host(ip_address) else "Network Inactive"
        print(f"{timestamp} {status} to {ip_address}")
        time.sleep(2)

if __name__ == "__main__":
    main()
