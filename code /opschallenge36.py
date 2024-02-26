#!/usr/bin/env python3 

# Script Name:                      opschallenge36.py
# Author Name:                      Tianna Farrow
# Date of Latest Revision:          02/26/24
# Purpose:                          develop a Python script that utilizes multiple banner grabbing approaches against a single target
# Execution                         python3 opschallenge36.py 
# Additional Resources:             https://www.hackingarticles.in/multiple-ways-to-banner-grabbing/; https://www.geeksforgeeks.org/what-is-banner-grabbing/; https://securitytrails.com/blog/banner-grabbing; https://www.yeahhub.com/use-netcat-listening-banner-grabbing-transferring-files/;  https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-36/challenges/DEMO.md; 



import subprocess

def netcat_banner_grab(target, port):
    try:
        result = subprocess.check_output(['nc', '-v', '-n', '-z', '-w', '1', target, str(port)], stderr=subprocess.STDOUT)
        print(result.decode())
    except subprocess.CalledProcessError as e:
        print(e.output.decode())

def telnet_banner_grab(target, port):
    try:
        result = subprocess.check_output(['timeout', '1', 'telnet', target, str(port)], stderr=subprocess.STDOUT)
        print(result.decode())
    except subprocess.CalledProcessError as e:
        print(e.output.decode())

def nmap_banner_grab(target):
    try:
        result = subprocess.check_output(['nmap', '-sV', target], stderr=subprocess.STDOUT)
        print(result.decode())
    except subprocess.CalledProcessError as e:
        print(e.output.decode())

def main():
    target = input("Enter URL or IP address: ")
    port = int(input("Enter port number: "))

    print("\nPerforming banner grabbing using netcat:")
    netcat_banner_grab(target, port)

    print("\nPerforming banner grabbing using telnet:")
    telnet_banner_grab(target, port)

    print("\nPerforming banner grabbing using Nmap:")
    nmap_banner_grab(target)

if __name__ == "__main__":
    main()