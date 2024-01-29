#!/usr/bin/env python3 

# Script Name:                          opschallenge16.py
# Author name:                          Tianna Farrow
# Date of latest revision:              01/29/2024
# Purpose:                              begin to develop a custom tool that performs brute force attacks to better understand the types of automation employed by adversaries. 
# Execution:                            python3 opschallenge16.py
# Additional Resources:                 https://www.geeksforgeeks.org/iterate-over-a-set-in-python/; https://github.com/raqueltianna/ops-401/blob/main/warmup.py
# Notes:                                Using the above the resource, I created this code based off of a warm up code during lecture which is also linked in the resources. 

import time

# Prompt user to select mode 
def offensive_mode():
    # ask user for path of the word file 
    word_list_path = input("Enter the path to the word list file: ")
    # ask user for how long of a delay 
    delay = float(input("Enter the delay between words: "))
    
    # open the  word file and iterate through each line
    with open(word_list_path, 'r') as file:
        for line in file:
            word = line.strip()
            time.sleep(delay)
            # print current word 
            print(f"Current: {word}")

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