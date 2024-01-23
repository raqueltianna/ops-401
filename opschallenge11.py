#!/usr/bin/env python3 

# Script Name:                      opschallenge11.py
# Author Name:                      Tianna Farrow
# Date of Latest Revision:          01/22/2024
# Purpose:                          Beginning development of your own network scanning tool utilizing Python library Scapy. 
# Execution                         python3 opschallenge11.py 
# Additional Resources:             https://scapy.readthedocs.io/en/latest/index.html; https://scapy.readthedocs.io/en/latest/introduction.html#; https://scapy.readthedocs.io/en/latest/extending.html; https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-11/challenges/demo.py;https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-11/challenges/DEMO.md 
# Note:                             I have to go back in and add the ports and IP addresses. I was a little confused and just made a code based off of the resources but I need to go back and watch the class video where Roger demo'd.
# Import necessary modules from scapy library
from scapy.all import IP, TCP, sr1, Ether, RandShort

# Define a function to scan a specific port on the target host
def scan_port(host, port):
    # Send a SYN packet to the specified port and wait for the response
    response = sr1(IP(dst=host) / TCP(sport=RandShort(), dport=port, flags='S'), timeout=1, verbose=0)

    # Check if a response was received
    if response is not None:
        # Check if the response has a TCP layer
        if response.haslayer(TCP):
            # Check TCP flags to determine port status
            if response[TCP].flags == 0x12:
                # If flag 0x12 is received, the port is open
                print(f"Port {port} is open. Sending RST packet to close connection.")
                # Send a RST packet to gracefully close the open connection
                sr1(IP(dst=host) / TCP(sport=RandShort(), dport=port, flags='R'), timeout=1, verbose=0)
            elif response[TCP].flags == 0x14:
                # If flag 0x14 is received, the port is closed
                print(f"Port {port} is closed.")
        else:
            # If no TCP layer is present, the port is filtered and silently dropped
            print(f"Port {port} is filtered and silently dropped.")
    else:
        # If no response is received, the port did not respond
        print(f"Port {port} did not respond.")

# Define a function to perform a TCP port range scan on the target host
def tcp_port_range_scanner(host, start_port, end_port):
    # Iterate over the specified port range
    for port in range(start_port, end_port + 1):
        # Call the scan_port function for each port in the range
        scan_port(host, port)

# Entry point of the script
if __name__ == "__main__":
    # Specify the target host IP address
    host = 'ip'
    # Specify the starting port of the range
    start_port = 1
    # Specify the ending port of the range
    end_port = 100

    # Call the tcp_port_range_scanner function with the specified parameters
    tcp_port_range_scanner(host, start_port, end_port)