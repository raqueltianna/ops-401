#!/usr/bin/env python3 

# Script Name:                      opschallenge31.py
# Author Name:                      Tianna Farrow
# Date of Latest Revision:          02/19/24
# Purpose:                          begin devlopment of my own basic antivirus tool in python
# Execution                         python3 opschallenge31.py 
# Additional Resources:             https://www.howtogeek.com/112674/how-to-find-files-and-folders-in-linux-using-the-command-line/; https://www.howtogeek.com/206097/how-to-use-find-from-the-windows-command-prompt/; https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-31/challenges/DEMO.md

import os

def search_file(filename, directory):
    hits = 0
    files_searched = 0
    
    print(f"Searching for '{filename}' in '{directory}'...\n")
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == filename:
                hits += 1
                print(f"Found: {file} --> {os.path.join(root, file)}")
            files_searched += 1
            
    print(f"\nSearch complete.")
    print(f"Files searched: {files_searched}")
    print(f"Hits found: {hits}")

def main():
    filename = input("Enter the filename to search for: ")
    directory = input("Enter the directory to search in: ")
    
    search_file(filename, directory)

if __name__ == "__main__":
    main()