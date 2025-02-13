import time
import json
import subprocess
import modules.macchanger
import modules.run_session
import modules.TorRamJail
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

    with open('modules/info.json') as f:
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


    print('\033[0;32m' + "Secure communication:"+'\033[0;97m')

    print("4. Run Session App fully isolated (amnesia mode)")


    print('\033[0;32m' + "Blind UFW"+'\033[0;97m')

    print("5. Run script to make UFW more secure")

    print("\n0. " + '\033[0;31m' + "Exit"+'\033[0;97m')

def cmd_console():

    print(13*"----")
    opcao = input('\033[1;33m' + "console: " + '\033[1;97m').strip()
        
    if opcao == "1" or opcao == "2":
            modules.TorRamJail.tor_script_exec(opcao)
    elif opcao == "3":
            modules.macchanger.change_mac()
    elif opcao == "4":
            modules.run_session.session_script_exec()
    elif opcao == "5":
            subprocess.run(f"clear")
            print("AnonSuite is making UFW more secure. Please wait and follow the instructions ahead.")
            time.sleep(2)
            command = f"./modules/shell/blind_ufw.sh"
            subprocess.run(command)

    elif opcao == "0" or opcao == "exit":
        subprocess.run(f"clear")
        print("Exiting...")
        clean_bash()

    else:
        print("\nInvalid option. Try again.")
        time.sleep(2)

def clean_memory():
    subprocess.run(f"clear", shell=True)
    print("Cleaning shared memory (ram, failsafe)...")
    print("\n")
    subprocess.run("rm -rf /dev/shm/tor-browser/", shell=True)
    print("Status: Clean")

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
               """)
    
    welcome = title
    print(welcome)