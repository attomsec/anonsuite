from modules import auto_install
from modules import TorRamJail
from modules import func
import subprocess
from modules import verify
from time import sleep

def main():

    subprocess.run("clear", shell=True)
    print("Initializing... \n")
    print('\033[1;33m' + "Aviso: "+ '\033[1;97m' + "Instale todas as dependências necessárias através do arquivo 'install_dependencies.sh' !!!")
    print("\nBem-Vindo ao " + '\033[1;32m' + "AnonSuite" + '\033[1;90m' + "\n\n\n\nstay anonymous...")
    sleep(8)

    func.show_menu()

if __name__ == "__main__":
    main()