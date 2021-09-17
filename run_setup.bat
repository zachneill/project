echo off 
cls
pip install python-dotenv >nul
cmd /k "cd /d env\Scripts & activate & cd /d ../../ & start_server.bat"
