@echo off
cd /d %~dp0

REM Attiva il virtualenv se esiste
if exist venv\Scripts\activate.bat (
    call venv\Scripts\activate.bat
)

start http://127.0.0.1:5000/anteprima-prodotti
echo Avvio del server Flask...
python app.py
pause
