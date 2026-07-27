# oc_manager.py – Bergo OS Overclock Manager

import json
import psutil
import time

def load_profiles():
    with open("performance/profiles.json", "r") as f:
        return json.load(f)

def apply_profile(profile_name):
    profiles = load_profiles()
    profile = profiles.get(profile_name)

    if not profile:
        print("[OC] Profil nicht gefunden:", profile_name)
        return

    print(f"[OC] Aktiviere Profil: {profile_name}")
    print(f"CPU-Limit: {profile['cpu_limit']}% | GPU-Limit: {profile['gpu_limit']}% | Temp-Limit: {profile['temp_limit']}°C")

    # Hier später echte Overclock-API oder Cluster-Boost einbauen
    time.sleep(1)
    print("[OC] Profil erfolgreich angewendet.")

if __name__ == "__main__":
    apply_profile("normal")
