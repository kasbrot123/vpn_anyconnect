echo off

ipconfig | find "tugraz.local"


IF %ERRORLEVEL% EQU 0 (
    echo already connected to tugraz.local
) ELSE (
    REM for safety reasons call vpnclose before
    call vpnclose
    python %~dp0%vpn_connect.py
    REM echo connected to tugraz.local
)


