#!/usr/bin/env python3 

# Script Name:                          opschallenge6.py
# Author name:                          Tianna Farrow
# Date of latest revision:              01/16/2024
# Purpose:                              A script that encrypts a single file
# Execution:                            python3 opschallenge6.py
# Additional Resources:                 https://pypi.org/project/cryptography/; https://www.freecodecamp.org/news/how-to-check-if-a-file-exists-in-python/; https://www.geeksforgeeks.org/fernet-symmetric-encryption-using-cryptography-module-in-python/; https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-06/challenges/DEMO.md; https://thepythoncode.com/article/encrypt-decrypt-files-symmetric-python; https://cryptography.io/en/latest/; https://cryptography.io/en/latest/fernet/; https://www.programiz.com/python-programming/input-output-import 

# Import cryptography libra and file handle 
from cryptography.fernet import Fernet 
import os

KEY_FILE = "secret.key"

# generate a random key if not exists
def generate_key():
    if not os.path.isfile(KEY_FILE):
        key = Fernet.generate_key()
        save_key(key)
    else:
        key = load_key()
    return key

# save the key to a file
def save_key(key, filename=KEY_FILE):
    with open(filename, "wb") as key_file:
        key_file.write(key)

# load the key from a file
def load_key(filename=KEY_FILE):
    return open(filename, "rb").read()

# encrypt a file using the provided key
def encrypt_file(filename, key):
    cipher = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = cipher.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)

# decrypt a file using the provided key
def decrypt_file(filename, key):
    cipher = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = cipher.decrypt(encrypted_data)
    with open(filename, "wb") as file:
        file.write(decrypted_data)

# encrypt a string using the provided key
def encrypt_string(text, key):
    cipher = Fernet(key)
    encrypted_text = cipher.encrypt(text.encode())
    print("Encrypted String:", encrypted_text.decode())

# decrypt a string using the provided key
def decrypt_string(text, key):
    cipher = Fernet(key)
    decrypted_text = cipher.decrypt(text.encode())
    print("Decrypted String:", decrypted_text.decode())

def main():
    # Generate a random key or load existing key
    key = generate_key()

    # Display user options
    print("Select mode:")
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    print("3. Encrypt a message")
    print("4. Decrypt a message")

    # Get user input for mode selection
    mode = int(input("Enter mode (1/2/3/4): "))

    # encryption/decryption
    if mode in [1, 2]:
        # Get the file path from the user
        filepath = input("Enter the file path: ")

        # Check if the file exists
        if not os.path.isfile(filepath):
            print("File not found. Exiting.")
            return

        # file encryption or decryption based on user input
        if mode == 1:
            encrypt_file(filepath, key)
            print("File encrypted successfully.")
        elif mode == 2:
            decrypt_file(filepath, key)
            print("File decrypted successfully.")
    # string encryption/decryption
    elif mode in [3, 4]:
        # Get the message from the user
        message = input("Enter the message: ")

        # Perform string encryption or decryption based on user input
        if mode == 3:
            encrypt_string(message, key)
        elif mode == 4:
            decrypt_string(message, key)

# Entry point of the script
if __name__ == "__main__":
    # Call the main start the program
    main()