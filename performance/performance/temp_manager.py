import psutil

MAX_TEMP = 79

def check_temp():
    temp = psutil.sensors_temperatures()['cpu_thermal'][0].current

    if temp >= MAX_TEMP:
        print(f"Warnung: {temp}°C erreicht! Aktiviere Throttle...")
        throttle()

def throttle():
    print("CPU & GPU werden gedrosselt...")

    # CPU runter
    set_cpu_clock(0.7)  # 70% Leistung

    # GPU runter
    set_gpu_clock(0.7)

    # VRAM leicht runter
    set_vram_clock(0.9)

    print("Throttle aktiv. Temperatur wird stabilisiert.")
