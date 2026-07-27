# terminal_oc.py

import sys
import json

def update_custom(cpu, gpu):
    with open("performance/profiles.json", "r") as f:
        data = json.load(f)

    data["custom"]["cpu"] = cpu
    data["custom"]["gpu"] = gpu

    with open("performance/profiles.json", "w") as f:
        json.dump(data, f, indent=4)

    print(f"[OC] CPU = {cpu} MHz | GPU = {gpu} MHz gespeichert.")

if __name__ == "__main__":
    cpu = int(sys.argv[1])
    gpu = int(sys.argv[2])
    update_custom(cpu, gpu)
