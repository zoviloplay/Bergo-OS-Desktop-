import parser

def start():
    print("Bergo Terminal gestartet. Tippe 'help' für Befehle.")

    while True:
        try:
            user_input = input("> ")
            parser.handle(user_input)

        except KeyboardInterrupt:
            print("\nBefehl abgebrochen (CTRL + C).")
            continue
