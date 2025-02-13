import time
import json
import subprocess
import modules.functions
import modules.mac_ram
import modules.mac_changer
import modules.run_session
import modules.tor_ram_jail
import signal

def continue_key():

    print("\nPressione uma tecla para continuar...")
    input()

def secure_exit(signal, frame):

    subprocess.run(f"clear")
    print("Ctrl + C detected. Exiting...")
    print('\033[1;31m' + "\nCleaning bash_history file")
    subprocess.run("echo -n > ~/.bash_history", shell=True)
    print('\033[1;33m' + "\nStatus: "+ '\033[1;32m' + "bash_history file cleaned\n")
    exit(0)

signal.signal(signal.SIGINT, secure_exit)

def show_menu():    

    with open('modules/json/info.json') as f:
        data = json.load(f)
    
    subprocess.run(f"clear")
        
    presentation()
        
    print('\033[0;32m' + "version:" ,data['version'] + 20*" " + "author:", data["author"]["name"])
        
    print('\033[0;97m' + "\n---------------Choose one option-------------------\n")
        
    print('\033[0;32m' + "Tor Browser:"+'\033[0;97m')
    print("1. Run Tor Browser isolated (no audio)")
    print("2. Run Tor Browser isolated with audio (less safe)")

        
    print('\033[0;32m' + "Mac Spoofing:"+'\033[0;97m')

    print("3. Change device MAC address")
    print("4. MAC Generator on isolated Mullvad Browser (Offline)")


    print('\033[0;32m' + "Secure communication:"+'\033[0;97m')

    print("5. Run Session App fully isolated (amnesia mode)")


    print('\033[0;32m' + "Blind UFW"+'\033[0;97m')

    print("6. Run script to make UFW more secure")

    print("\n0. " + '\033[0;31m' + "Exit"+'\033[0;97m')

def cmd_console():

    print(13*"----")
    opcao = input('\033[1;33m' + "cmd: " + '\033[0;97m').strip()
        
    if opcao == "1" or opcao == "2":
            modules.tor_ram_jail.tor_script_exec(opcao)
    elif opcao == "3":
            modules.mac_changer.change_mac()
    elif opcao == "4":
            modules.mac_ram.mac_ram_script_exec()
    elif opcao == "5":
            modules.run_session.session_script_exec()
    elif opcao == "6":
            subprocess.run(f"clear")
            print("AnonSuite is making UFW more secure. Please wait and follow the instructions ahead.")
            time.sleep(2)
            command = f"./modules/shell/blind_ufw.sh"
            subprocess.run(command)
    elif opcao == "0" or opcao == "exit":
        subprocess.run(f"clear", shell=True)
        print("Exiting...")
        clean_bash()
    elif opcao == "install dependencies":
         subprocess.run(f"clear", shell=True)
         print("Instalando dependencias... Necesário "+ '\033[0;31m' + "root" + '\033[0;97m' + " !!!\n")
         time.sleep(2)
         command = f"./modules/shell/install_dependencies.sh"
         command_exec(command)
         modules.functions.continue_key()

    else:
        print("\nInvalid option. Try again.")
        time.sleep(2)

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

def command_exec(comando):

    try:
        subprocess.run(comando, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"{e}")
        print("\nPressione uma tecla para continuar...")
        input()

def clean_bash():

    print("\nCleaning bash_history file")
    subprocess.run("echo -n > ~/.bash_history", shell=True)
    print("\nStatus: bash_history file cleaned\n")
    exit(0)

def presentation():

    title = str('\033[0;97m'+"""
 ▗▄▖ ▗▖  ▗▖ ▗▄▖ ▗▖  ▗▖ ▗▄▄▖▗▖ ▗▖▗▄▄▄▖▗▄▄▄▖▗▄▄▄▖
▐▌ ▐▌▐▛▚▖▐▌▐▌ ▐▌▐▛▚▖▐▌▐▌   ▐▌ ▐▌  █    █  ▐▌   
▐▛▀▜▌▐▌ ▝▜▌▐▌ ▐▌▐▌ ▝▜▌ ▝▀▚▖▐▌ ▐▌  █    █  ▐▛▀▀▘
▐▌ ▐▌▐▌  ▐▌▝▚▄▞▘▐▌  ▐▌▗▄▄▞▘▝▚▄▞▘▗▄█▄▖  █  ▐▙▄▄▖
                .:stay anon:.""")
    
    welcome = title
    print(welcome)