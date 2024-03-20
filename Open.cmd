@echo off
setlocal enabledelayedexpansion

:: Set the script path to the directory of the batch script plus the filename
set "script_path=%~dp0Automatic_Alumn_Card_Generator_WEB_APP.py"

:: Change the directory to the script's directory
cd /d "%~dp0"

:: Extract the drive from the script_path
set "drive=!script_path:~0,2!"

:: Execute the Python script
python "!script_path!"
