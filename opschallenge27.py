#!/usr/bin/env python3 

# Script Name:                      opschallenge26.py 
# Author Name:                      Tianna Farrow
# Date of Latest Revision:          02/13/24
# Purpose:                          add logging capabilities and file handler to a previous script 
# Execution                         python3 opschallenge26.py 
# Additional Resources:             https://github.com/raqueltianna/ops-401/blob/main/opschallenge12.py; https://github.com/Data-Dazzlers/Scripts/blob/main/sshbruteforce.py; https://github.com/raqueltianna/ops-401/blob/main/opschallenege26.py; https://www.blog.pythonlibrary.org/2014/02/11/python-how-to-create-rotating-logs/


from scapy.all import IP, ICMP, sr1, RandShort, TCP
from ipaddress import ip_network
import logging
from logging.handlers import RotatingFileHandler

# Configure logging with log rotation based on size
log_file = 'scan_log.log'
max_log_size = 1024 * 1024  # 1 MB
backup_count = 3  # Number of backup log files
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler = RotatingFileHandler(log_file, maxBytes=max_log_size, backupCount=backup_count)
handler.setFormatter(formatter)
logger = logging.getLogger()
logger.addHandler(handler)
logger.setLevel(logging.INFO)

# Define a function to scan a specific port on the target host
def scan_port(host, port):
    try:
        # Send a SYN packet to the specified port and wait for the response
        response = sr1(IP(dst=host) / TCP(sport=RandShort(), dport=port, flags='S'), timeout=1, verbose=0)

        # Check if a response was received
        if response is not None:
            # Check if the response has a TCP layer
            if response.haslayer(TCP):
                # Check TCP flags to determine port status
                if response[TCP].flags == 0x12:
                    # If flag 0x12 is received, the port is open
                    logger.info(f"Port {port} is open. Sending RST packet to close connection.")
                    # Send a RST packet to gracefully close the open connection
                    sr1(IP(dst=host) / TCP(sport=RandShort(), dport=port, flags='R'), timeout=1, verbose=0)
                elif response[TCP].flags == 0x14:
                    # If flag 0x14 is received, the port is closed
                    logger.info(f"Port {port} is closed.")
            else:
                # If no TCP layer is present, the port is filtered and silently dropped
                logger.info(f"Port {port} is filtered and silently dropped.")
        else:
            # If no response is received, the port did not respond
            logger.info(f"Port {port} did not respond.")
    except Exception as e:
        # Log any exceptions that occur
        logger.error(f"Error occurred while scanning port {port}: {str(e)}")

# Define a function to perform an ICMP Ping Sweep on the target network
def icmp_ping_sweep(network):
    try:
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
                    logger.info(f"Host {address} is responding.")
                    online_hosts += 1
                elif response[ICMP].type == 3 and response[ICMP].code in [1, 2, 3, 9, 10, 13]:
                    # If type 3 and code in [1, 2, 3, 9, 10, 13], the host is actively blocking ICMP traffic
                    logger.info(f"Host {address} is actively blocking ICMP traffic.")
                else:
                    # Otherwise, inform the user that the host is down or unresponsive
                    logger.info(f"Host {address} is down or unresponsive.")
            else:
                # If no response is received, the host is down or unresponsive
                logger.info(f"Host {address} is down or unresponsive.")

        # Inform the user about the number of online hosts
        logger.info(f"\nTotal online hosts: {online_hosts}")
    except Exception as e:
        # Log any exceptions that occur
        logger.error(f"Error occurred during ICMP Ping Sweep: {str(e)}")

# Entry point of the script
if __name__ == "__main__":
    try:
        # Prompt user for choice between TCP Port Range Scanner and ICMP Ping Sweep
        choice = input("Choose mode: 1 for TCP Port Range Scanner, 2 for ICMP Ping Sweep: ")

        if choice == '1':
            # Prompt user for target host IP address
            host = input("Enter the target IP address: ")

            # Prompt user for port range
            start_port = int(input("Enter the starting port of the range: "))
            end_port = int(input("Enter the ending port of the range: "))

            # Call the tcp_port_range_scanner function with the specified parameters
            for port in range(start_port, end_port + 1):
                scan_port(host, port)
        elif choice == '2':
            # Prompt user for network address with CIDR block
            network_address = input("Enter the network address with CIDR block (e.g., '10.10.0.0/24'): ")

            # Call the icmp_ping_sweep function with the specified network address
            icmp_ping_sweep(ip_network(network_address, strict=False))
        else:
            print("Invalid choice. Please choose 1 or 2.")
    except KeyboardInterrupt:
        logger.info("Keyboard Interrupt detected. Exiting...")
    except Exception as e:
        # Log any unexpected exceptions that occur
        logger.error(f"Unexpected error occurred: {str(e)}")