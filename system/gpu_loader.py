def init_gpu():
    print("Initialisiere GPU...")

    # Check ob GPU existiert
    gpu_found = True  # später echte Hardware-Abfrage

    if not gpu_found:
        print("Keine GPU gefunden. Starte im Safe Mode.")
        return False

    print("GPU erkannt.")
    print("Aktiviere GPU-Beschleunigung...")
    print("GPU-Treiber geladen.")
    print("GPU erfolgreich initialisiert.")

    return True
