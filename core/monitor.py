def check_services():
    print("Überprüfe Dienste...")

    services = ["gpu-controller", "network-manager", "desktop-engine"]
    active = [s for s in services if "controller" in s]

    print(f"Aktive Controller: {len(active)}")
    for s in active:
        print(" -", s)
