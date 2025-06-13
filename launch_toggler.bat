@echo off
:: Nathan's Toggler Hybrid Admin BAT Launcher
:: Check for admin rights by trying to list sessions
net session >nul 2>&1
if %errorlevel% == 0 (
    goto :run
) else (
    powershell -Command "Start-Process '%~f0' -Verb RunAs"
    exit /b
)
:run
cd /d "%~dp0"
python Nathans_Toggler.py
pause
