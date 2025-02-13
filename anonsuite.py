from modules import functions
import subprocess

def main():

    subprocess.run("clear", shell=True)
    print("Initializing... \n")
    print("Bem-Vindo ao " + '\033[1;32m' + "AnonSuite" + '\033[0;97m')
    # functions.presentation()
    print('\033[1;31m' + "\nAviso: "+ '\033[0;97m' + "No menu principal, rode o comando 'install dependencies' para instalar todas as dependencias necessárias.")
    functions.continue_key()


    while True:
        functions.show_menu()
        functions.cmd_console()

if __name__ == "__main__":
    main()