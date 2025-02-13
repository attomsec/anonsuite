import os
import subprocess
import modules.functions

directory = os.path.expanduser("~/Downloads/mullvad-browser/")
html_file = "modules/html/mac-random.html"
app_id = "mac-ram"

# Função para verificar se o diretório do tor-browser existe
def check_directory(directory):

    if os.path.isdir(directory):
        subprocess.run(f"clear", shell=True)
        print(f"Aviso: O diretório '{directory}' existe.\n")
        mac_ram()
    else:
        print(f"O diretório '{directory}' não existe.")
        print(f"\nAviso: Você deve extrair o Tarball do Mullvad Browser em {directory}")
        print("O nome da pasta deve ser 'mullvad-browser' !!!")
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

def mac_ram():

    # subprocess.run(f"clear", shell=True)

    # Copiar o diretório do Mullvad para a memória RAM
    print("Copiando o Mullvad Browser para a memória RAM...")
    subprocess.run(f"cp -r {directory} /dev/shm", shell=True)
    subprocess.run(f"cp -r {html_file} /dev/shm", shell=True)
    subprocess.run(f"rm -rf /dev/shm/mullvad-browser/Browser/distribution/*", shell=True)
    print("\nStatus: Concluído")

    print("\n")
    print("Executando Mullvad Browser (offline) na memória RAM em failsafe usando o comando firejail ->")
    print(f"\nfirejail --noprofile --ipc-namespace --machine-id --novideo --nosound --caps.drop=all --private-tmp --net=none /dev/shm/mullvad-browser/Browser/start-mullvad-browser file:///dev/shm/mac-random.html")
    print("\n")
    print("Pressione enter para executar...")
    input()

    subprocess.run(f"clear", shell=True)

    # Executar o Mullvad Browser com o firejail
    firejail_command = f"firejail --noprofile --ipc-namespace --machine-id --novideo --nosound --caps.drop=all --private-tmp --net=none /dev/shm/mullvad-browser/Browser/start-mullvad-browser file:///dev/shm/mac-random.html"
    modules.functions.command_exec(firejail_command)

    subprocess.run(f"clear", shell=True)

    # Limpar a memória compartilhada
    modules.functions.clean_memory(app_id)

def mac_ram_script_exec():

    subprocess.run(f"clear", shell=True)

    # directory = os.path.expanduser("~/Downloads/mullvad-browser/")

    check_directory(directory)

