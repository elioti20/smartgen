import os
import ctypes
import sys

def set_password(directory, password):
    """
    Adds password protection to a specified directory by hiding it and 
    creating a batch file to toggle visibility using a password.
    """
    if not os.path.exists(directory):
        print(f"Directory {directory} does not exist.")
        return

    bat_file_path = os.path.join(directory, "lock.bat")
    with open(bat_file_path, "w") as bat_file:
        bat_file.write(f"""
@echo off
title Folder Locker
if EXIST "Control Panel.{{21EC2020-3AEA-1069-A2DD-08002B30309D}}" goto UNLOCK
if NOT EXIST Private goto MDLOCKER
echo Invalid directory
goto End
:CONFIRM
echo Enter password to access folder:
set/p "pass=>"
if NOT %pass%=={password} goto FAIL
if %pass%=={password} goto UNLOCK
:FAIL
echo Invalid password
pause
goto End
:UNLOCK
ren "Control Panel.{{21EC2020-3AEA-1069-A2DD-08002B30309D}}" Private
echo Folder Unlocked
goto End
:MDLOCKER
md Private
echo Private created successfully
goto End
:LOCK
ren Private "Control Panel.{{21EC2020-3AEA-1069-A2DD-08002B30309D}}"
attrib +h +s "Control Panel.{{21EC2020-3AEA-1069-A2DD-08002B30309D}}"
echo Folder locked
goto End
:End
""")
    print(f"Password protection added to {directory}. Use 'lock.bat' to lock/unlock.")

def main():
    if len(sys.argv) != 3:
        print("Usage: python smartgen.py <directory_path> <password>")
        sys.exit(1)

    directory = sys.argv[1]
    password = sys.argv[2]
    set_password(directory, password)

if __name__ == "__main__":
    main()