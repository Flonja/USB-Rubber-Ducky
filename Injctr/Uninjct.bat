@echo off

echo.
echo Deleting the first stage!
del "C:\Users\%username%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\run.vbs"
echo Deleting the second stage!
del "C:\Users\%username%\mybad.bat"
echo Done!
pause