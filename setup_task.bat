@echo off
set SCRIPT_PATH=%~dp0retrain.py
set PYTHON_EXE=python

schtasks /create /tn "SentimentRetrain" /tr "%PYTHON_EXE% \"%SCRIPT_PATH%\"" /sc weekly /d SUN /st 00:00
echo Tâche planifiée 'SentimentRetrain' créée avec succès.
pause
