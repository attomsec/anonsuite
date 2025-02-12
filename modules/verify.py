import os
import subprocess
import modules.func
import modules.auto_install

# Função para verificar se o firejail está instalado

def verify_firejail_install():

    # subprocess.run(f"clear", shell=True)
    print("Verificando se o firejail está instalado e configurado...\n")
    
    try:
        # Tenta verificar se o firejail está instalado
        subprocess.run(["firejail", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        modules.func.continue_key()
        return False
    
def verify_selinux_install():
    # Check if the os is Linux
    if os.name != 'posix':
        return "This function only works on Linux systems."

    # Check if SELinux is enabled
    try:
        result = subprocess.run(['sestatus'], stdout=subprocess.PIPE)
        output = result.stdout.decode('utf-8')

        if 'SELinux status:                 enabled' not in output:
            return "SELinux is not currently enabled."

        if 'Policy MLS status:              enabled' not in output:
            return "\nSELinux is enabled but MLS policy is not enforcing."

        return "\nSELinux is enabled and MLS policy is enforcing."

    except Exception as e:
        print("SELinux parece nao estar instalado. Instalando automaticamente...")
        modules.auto_install.install_selinux()

def verify_macchanger_install():

    print("\nVerificando se o macchanger está instalado e configurado...\n")
    
    try:
        # Tenta verificar se o firejail está instalado
        subprocess.run(["macchanger", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        modules.func.continue_key()
        return False
