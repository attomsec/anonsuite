import os
import subprocess
import time
import modules.functions

def session_script_exec():

    directory = os.path.expanduser("~/Downloads/session/session.AppImage")
    check_directory(directory)

def run_session():

    print('\033[1;31m' + "Warning:" + '\033[0;33m' + " Session will run in amnesia mode. This means that once you close the app, everything will be permanently deleted! Make sure to back up your recovery key or you won't be able to recover your account (if needed)" + '\033[0;97m')
    modules.functions.continue_key()

    print("Insert a never used different vendor MAC address to improve anonymity")
    print('\033[1;90m' + "\nTip: You can generate a MAC address with AnonSuite. Check menu." + '\033[1;97m')
    mac = input("\nNew mac: ")
    print(f"\nChosen MAC: {mac}\n")
    print("Chosen MAC address: " + mac)
    time.sleep(1)

    print("\nChoose network interface to be used by Firejail")
    interface = input("\nInterface: ")
    print("\nChosen interface: " + interface)
    time.sleep(1)

    subprocess.run(f"clear", shell=True)

    print("Executando Session App em modo amnésia na memória RAM em failsafe usando o comando:")
    print(f"\nfirejail --noprofile --private --private-tmp --ipc-namespaces --nosound --novideo --net={interface} --mac={mac} --appimage ~/Downloads/session/session.AppImage")
    print("\n")
    print("Pressione enter para executar...")
    input()

    command = f"firejail --noprofile --private --private-tmp --ipc-namespaces --nosound --novideo --net={interface} --mac={mac} --appimage ~/Downloads/session/session.AppImage"
    modules.functions.command_exec(command)

    subprocess.run(f"clear", shell=True)
    print("Session App " + '\033[1;31m' + "killed." + '\033[0;97m' + " Contracted amnesia.")
    time.sleep(3)

def check_directory(directory):

    if os.path.isfile(directory):
        subprocess.run(f"clear", shell=True)
        print(f"Status: O diretório '{directory}' existe.\n")
        run_session()
    else:
        subprocess.run(f"clear", shell=True)
        print(f"O diretório '{directory}' não existe.")
        print("\nAviso: Você deve copiar o AppImage do Session em /home/seu_usuario/Downloads/session/ !!!")
        print("O nome da pasta que contém o AppImage deve ser 'session' !!!")
        print("\n")
        print("Pressione uma tecla para voltar ao menu...")
        input()