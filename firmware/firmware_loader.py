import configparser

def load_firmware():
    print("Lade Firmware...")

    boot = configparser.ConfigParser()
    boot.read("firmware/boot.cfg")

    gpu = configparser.ConfigParser()
    gpu.read("firmware/gpu.cfg")

    system = configparser.ConfigParser()
    system.read("firmware/system.cfg")

    print("Firmware erfolgreich geladen.")
    return boot, gpu, system
