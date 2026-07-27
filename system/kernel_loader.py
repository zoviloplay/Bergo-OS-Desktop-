import boot_sequence
import hardware_check
import drivers

def start_kernel():
    print("Starte Bergo Kernel...")

    hardware_check.run()
    drivers.load_all()
    boot_sequence.run()

    print("Kernel erfolgreich gestartet.")
