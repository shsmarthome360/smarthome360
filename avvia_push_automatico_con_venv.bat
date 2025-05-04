@echo off
cd /d %~dp0

REM Attiva il virtualenv se esiste
if exist venv\Scripts\activate.bat (
    call venv\Scripts\activate.bat
)

echo Avvio push automatico ogni 30 secondi...
python push_automatico.py
pause
