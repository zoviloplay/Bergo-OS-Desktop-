import system.kernel_loader as kernel
import time
import os

print("Starte Bergo OS...")
kernel.start_kernel()

# FAST Boot Animation
os.system("clear")
print("[LOGO] Fade-In")
time.sleep(0.5)
print("[LOGO] Glow-Effekt")
time.sleep(1)
print("[LOGO] Fade-Out")
time.sleep(0.5)
print("Desktop wird geladen...")
time.sleep(0.5)
