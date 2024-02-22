#!/usr/bin/env python3 

# Script Name:                      opschallenge32.py
# Author Name:                      Tianna Farrow
# Date of Latest Revision:          02/20/24
# Purpose:                          continue devlopment of my own basic antivirus tool in python
# Execution                         python3 opschallenge32.py 
# Additional Resources:             https://docs.python.org/3/library/hashlib.html; https://github.com/codefellows/seattle-cybersecurity-401d8/blob/main/class-32/challenges/DEMO.md;  https://www.programiz.com/python-programming/examples/hash-file; https://github.com/raqueltianna/ops-401/blob/main/opschallenge31.py

import os
import hashlib
import datetime

def search_file(filename, directory):
    hits = 0
    files_searched = 0
    
    print(f"Searching for '{filename}' in '{directory}'...\n")
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == filename:
                hits += 1
                file_path = os.path.join(root, file)
                print(f"Found: {file} --> {file_path}")
                print_file_details(file_path)
            files_searched += 1
            
    print(f"\nSearch complete.")
    print(f"Files searched: {files_searched}")
    print(f"Hits found: {hits}")

def print_file_details(file_path):
    # Get file size
    file_size = os.path.getsize(file_path)
    # Get current timestamp
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Generate MD5 hash
    md5_hash = generate_md5(file_path)
    
    # Print details
    print(f"Timestamp: {timestamp}")
    print(f"File Name: {os.path.basename(file_path)}")
    print(f"File Size: {file_size} bytes")
    print(f"MD5 Hash: {md5_hash}\n")

def generate_md5(file_path):
    hasher = hashlib.md5()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hasher.update(chunk)
    return hasher.hexdigest()

def main():
    filename = input("Enter the filename to search for: ")
    directory = input("Enter the directory to search in: ")
    
    search_file(filename, directory)

if __name__ == "__main__":
    main()