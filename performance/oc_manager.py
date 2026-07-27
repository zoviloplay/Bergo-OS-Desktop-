import json

def load_profiles():
    with open("performance/profiles.json") as f:
        return json.load(f)

def apply_profile(name):
    profiles = load_profiles()
    if name not in profiles:
        print("Profil nicht gefunden.")
        return

    profile = profiles[name]
    print(f"Aktiviere Profil: {name}")
    print("CPU-Takt:", profile["cpu_clock"])
    print("GPU-Offset:", profile["gpu_clock_offset"])
    print("VRAM-Offset:", profile["vram_clock_offset"])
    # Hier würden später echte Hardware-Calls kommen
