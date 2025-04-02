@echo off
cd /d D:\Desktop\Projects\Python\system-cleanup-tool

:: Check if running as administrator
NET SESSION >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Requesting administrative privileges...
    powershell -Command "Start-Process '%~0' -Verb RunAs"
    exit
)

:: Check if the virtual environment exists
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
    echo Virtual environment created successfully.
)

:: Activate the virtual environment
call venv\Scripts\activate

:: Install dependencies specific to this project
if exist requirements-cleanup.txt (
    echo Installing dependencies...
    pip install -r requirements-cleanup.txt
)

:: Run the cleanup tool
python cleanup_tool.py
:: Pause to keep the admin CMD window open
pause
