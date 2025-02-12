import os
import subprocess
import platform
import modules.func

diretorio = os.path.expanduser("~/Downloads/tor-browser/")

# Função para verificar se o diretório do tor-browser existe
def checar_diretorio(diretorio, opcao):

    if os.path.isdir(diretorio):
        subprocess.run(f"clear", shell=True)
        print(f"Aviso: O diretório '{diretorio}' existe.\n")
        ram_jail(opcao)
    else:
        print(f"O diretório '{diretorio}' não existe.")
        print("\nAviso: Você deve extrair o Tarball do Tor Browser em /home/seu_usuario/Downloads/tor-browser/ !!!")
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

    mac = input("Digite um endereço mac diferente para maior anonimidade: ")
    print(f"\nO mac escolhido foi: {mac}\n")

    rede = input("Digite a interface de rede que será utilizada pelo Firejail: ")
    print(f"A interface de rede escolhida foi: {rede}\n")

    torrc_path = os.path.expanduser("~/Downloads/tor-browser/Browser/TorBrowser/Data/Tor/torrc")
    subprocess.run(f"clear", shell=True)
    print(f"\nExibindo conteúdo de {torrc_path}:")
    print("\nConteudo torrc:")
    print("#########################\n")
    exibir_arquivo(torrc_path)
    print("\n#########################")
    print("\nPressione enter para continuar...")
    input()

    subprocess.run(f"clear", shell=True)

    # Copiar o diretório do Tor para a memória RAM
    print("Copiando o Tor Browser para a memória RAM...")
    subprocess.run(f"cp -r {diretorio} /dev/shm", shell=True)
    print("\nStatus: Concluído")

    if opcao == "1":
        print("\n")
        print("Executando tor browser (sem áudio) na memória RAM em failsafe usando o comando firejail->")
        print(f"\nfirejail --noprofile --ipc-namespace --machine-id --novideo --nosound --caps.drop=all --private-tmp --net={rede} --mac={mac} /dev/shm/tor-browser/Browser/start-tor-browser;")
        print("\n")
        print("Pressione enter para executar...")
        input()

        subprocess.run(f"clear", shell=True)

        # Executar o Tor Browser com o firejail
        firejail_command = f"firejail --noprofile --ipc-namespace --machine-id --novideo --nosound --caps.drop=all --private-tmp --net={rede} --mac={mac} /dev/shm/tor-browser/Browser/start-tor-browser"
        modules.func.command_exec(firejail_command)

    elif opcao == "2":
        
        print("\n")
        print("Executando tor browser (com áudio) na memória RAM em failsafe usando o comando firejail->")
        print(f"\nfirejail --noprofile --ipc-namespace --machine-id --caps.drop=all --private-tmp --net={rede} --mac={mac} /dev/shm/tor-browser/Browser/start-tor-browser;")
        print("\n")
        print("Pressione enter para executar...")
        input()

        subprocess.run(f"clear", shell=True)

        # Executar o Tor Browser com o firejail
        firejail_command = f"firejail --noprofile --ipc-namespace --machine-id --caps.drop=all --private-tmp --net={rede} --mac={mac} /dev/shm/tor-browser/Browser/start-tor-browser"
        command_exec(firejail_command)
    else:
        print("Opção inválida")

    subprocess.run(f"clear", shell=True)

    # Limpar a memória compartilhada
    modules.func.clean_memory()

    print("\n")
    print("Checando arquivo torrc! Confira se as Bridges foram deletadas corretamente !")
    print("\n")

    # Verificar se o torrc foi atualizado
    print("\nConteudo torrc:")
    print("#########################\n")
    exibir_arquivo(torrc_path)
    print("\n#########################")
    print("Pressione enter para continuar e voltar ao menu principal...")
    input()

def tor_script_exec(opcao):

    subprocess.run(f"clear", shell=True)

    diretorio = os.path.expanduser("~/Downloads/tor-browser/")

    # if opcao == "1":
    checar_diretorio(diretorio, opcao)
    # elif opcao == "2":
        # checar_diretorio(diretorio)


# Função para instalar o Firejail dependendo da distribuição
def install_firejail():

    print("O firejail será instalado automaticamente. Para confirmar tecle Enter")
    input()
    subprocess.run(f"clear", shell=True)
    distrib = platform.linux_distribution()[0].lower()
    try:
        if "debian" in distrib or "ubuntu" in distrib:
            print("Instalando firejail para distribuições Debian/Ubuntu...")
            subprocess.run(["sudo", "apt", "install", "firejail", "-y"], check=True)
        elif "fedora" in distrib or "redhat" in distrib:
            print("Instalando firejail para distribuições Fedora/RedHat...")
            subprocess.run(["sudo", "dnf", "install", "firejail", "-y"], check=True)
        elif "arch" in distrib:
            print("Instalando firejail para distribuições Arch Linux...")
            subprocess.run(["sudo", "pacman", "-S", "firejail", "-y"], check=True)
        else:
            print(f"Distribuição não reconhecida: {distrib}. Não é possível instalar firejail automaticamente.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao tentar instalar firejail: {e}")