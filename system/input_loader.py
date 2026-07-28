import os

print("🔌 Aktiviere Eingabegeräte...")

os.system("modprobe usbhid")
os.system("modprobe hid-generic")
os.system("modprobe evdev")

print("🖱️ Maus & ⌨️ Tastatur aktiv!")
