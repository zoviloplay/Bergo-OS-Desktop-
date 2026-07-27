import os

# 1️⃣ WLAN & Bluetooth zuerst aktivieren
print("📶 Aktiviere WLAN...")
os.system("sudo rfkill unblock wifi")
os.system("sudo ifconfig wlan0 up")
print("✅ WLAN aktiviert.\n")

print("🔵 Aktiviere Bluetooth...")
os.system("sudo rfkill unblock bluetooth")
os.system("sudo systemctl start bluetooth")
print("✅ Bluetooth aktiviert.\n")

# 2️⃣ Danach Apps installieren
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

print("🎉 Alle Apps installiert und Verbindungen aktiv! Desktop wird vorbereitet...")
