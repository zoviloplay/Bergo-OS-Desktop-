def help():
    print("Verfügbare Befehle:")
    print("help  - zeigt alle Befehle")
    print("info  - zeigt OS-Informationen")
    print("clear - leert den Bildschirm")
    print("exit  - Terminal beenden")

def info():
    print("Bergo OS Terminal v0.1.0")

def clear():
    print("\033[H\033[J")  # Terminal clear

def exit_terminal():
    print("Terminal wird beendet...")
    exit()
