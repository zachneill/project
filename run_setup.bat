cls
@echo.
@echo [92m----- INSTALLING REQUIREMENTS -----[0m
echo off 
pip install -r requirements.txt
cmd /k "cd /d env\Scripts & activate & cd /d ../../ & start_server.bat"

