cls
@echo off
@echo.
@echo [94m----- ACTIVATED VIRTUAL ENVIRONMENT 'env' -----
@echo.
@echo [92m----- INSTALLING DEPENDENCIES FROM requirements.txt -----
pip install -r requirements.txt >nul

echo on
@echo.
@echo [95m----- STARTING MAIN.PY -----
@echo.
@echo [93m----- Ctrl+C 2+ times to exit, main.py to re-run -----[0m
@echo.
@echo off
python c:main.py %*
cmd /k