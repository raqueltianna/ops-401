#!/usr/bin/env python3 

# Script Name:                      opschallenge12.py
# Author Name:                      Tianna Farrow
# Date of Latest Revision:          01/23/2024
# Purpose:                          Continue devlopment of my own network scanning tool.  
# Execution                         python3 opschallenge12.py 
# Additional Resources:             https://github.com/raqueltianna/ops-401/blob/main/opschallenge11.py; https://sedo.com/search/details/?partnerid=324561&language=us&domain=infinityquest.com&origin=sales_lander_1&utm_medium=Parking&utm_campaign=offerpage; https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-12/challenges/DEMO.md; https://docs.python.org/3/library/ipaddress.html;  
# Notes:                            This is a continuation of a previous code I created. It is linked in the resources above! The resources in the previous code also applies to this one. 

# Import necessary modules from scapy library
from scapy.all import IP, ICMP, sr1, RandShort
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
def icmp_ping_sweep(network):
    # Create a list of all addresses in the given network
    addresses = [str(ip) for ip in ip_network(network).hosts()]

    # Count how many hosts are online
    online_hosts = 0

    # Iterate over each address in the network
    for address in addresses:
        # Skip network address and broadcast address
        if address == network.network_address or address == network.broadcast_address:
            continue

        # Send an ICMP Echo Request to the address
        response = sr1(IP(dst=address) / ICMP(), timeout=1, verbose=0)

        # Check if a response was received
        if response is not None:
            # Check ICMP type and code to determine host status
            if response[ICMP].type == 0 and response[ICMP].code == 0:
                # If type 0 and code 0 is received, the host is responding
                print(f"Host {address} is responding.")
                online_hosts += 1
            elif response[ICMP].type == 3 and response[ICMP].code in [1, 2, 3, 9, 10, 13]:
                # If type 3 and code in [1, 2, 3, 9, 10, 13], the host is actively blocking ICMP traffic
                print(f"Host {address} is actively blocking ICMP traffic.")
            else:
                # Otherwise, inform the user that the host is down or unresponsive
                print(f"Host {address} is down or unresponsive.")
        else:
            # If no response is received, the host is down or unresponsive
            print(f"Host {address} is down or unresponsive.")

    # Inform the user about the number of online hosts
    print(f"\nTotal online hosts: {online_hosts}")

# Entry point of the script
if __name__ == "__main__":
    # Prompt user for choice between TCP Port Range Scanner and ICMP Ping Sweep
    choice = input("Choose mode: 1 for TCP Port Range Scanner, 2 for ICMP Ping Sweep: ")

    if choice == '1':
        # Prompt user for target host IP address
        host = input("Enter the target IP address: ")

        # Prompt user for port range
        start_port = int(input("Enter the starting port of the range: "))
        end_port = int(input("Enter the ending port of the range: "))

        # Call the tcp_port_range_scanner function with the specified parameters
        tcp_port_range_scanner(host, start_port, end_port)
    elif choice == '2':
        # Prompt user for network address with CIDR block
        network_address = input("Enter the network address with CIDR block (e.g., '10.10.0.0/24'): ")

        # Call the icmp_ping_sweep function with the specified network address
        icmp_ping_sweep(ip_network(network_address, strict=False))
    else:
        print("Invalid choice. Please choose 1 or 2.")


