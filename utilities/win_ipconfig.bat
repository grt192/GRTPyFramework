@echo off
:: BatchGotAdmin
:-------------------------------------
REM  --> Check for permissions
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"

REM --> If error flag set, we do not have admin.
if '%errorlevel%' NEQ '0' (
    echo Requesting administrative privileges...
    goto UACPrompt
) else ( goto gotAdmin )

:UACPrompt
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    set params = %*:"=""
    echo UAC.ShellExecute "%~s0", "%params%", "", "runas", 1 >> "%temp%\getadmin.vbs"

    "%temp%\getadmin.vbs"
    exit /B

:gotAdmin
    if exist "%temp%\getadmin.vbs" ( del "%temp%\getadmin.vbs" )
    pushd "%CD%"
    CD /D "%~dp0"
:--------------------------------------
set /p teamnum="Enter team number: " %=%
set /a "fbyte=teamnum/100"
set /a "lbyte=teamnum%%100"
netsh interface ip set address name="Wireless Network Connection" static 10.%fbyte%.%lbyte%.9 255.0.0.0 10.0.0.1
netsh interface ip set dns name="Wireless Network Connection" static 208.67.222.222
netsh interface ip add dns name="Wireless Network Connection" 208.67.220.220
