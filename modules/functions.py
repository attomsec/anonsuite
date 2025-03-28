import os
import time
import json
import subprocess
import modules.mac_ram
import modules.mac_changer
import modules.run_session
import modules.tor_ram_jail
import signal
import modules.data_protect
import modules.show_ipaddr

# Pausa e aguarda uma tecla ser pressionada
def continue_key():

    print("\nPress any key to continue...")
    input()

# Quando detecta CTRL + C e chama a função 'clean_exit'
def secure_exit(signal, frame):
    os.system("clear")
    print("CTRL + C detected !!!")
    time.sleep(2)
    clean_bash()

# # Limpa o arquivo .bash_history na home do usuário
def clean_bash():

    os.system("clear")
    print("Exiting...")
    print('\033[1;31m' + "\nCleaning .bash_history file")
    print('\033[1;31m' + "\nCleaning .histfile")
    subprocess.run("echo -n > ~/.bash_history", shell=True)
    subprocess.run("echo -n > ~/.histfile", shell=True)
    print('\033[1;33m' + "\nStatus:\n " + '\033[1;32m' + "\n.bash_history file cleaned\n.histfile cleaned\n")
    exit(0)

# Captura a combinação CTRL + C e executa a função 'secure_exit()'
signal.signal(signal.SIGINT, secure_exit)

def show_menu(data):

    # Limpa o terminal
    os.system("clear")

    # Exibe o banner, versão e author 
    presentation()
    print('\n\033[0;32m' + "version:" ,data['version'] + 17*" " + "author:", data["author"]["name"])
    print("")

    # Carrega o arquivo menu.json e percorre os titulos e opções gerando o menu principal
    with open(f"modules/json/menu.json") as menufile:
        data = json.load(menufile)
        for entry in data:
            print(f"\033[0;32m{entry['name']}\033[0m")
            for opt in entry['option']:
                print(opt)

# Configuração do console                
def cmd_console():

    print(13*"----")
    option = str(input('\033[1;33m' + "cmd: " + '\033[0;97m'))
        
    if option == "1" or option == "2":
            modules.tor_ram_jail.tor_script_exec(option)
    elif option == "3":
            modules.mac_changer.change_mac()
    elif option == "4":
            modules.mac_ram.mac_ram_script_exec()
    elif option == "5":
            modules.run_session.session_script_exec()
    elif option == "6":
            command = f"./modules/shell/blind_ufw.sh"
            subprocess.run(command)
    elif option == "7":
        modules.data_protect.protect_data("encrypt")
    elif option == "8":
        modules.data_protect.protect_data("decrypt")
    elif option == "9":
        modules.show_ipaddr.get_ip()
    elif option == "10":
        command = f"./modules/shell/run_stresser.sh"
        command_exec(command)
    elif option == "0" or option == "exit":
        clean_bash()
    elif option == "install dependencies":
         subprocess.run(f"clear", shell=True)
         print("Installing dependencies... "+ '\033[0;31m' + "Root" + '\033[0;97m' + " access required.\n")
         time.sleep(2)
         command = f"./modules/shell/install_dependencies.sh"
         command_exec(command)
         modules.functions.continue_key()
    elif option == "help":
         subprocess.run("less README.md", shell=True)
    else:
        print("\nInvalid option. Try again.")
        time.sleep(2)

# Limpa a memória ram (arquivos sendo usados em '/dev/shm/tor-browser/' ou '/dev/shm/mullvad-browser/')
def clean_memory(identity):

    if identity == "tor-browser":
        subprocess.run(f"clear", shell=True)
        print("Cleaning shared memory (ram, failsafe)...")
        print("\n")
        subprocess.run("rm -rf /dev/shm/tor-browser/", shell=True)
        print("Status: " + '\033[1;32m' +  "Clean" + '\033[0;97m')
        time.sleep(3)
    elif identity == "mac-ram":
        subprocess.run(f"clear", shell=True)
        print("Cleaning shared memory (ram, failsafe)...")
        print("\n")
        subprocess.run("rm -rf /dev/shm/mullvad-browser/", shell=True)
        subprocess.run("rm -rf /dev/shm/mac-random.html", shell=True)
        print("Status: " + '\033[1;32m' +  "Clean" + '\033[0;97m')
        time.sleep(3)

# Faz a execução de comandos pre determinados 
def command_exec(comando):

    try:
        subprocess.run(comando, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"{e}")
        print("\nPress enter to continue...")
        input()


def splash_screen():

    os.system("clear")
    print("Initializing... \n")
    print("Welcome to " + '\033[1;32m' + "AnonSuite" + '\033[0;97m')
    print('\033[1;31m' + "\nWarning: " + '\033[0;97m' + "From the main menu, run the 'install dependencies' command to install all required dependencies.")
    continue_key()

# Gera e imprime o banner (software logo)
def presentation():

    title = str('\033[0;97m'+"""
 _           __            
|_|__  _ __ (_     o _|_ _ 
| || |(_)| |__)|_| |  |_(/_

      .:stay anon:.""")
    
    welcome = title
    print(welcome)