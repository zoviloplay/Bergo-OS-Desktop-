# safety.py – Bergo OS Performance Safety System

import psutil
import time

MAX_TEMP = 79  # °C Grenze
MAX_CPU = 95   # % Auslastung
CHECK_INTERVAL = 5  # Sekunden

def check_system_safety():
    cpu = psutil.cpu_percent(interval=1)
    temp = psutil.sensors_temperatures().get('cpu_thermal', [{}])[0].get('current', 0)

    if cpu > MAX_CPU:
        print("[Safety] CPU zu hoch:", cpu, "% – Boost deaktiviert.")
        return False
    if temp > MAX_TEMP:
        print("[Safety] Temperatur zu hoch:", temp, "°C – Boost deaktiviert.")
        return False

    print("[Safety] System stabil:", cpu, "% CPU,", temp, "°C")
    return True

def safety_loop():
    while True:
        check_system_safety()
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    safety_loop()
