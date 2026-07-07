@echo off
set SCRIPT_PATH=%~dp0..\src\retrain.py
for %%I in ("%SCRIPT_PATH%") do set SCRIPT_PATH=%%~fI
set PYTHON_EXE=python

schtasks /create /tn "SentimentRetrain" /tr "%PYTHON_EXE% \"%SCRIPT_PATH%\"" /sc weekly /d SUN /st 00:00
echo Tâche planifiée 'SentimentRetrain' créée avec succès.
pause
