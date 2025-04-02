SYSTEM CLEANUP TOOL
====================

Overview:
---------
The System Cleanup Tool is a Python-based utility designed to optimize your Windows system 
by deleting temporary files, prefetch data, and launching the built-in disk cleanup operation.
This tool helps free up disk space and improve system performance.

Features:
---------
- Admin Privilege Detection: Ensures the script runs with elevated rights for full cleanup.
- Path Cleanup: Deletes files from %TEMP%, C:\Windows\Temp, and C:\Windows\Prefetch.
- Windows Disk Cleanup: Launches the built-in cleanmgr tool.
- Interactive Menu: Choose to clean specific paths, run disk cleanup, or perform a full cleanup.
- Detailed Logs: Displays deleted files and skipped files (if in-use or permission-restricted).
- Automatic Admin Relaunch: If not running as administrator, the script relaunches itself with admin rights.

Installation & Setup:
----------------------
**Prerequisites**
- Python 3.x must be installed on your system.

**Setup Steps**
1. Download or clone the project folder.
2. (Optional) Set up a virtual environment:
     python -m venv venv
3. Activate the virtual environment:
   - On Windows CMD: venv\Scripts\activate
   - On Windows PowerShell: .\venv\Scripts\Activate.ps1
4. (Optional) Install dependencies if required:
     pip install -r requirements-cleanup.txt

Usage:
------
1. Navigate to the project folder in the terminal or command prompt.
2. Run the script:
     python cleanup_tool.py
3. Select an option from the menu:
   - 1: Clean Temp, %temp%, and Prefetch folders.
   - 2: Run Windows Disk Cleanup.
   - 3: Perform Full Cleanup (Path Cleanup + Disk Cleanup).
   - 4: Exit.

Notes:
------
- Running the script as Administrator is recommended for full access.
- Some files may be skipped if they are in use by the system.
- The tool does not delete critical system files, ensuring safe usage.

Troubleshooting:
----------------
- If the script does not delete files, ensure you have admin rights.
- If the script does not run, check if Python is installed and added to the system PATH.
- If facing permission issues, try running the script from an Administrator Command Prompt.

Credits:
--------
[Abhishek Maurya]
Feel free to connect and contribute!

