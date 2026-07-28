import os

PASS_FILE = "/system/userdata/pass.txt"

def set_password(new_pass):
    os.makedirs("/system/userdata", exist_ok=True)
    with open(PASS_FILE, "w") as f:
        f.write(new_pass)
    print("🔐 Neues Passwort gesetzt!")

def change_password(old, new):
    if not os.path.exists(PASS_FILE):
        print("⚠️ Kein Passwort vorhanden – setze neues.")
        set_password(new)
        return

    with open(PASS_FILE, "r") as f:
        saved = f.read().strip()

    if old == saved:
        set_password(new)
        print("🔄 Passwort geändert!")
    else:
        print("❌ Altes Passwort falsch!")

def check_password(pass_try):
    if not os.path.exists(PASS_FILE):
        return False
    with open(PASS_FILE, "r") as f:
        saved = f.read().strip()
    return pass_try == saved
