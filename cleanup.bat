@echo off
echo Cleaning up project...

:: Remove Python cache files
for /d /r . %%d in (__pycache__) do @if exist "%%d" rd /s /q "%%d"
del /s /q *.pyc
del /s /q *.pyo
del /s /q *.pyd

:: Remove IDE files
if exist .idea rd /s /q .idea
if exist .vscode rd /s /q .vscode
del /s /q *.swp
del /s /q *.swo

:: Remove environment files
if exist venv rd /s /q venv
if exist .venv rd /s /q .venv
if exist ENV rd /s /q ENV

:: Remove database files
if exist db.sqlite3 del db.sqlite3

:: Remove static files
if exist staticfiles rd /s /q staticfiles

echo Cleanup complete!
pause 