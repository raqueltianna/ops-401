#!/usr/bin/env python3 

# Script Name:                      opschallenge12.py
# Author Name:                      Tianna Farrow
# Date of Latest Revision:          01/25/2024
# Purpose:                          Continue devlopment of my own network scanning tool.  
# Execution                         python3 opschallenge12.py 
# Additional Resources:             https://github.com/raqueltianna/ops-401/blob/main/opschallenge11.py; https://github.com/raqueltianna/ops-401/blob/main/opschallenge12.py; https://wiki.sans.blue/Tools/pdfs/ScapyCheatSheet_v0.2.pdf; 
# Notes:                            This is a continuation of a previous code I created. It is linked in the resources above! The resources in the previous code also applies to this one. 

# Import necessary modules from scapy library
from scapy.all import IP, ICMP, TCP, sr1, RandShort
from ipaddress import ip_network

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

# Define a function to perform an ICMP Ping Sweep on the target network
def icmp_ping_sweep(host):
    # Send an ICMP Echo Request to the host
    response = sr1(IP(dst=host) / ICMP(), timeout=1, verbose=0)

    # Check if a response was received
    if response is not None:
        # Check ICMP type and code to determine host status
        if response[ICMP].type == 0 and response[ICMP].code == 0:
            # If type 0 and code 0 is received, the host is responding
            print(f"Host {host} is responding.")
            # Call the port scan function
            port_scan(host)
        elif response[ICMP].type == 3 and response[ICMP].code in [1, 2, 3, 9, 10, 13]:
            # If type 3 and code in [1, 2, 3, 9, 10, 13], the host is actively blocking ICMP traffic
            print(f"Host {host} is actively blocking ICMP traffic.")
        else:
            # Otherwise, inform the user that the host is down or unresponsive
            print(f"Host {host} is down or unresponsive.")
    else:
        # If no response is received, the host is down or unresponsive
        print(f"Host {host} is down or unresponsive.")

# Define a function to perform port scanning on the target host
def port_scan(host):
    # Prompt user for port range
    start_port = int(input("Enter the starting port of the range: "))
    end_port = int(input("Enter the ending port of the range: "))

    # Iterate over the specified port range and call scan_port function
    for port in range(start_port, end_port + 1):
        scan_port(host, port)

# Entry point of the script
if __name__ == "__main__":
    # Prompt user for target host IP address
    host = input("Enter the target IP address: ")

    # Call the icmp_ping_sweep function with the specified host
    icmp_ping_sweep(host)
