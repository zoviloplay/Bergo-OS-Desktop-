import parser

def start():
    print("Bergo Terminal gestartet. Tippe 'help' für Befehle.")

    while True:
        user_input = input("> ")
        parser.handle(user_input)
