import os
import subprocess
import time
import modules.functions

diretorio = os.path.expanduser("~/Downloads/tor-browser/")
app_id = "tor-browser"

# Função para verificar se o diretório do tor-browser existe
def check_directory(diretorio, opcao):

    if os.path.isdir(diretorio):
        subprocess.run(f"clear", shell=True)
        print(f"Aviso: O diretório '{diretorio}' existe.\n")
        ram_jail(opcao)
    else:
        print(f"O diretório '{diretorio}' não existe.")
        print(f"\nAviso: Você deve extrair o Tarball do Tor Browser em {diretorio}")
        print("O nome da pasta deve ser 'tor-browser' !!!")
        print("\n")
        print("Pressione uma tecla para voltar ao menu...")
        input()

def exibir_arquivo(arquivo):

    if os.path.exists(arquivo):
        with open(arquivo, 'r') as file:
            print(file.read())
    else:
        print(f"O arquivo {arquivo} não existe.")

def command_exec(comando):

    try:
        subprocess.run(comando, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"{e}")
        print("\nPressione uma tecla para continuar...")
        input()

def ram_jail(opcao):

    opcao = opcao

    print("Insert a never used different vendor MAC address to improve anonymity")
    print('\033[1;90m' + "\nTip: You can generate a MAC address with AnonSuite. Check menu." + '\033[1;97m')
    mac = input("\nNew mac: ")
    print(f"\nChosen MAC: {mac}")

    print("\nChoose network interface to be used by Firejail")
    interface = input("\nInterface: ")
    print(f"\nChosen interface: {interface}\n")
    time.sleep(1)

    # Copiar o diretório do Tor para a memória RAM
    print("\nCopiando o Tor Browser para a memória RAM...")
    subprocess.run(f"cp -r {diretorio} /dev/shm", shell=True)
    print("\nStatus: Concluído")
    time.sleep(1)

    subprocess.run(f"clear", shell=True)

    if opcao == "1":
        print("Executando tor browser (sem áudio) na memória RAM em failsafe usando o comando:")
        print(f"\nfirejail --noprofile --ipc-namespace --machine-id --novideo --nosound --caps.drop=all --private-tmp --net={interface} --mac={mac} /dev/shm/tor-browser/Browser/start-tor-browser;")
        print("\n")
        print("Pressione enter para executar...")
        input()

        subprocess.run(f"clear", shell=True)

        # Executar o Tor Browser com o firejail
        firejail_command = f"firejail --noprofile --ipc-namespace --machine-id --novideo --nosound --caps.drop=all --private-tmp --net={interface} --mac={mac} /dev/shm/tor-browser/Browser/start-tor-browser"
        modules.functions.command_exec(firejail_command)

    elif opcao == "2":
        print("Executando tor browser (com áudio) na memória RAM em failsafe usando o comando:")
        print(f"\nfirejail --noprofile --ipc-namespace --machine-id --caps.drop=all --private-tmp --net={interface} --mac={mac} /dev/shm/tor-browser/Browser/start-tor-browser;")
        print("\n")
        print("Pressione enter para executar...")
        input()

        subprocess.run(f"clear", shell=True)

        # Executar o Tor Browser com o firejail
        firejail_command = f"firejail --noprofile --ipc-namespace --machine-id --caps.drop=all --private-tmp --net={interface} --mac={mac} /dev/shm/tor-browser/Browser/start-tor-browser"
        command_exec(firejail_command)
    else:
        print("Opção inválida")

    subprocess.run(f"clear", shell=True)

    # Limpar a memória compartilhada
    modules.functions.clean_memory(app_id)

def tor_script_exec(opcao):

    subprocess.run(f"clear", shell=True)

    # diretorio = os.path.expanduser("~/Downloads/tor-browser/")

    check_directory(diretorio, opcao)

