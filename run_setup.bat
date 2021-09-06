cls
@echo [92m----- INSTALLING REQUIREMENTS -----[0m
pip install -r requirements.txt
cls
@echo ^[45m----- STARTING run_setup.bat +-+-+[0m
@echo.
@echo.
@echo [93m----- ON STARTUP: Ctrl+C 2 times to exit and main.py to re-run -----[0m
@echo.
@echo.
@echo off
python c:main.py %*
cmd /k
