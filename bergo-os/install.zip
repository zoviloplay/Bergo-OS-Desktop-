#!/bin/bash

echo "📦 Installiere Bergo OS Free..."
INSTALL_DIR="/usr/local/bergo-os"

# Ordner erstellen
echo "📁 Erstelle Systemordner..."
sudo mkdir -p $INSTALL_DIR
sudo mkdir -p $INSTALL_DIR/main
sudo mkdir -p $INSTALL_DIR/system
sudo mkdir -p $INSTALL_DIR/firmware

# Dateien kopieren
echo "📂 Kopiere Dateien..."
sudo cp -r main/* $INSTALL_DIR/main/
sudo cp -r system/* $INSTALL_DIR/system/
sudo cp -r firmware/* $INSTALL_DIR/firmware/
sudo cp README.md $INSTALL_DIR/

# Startdatei ausführbar machen
echo "⚙️ Setze Berechtigungen..."
sudo chmod +x $INSTALL_DIR/main/main.py
sudo chmod +x $INSTALL_DIR/main/main_start.py

# Desktop‑Icon erstellen
echo "🖥️ Erstelle Desktop‑Starter..."
DESKTOP_FILE="$HOME/Desktop/BergoOS.desktop"

cat <<EOF > $DESKTOP_FILE
[Desktop Entry]
Type=Application
Name=Bergo OS Free
Exec=python3 /usr/local/bergo-os/main/main.py
Icon=/usr/local/bergo-os/firmware/assets/icon.png
Terminal=true
EOF

chmod +x "$DESKTOP_FILE"

echo "✅ Installation abgeschlossen!"
echo "➡️ Starte Bergo OS über das Desktop‑Icon."
