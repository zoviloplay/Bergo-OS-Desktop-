import os
import time

def show_login():
    print("🔐 Bergo OS Login")
    print("-------------------------")
    username = input("👤 Benutzername: ")
    password = input("🔑 Passwort: ")

    # Passwort prüfen
    if os.path.exists("/system/userdata/pass.txt"):
        with open("/system/userdata/pass.txt", "r") as f:
            saved = f.read().strip()

        if password == saved:
            print("✅ Login erfolgreich!")
            time.sleep(1)
            os.system("python3 /main/main_start.py")
        else:
            print("❌ Falsches Passwort!")
            time.sleep(1)
            show_login()
    else:
        print("⚠️ Kein Passwort gesetzt – Standard wird erstellt.")
        os.makedirs("/system/userdata", exist_ok=True)
        with open("/system/userdata/pass.txt", "w") as f:
            f.write(password)
        print("🔧 Passwort gespeichert – bitte erneut einloggen.")
        show_login()

if __name__ == "__main__":
    show_login()
