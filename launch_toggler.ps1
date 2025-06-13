# Nathan's Toggler Hybrid Admin PowerShell Launcher
# Self-elevate
If (-NOT ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator"))
{
    Start-Process powershell "-ExecutionPolicy Bypass -File `"$PSCommandPath`"" -Verb RunAs
    exit
}
Write-Host "Launching Nathan's Toggler..."
cd $PSScriptRoot
python Nathans_Toggler.py
Pause
