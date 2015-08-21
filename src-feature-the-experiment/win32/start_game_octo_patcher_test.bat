@echo off
cd ..

rem Read the contents of PPYTHON_PATH into %PPYTHON_PATH%:
set /P PPYTHON_PATH=<PPYTHON_PATH

rem Get the user input:
set ttiUsername=Invisblemario
rem Export the environment variables:
set ttiPassword=password
set TTI_PLAYCOOKIE=%ttiUsername%
set TTI_GAMESERVER=25.118.159.76

echo ===============================
echo Starting Toontown Infinite...
echo ppython: %PPYTHON_PATH%
echo Username: %ttiUsername%
echo Gameserver: %TTI_GAMESERVER%
echo ===============================

IF EXIST 1.0.0.txt (
DEL /Q 1.0.0.txt
ECHO. >>1.0.1.txt
set cd1=%cd%


%PPYTHON_PATH% -m toontown.toonbase.ClientStart
pause
