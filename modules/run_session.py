import os
import subprocess
import modules.func

def session_script_exec():

    directory = os.path.expanduser("~/Downloads/session/session.AppImage")
    check_directory(directory)

def run_session():

    print("Warning: Session will run in amnesia mode. This means that once you close the app, everything will be permanently deleted! Make sure to back up your recovery key or you won't be able to recover your account (if needed)")
    modules.func.continue_key()

    print("Insert a never used different vendor MAC address to improve anonymity")
    mac = input("\nNew mac: ")
    print("\nChoose network interface to be used by Firejail")
    interface = input("\nInterface: ")

    command = f"firejail --noprofile --private --private-tmp --ipc-namespaces --nosound --novideo --net={interface} --mac={mac} --appimage ~/Downloads/session/session.AppImage"
    modules.func.command_exec(command)

    subprocess.run(f"clear", shell=True)
    print("Session App killed. Contracted amnesia.")
    modules.func.continue_key()

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