# Script Name:                          lab01-powershell.bat
# Author name:                          Tianna Farrow
# Date of latest revision:              01/08/2024
# Purpose:                              Powershell script that makes sure antivirus is installed and scanning, automatic screen lock, and automatic OS updates enabled. 
# Execution:                            add it as a .ps1 file on the server or copy code into powershell as 
# Additional resources:                 https://www.tenforums.com/tutorials/77458-rundll32-commands-list-windows-10-a.html; https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/timeout; https://ss64.com/nt/set.html


rem Set the lock delay in seconds (adjust as needed)
set LOCK_DELAY=300

echo Waiting for %LOCK_DELAY% seconds before locking the screen...
timeout /t %LOCK_DELAY% /nobreak

echo Locking the screen now...
rundll32.exe user32.dll,LockWorkStation

echo Screen locked successfully.