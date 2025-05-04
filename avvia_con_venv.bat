@echo off
cd /d %~dp0

REM Attiva il virtualenv se esiste
if exist venv\Scripts\activate.bat (
    call venv\Scripts\activate.bat
)

REM Avvia il browser e l'app Flask
start http://127.0.0.1:5000/anteprima-prodotti
python app.py
pause
