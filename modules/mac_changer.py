import os
import subprocess
import modules.functions

def change_mac():
    
    subprocess.run(f"clear", shell=True)

    mac = input("Digite o MAC desejado: ")
    print(f"\nO mac escolhido foi: {mac}\n")

    interface = input("Digite a interface de rede para trocar o MAC: ")

    print("\nAviso: Será solicitado a senha do usuário para permitir a execução do macchanger!")
    
    print("\nSubstituindo mac com macchanger usando o comando>")
    print(f"\nsudo macchanger --mac={mac} {interface}")

    change_command = f"sudo macchanger --mac={mac} {interface}"
    print("\n")
    modules.functions.command_exec(change_command)
    # except subprocess.CalledProcessError as e:
    #     print("Erro ao tentar substituir o mac: " + f"\n{e}")