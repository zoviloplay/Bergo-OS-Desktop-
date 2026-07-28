
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
    start_drivers()
    start_gpu()
    start_hardware_check()
    start_boot_sequence()
    start_desktop_setup()

    print("\n✅ Alle Systeme aktiv – Bergo OS vollständig geladen!")

if __name__ == "__main__":
    main_start()
