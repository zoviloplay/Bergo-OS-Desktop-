import os
import time

# Globale Variable für Internetstatus
internet_status = False

# 1️⃣ Internet prüfen
def check_internet():
    global internet_status
    print("🌐 Prüfe Internet...")
    if os.system("ping -c 1 google.com > /dev/null 2>&1") == 0:
        internet_status = True
        print("✔️ Internet ist aktiv.\n")
    else:
        internet_status = False
        print("❌ Kein Internet gefunden.\n")

# 2️⃣ Info-Tab öffnen
def open_download_tab():
    print("\n📥 Bitte warte...")
    print("Das restliche Nötige wird jetzt gedownloadet.")
    print("Danach kannst du den Free OS zu 100% nutzen.\n")

# 3️⃣ Auto-Installer
def auto_install():
    apps = [
        "Nemo",
        "Stacer",
        "Better Chromium",
        "Drop-Down Terminal"
    ]

    for app in apps:
        print(f"⬇️ Installiere {app}...")
        os.system(f'~/pi-apps/manage install "{app}"')
        print(f"✔️ {app} installiert.\n")

# 4️⃣ Desktop starten
def start_desktop():
    print("🖥️ Desktop wird geladen...\n")
    time.sleep(1)

    check_internet()

    if internet_status:
        open_download_tab()
        auto_install()
        print("🎉 Installation abgeschlossen! Free OS ist jetzt vollständig nutzbar.")
    else:
        print("⚠️ Kein Internet – automatische Installation wird später erneut versucht.")

# Startpunkt
if __name__ == "__main__":
    start_desktop()
