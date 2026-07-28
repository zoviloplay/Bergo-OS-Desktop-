import os

print("🌐 Starte Netzwerk...")

os.system("systemctl start NetworkManager")
os.system("dhclient -v")

print("✅ Internet aktiv!")
