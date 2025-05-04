import os
import subprocess

REPO_DIR = os.path.dirname(os.path.abspath(__file__))

def git_push():
    try:
        os.chdir(REPO_DIR)
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "Aggiornamento prodotti automatico"], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("✅ Push completato con successo.")
    except subprocess.CalledProcessError as e:
        print("❌ Errore durante il push:", e)

if __name__ == "__main__":
    git_push()
