from modules import func
import subprocess

def main():

    subprocess.run("clear", shell=True)
    print("Initializing... \n")
    print('\033[1;33m' + "Aviso: "+ '\033[0;97m' + "Instale todas as dependências necessárias através do arquivo 'install_dependencies.sh' !!!")
    print("\nBem-Vindo ao " + '\033[1;32m' + "AnonSuite" + '\033[0;90m' + "\n\nStay anonymous...")
    func.continue_key()


    while True:
        func.show_menu()
        func.cmd_console()

if __name__ == "__main__":
    main()