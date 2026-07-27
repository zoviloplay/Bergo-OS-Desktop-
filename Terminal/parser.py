import commands

def handle(cmd):
    if cmd == "help":
        commands.help()
    elif cmd == "info":
        commands.info()
    elif cmd == "clear":
        commands.clear()
    elif cmd == "exit":
        commands.exit_terminal()
    else:
        print("Unbekannter Befehl:", cmd)
