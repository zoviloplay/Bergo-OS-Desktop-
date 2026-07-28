# Bergo OS Main Starter – lädt ALLE Kernmodule
import os
import time

def start_kernel():
    print("🧠 Starte Kernel...")
    os.system("python3 /system/kernel_loader.py")

def start_input():
    print("🖱️ Lade Maus & Tastatur...")
    os.system("python3 /system/input_loader.py")

def start_network():
    print("🌐 Starte Internet-Modul...")
    os.system("python3 /system/network_manager.py")

def start_gpu():
    print("🎮 Initialisiere GPU...")
    os.system("python3 /system/gpu_loader.py")

def start_hardware_check():
    print("🔍 Prüfe Hardware...")
    os.system("python3 /system/hardware_check.py")

def start_boot_sequence():
    print("🚀 Starte Boot-Sequenz...")
    os.system("python3 /system/boot_sequence.py")

def start_desktop_setup():
    print("🖥️ Lade Desktop-Setup...")
    os.system("python3 /firmware/assets/setup_desktop.py")

def main_start():
    print("🌌 Bergo OS Main-Zentrum wird gestartet...\n")
    time.sleep(1)

    start_kernel()
    start_input()       # NEU – Maus + Tastatur
    start_network()     # NEU – Internet
    start_gpu()
    start_hardware_check()
    start_boot_sequence()
    start_desktop_setup()

    print("\n✅ Alle Systeme aktiv – Bergo OS vollständig geladen!")

if __name__ == "__main__":
    main_start()
