import subprocess
import time
import os

REPO_PATH = r"C:\Users\SmartHome360\Desktop\Smarthome360"

def run_git_command(command):
    result = subprocess.run(command, cwd=REPO_PATH, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout.strip()

def has_changes():
    status = run_git_command("git status --porcelain")
    return bool(status)

def main():
    print("Avvio push automatico ogni 30 secondi (solo se ci sono modifiche)...")
    while True:
        if has_changes():
            print("🟡 Modifiche rilevate. Eseguo commit e push...")
            run_git_command("git add .")
            run_git_command('git commit -m "Aggiornamento automatico via script"')
            result = run_git_command("git push origin main")
            print("✅ Push eseguito:", result)
        else:
            print("🔵 Nessuna modifica da pushare.")
        time.sleep(30)

if __name__ == "__main__":
    main()
