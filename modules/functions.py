import time
import json
import subprocess
import modules.functions
import modules.mac_ram
import modules.mac_changer
import modules.run_session
import modules.tor_ram_jail
import signal

# Pausa e aguarda uma tecla ser pressionada
def continue_key():

    print("\nPressione uma tecla para continuar...")
    input()

# Quando detecta CTRL + C deleta o arquivo .bash_history e fecha o AnonSuite
def secure_exit(signal, frame):

    subprocess.run(f"clear")
    print("Ctrl + C detected. Exiting...")
    print('\033[1;31m' + "\nCleaning bash_history file")
    subprocess.run("echo -n > ~/.bash_history", shell=True)
    print('\033[1;33m' + "\nStatus: "+ '\033[1;32m' + "bash_history file cleaned\n")
    exit(0)

# Captura a combinação CTRL + C e executa a função 'secure_exit()'
signal.signal(signal.SIGINT, secure_exit)

def show_menu():

    # Abre o arquivo info.json
    with open(f"modules/json/info.json") as info:
        data = json.load(info)

    # Limpa o terminal
    subprocess.run("clear", shell=True)

    # Exibe o banner, versão e author 
    presentation()
    print('\n\033[0;32m' + "version:" ,data['version'] + 17*" " + "author:", data["author"]["name"])
    print("")

    # Carrega o arquivo menu.json e percorre os titulos e opções gerando o menu principal
    with open(f"modules/json/menu.json") as menufile:
        data = json.load(menufile)
        for entry in data:
            print(f"\n\033[0;32m{entry['name']}\033[0m")
            for opt in entry['option']:
                print(opt)

# Configuração do console                
def cmd_console():

    print(13*"----")
    option = input('\033[1;33m' + "cmd: " + '\033[0;97m').strip()
        
    if option == "1" or option == "2":
            modules.tor_ram_jail.tor_script_exec(option)
    elif option == "3":
            modules.mac_changer.change_mac()
    elif option == "4":
            modules.mac_ram.mac_ram_script_exec()
    elif option == "5":
            modules.run_session.session_script_exec()
    elif option == "6":
            subprocess.run(f"clear")
            print("AnonSuite is making UFW more secure. Please wait and follow the instructions ahead.")
            time.sleep(2)
            command = f"./modules/shell/blind_ufw.sh"
            subprocess.run(command)
            print("\nPress any key to continue...")
            input()
    elif option == "0" or option == "exit":
        subprocess.run(f"clear", shell=True)
        print("Exiting...")
        clean_bash()
    elif option == "install dependencies":
         subprocess.run(f"clear", shell=True)
         print("Instalando dependencias... Necesário "+ '\033[0;31m' + "root" + '\033[0;97m' + " !!!\n")
         time.sleep(2)
         command = f"./modules/shell/install_dependencies.sh"
         command_exec(command)
         modules.functions.continue_key()
    elif option == "help":
         subprocess.run("less README.md", shell=True)

    else:
        print("\nInvalid option. Try again.")
        time.sleep(2)

# Limpa a memória ram (arquivos sendo usados em '/dev/shm/tor-browser/')
def clean_memory(id):

    if id == "tor-browser":
        subprocess.run(f"clear", shell=True)
        print("Cleaning shared memory (ram, failsafe)...")
        print("\n")
        subprocess.run("rm -rf /dev/shm/tor-browser/", shell=True)
        print("Status: " + '\033[1;32m' +  "Clean" + '\033[0;97m')
        time.sleep(3)
    elif id == "mac-ram":
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

# Limpa o arquivo .bash_history na home do usuário
def clean_bash():

    print("\nCleaning bash_history file")
    subprocess.run("echo -n > ~/.bash_history", shell=True)
    print("\nStatus: bash_history file cleaned\n")
    exit(0)

# Gera e imprime o banner (software logo)
def presentation():

    title = str('\033[0;97m'+"""
 ▗▄▖ ▗▖  ▗▖ ▗▄▖ ▗▖  ▗▖ ▗▄▄▖▗▖ ▗▖▗▄▄▄▖▗▄▄▄▖▗▄▄▄▖
▐▌ ▐▌▐▛▚▖▐▌▐▌ ▐▌▐▛▚▖▐▌▐▌   ▐▌ ▐▌  █    █  ▐▌   
▐▛▀▜▌▐▌ ▝▜▌▐▌ ▐▌▐▌ ▝▜▌ ▝▀▚▖▐▌ ▐▌  █    █  ▐▛▀▀▘
▐▌ ▐▌▐▌  ▐▌▝▚▄▞▘▐▌  ▐▌▗▄▄▞▘▝▚▄▞▘▗▄█▄▖  █  ▐▙▄▄▖
                .:stay anon:.""")
    
    welcome = title
    print(welcome)