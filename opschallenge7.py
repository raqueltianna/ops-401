#!/usr/bin/env python3 

# Script Name:                          opschallenge7.py
# Author name:                          Tianna Farrow
# Date of latest revision:              01/17/2024
# Purpose:                              A script that encrypts a single file; recruisvely encrypt and decrypt a file.
# Execution:                            python3 opschallenge7.py
# Additional Resources:                 https://github.com/raqueltianna/ops-401/blob/main/opschallenge6.py; https://www.pythoncentral.io/recursive-file-and-directory-manipulation-in-python-part-1/; https://appdividend.com/2020/01/20/python-list-of-files-in-directory-and-subdirectories/; https://pypi.org/project/cryptography/; https://www.freecodecamp.org/news/how-to-check-if-a-file-exists-in-python/; https://www.geeksforgeeks.org/fernet-symmetric-encryption-using-cryptography-module-in-python/; https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-06/challenges/DEMO.md; https://thepythoncode.com/article/encrypt-decrypt-files-symmetric-python; https://cryptography.io/en/latest/; https://cryptography.io/en/latest/fernet/; https://www.programiz.com/python-programming/input-output-import; 
# Note                                  this script is a continuation of a script that I made yesterday. It is listed in the resources above. 




from cryptography.fernet import Fernet
import os

KEY_FILE = "secret.key"

# Generate a random key if not exists
def generate_key():
    if not os.path.isfile(KEY_FILE):
        key = Fernet.generate_key()
        save_key(key)
    else:
        key = load_key()
    return key

# Save the key to a file
def save_key(key, filename=KEY_FILE):
    with open(filename, "wb") as key_file:
        key_file.write(key)

# Load the key from a file
def load_key(filename=KEY_FILE):
    return open(filename, "rb").read()

# Encrypt a file using the provided key
def encrypt_file(filename, key):
    cipher = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = cipher.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)

# Decrypt a file using the provided key
def decrypt_file(filename, key):
    cipher = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = cipher.decrypt(encrypted_data)
    with open(filename, "wb") as file:
        file.write(decrypted_data)

# Encrypt a string using the provided key
def encrypt_string(text, key):
    cipher = Fernet(key)
    encrypted_text = cipher.encrypt(text.encode())
    print("Encrypted String:", encrypted_text.decode())

# Decrypt a string using the provided key
def decrypt_string(text, key):
    cipher = Fernet(key)
    decrypted_text = cipher.decrypt(text.encode())
    print("Decrypted String:", decrypted_text.decode())

# Recursively encrypt a single folder and all its contents
def encrypt_folder(folder_path, key):
    for foldername, subfolders, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            encrypt_file(file_path, key)

# Recursively decrypt a single folder that was encrypted by this tool
def decrypt_folder(folder_path, key):
    for foldername, subfolders, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            decrypt_file(file_path, key)

def main():
    # Generate a random key or load an existing key
    key = generate_key()

    # Display user options
    print("Select mode:")
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    print("3. Encrypt a message")
    print("4. Decrypt a message")
    print("5. Recursively encrypt a folder")
    print("6. Recursively decrypt a folder")

    # Get user input for mode selection
    mode = int(input("Enter mode (1/2/3/4/5/6): "))

    # Encryption/decryption options
    if mode in [1, 2]:
        filepath = input("Enter the file or folder path: ")
        if not os.path.exists(filepath):
            print("Path not found. Exiting.")
            return

        if os.path.isfile(filepath):
            if mode == 1:
                encrypt_file(filepath, key)
                print("File encrypted successfully.")
            elif mode == 2:
                decrypt_file(filepath, key)
                print("File decrypted successfully.")
        elif os.path.isdir(filepath):
            if mode == 1:
                encrypt_folder(filepath, key)
                print("Folder and its contents encrypted successfully.")
            elif mode == 2:
                decrypt_folder(filepath, key)
                print("Folder and its contents decrypted successfully.")

    elif mode in [3, 4]:
        message = input("Enter the message: ")
        if mode == 3:
            encrypt_string(message, key)
        elif mode == 4:
            decrypt_string(message, key)

    elif mode in [5, 6]:
        folder_path = input("Enter the folder path: ")
        if not os.path.exists(folder_path):
            print("Folder not found. Exiting.")
            return

        if mode == 5:
            encrypt_folder(folder_path, key)
            print("Folder and its contents encrypted successfully.")
        elif mode == 6:
            decrypt_folder(folder_path, key)
            print("Folder and its contents decrypted successfully.")

if __name__ == "__main__":
    main()