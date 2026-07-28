import os

USER_FILE = "/system/userdata/user.txt"

def set_user(name):
    os.makedirs("/system/userdata", exist_ok=True)
    with open(USER_FILE, "w") as f:
        f.write(name)
    print(f"👤 Benutzer gesetzt: {name}")

def get_user():
    if not os.path.exists(USER_FILE):
        return "Unbekannt"
    with open(USER_FILE, "r") as f:
        return f.read().strip()

def switch_user(new_user):
    set_user(new_user)
    print(f"🔄 Benutzer gewechselt zu: {new_user}")
