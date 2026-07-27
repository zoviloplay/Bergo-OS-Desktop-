# instalire apps aus pi apps
   import os

apps = [
    "Nemo",
    "Stacer",
    "Better Chromium",
    "Drop-Down Terminal"
]

for app in apps:
    print(f"⬇️ Installiere {app}...")
    os.system(f'~/pi-apps/manage install "{app}"')
    print(f"✔️ {app} installiert.\n")

print("🎉 Alle Apps installiert! Desktop wird vorbereitet...")
