import platform
import subprocess

def auto_install(package):

    match package:

        case "firejail":
            pkg = "firejail"
        case "selinux":
            pkg = "selinux"
            # pkgDebian0 = "policycoreutils"
            # pkgDebian1 = "selinux-utils"
            # pkgDebian2 = "selinux-basics"
            # pkgDebian3 = "selinux-policy-default"
        case "macchanger":
            pkg = "macchanger"
    
    print(f"O {pkg} será instalado automaticamente. Para confirmar tecle Enter")
    input()
    subprocess.run(f"clear", shell=True)
    distrib = platform.linux_distribution()[0].lower()
    
    if pkg == "selinux":
    
        if "debian" in distrib or "ubuntu" in distrib:
                print(f"Instalando {pkg} para distribuições Debian/Ubuntu...")
                # subprocess.run(["sudo", "apt", "install", f"{pkg}", "-y"], check=True)
                subprocess.run(["sudo", "apt", "install", "policycoreutils", "selinux-utils", "selinux-basics", "selinux-policy-default" "-y"], check=True)
        else:
            try:
                if "debian" in distrib or "ubuntu" in distrib:
                    print(f"Instalando {pkg} para distribuições Debian/Ubuntu...")
                    subprocess.run(["sudo", "apt", "install", f"{pkg}", "-y"], check=True)
                elif "fedora" in distrib or "redhat" in distrib:
                    print(f"Instalando {pkg} para distribuições Fedora/RedHat...")
                    subprocess.run(["sudo", "dnf", "install", f"{pkg}", "-y"], check=True)
                elif "arch" in distrib:
                    print(f"Instalando {pkg} para distribuições Arch Linux...")
                    subprocess.run(["sudo", "pacman", "-S", f"{pkg}", "-y"], check=True)
                else:
                    print(f"Distribuição não reconhecida: {distrib}. Não é possível instalar {pkg} automaticamente.")
            except subprocess.CalledProcessError as e:
                print(f"Erro ao tentar instalar {pkg}: {e}")


# Função para instalar o Firejail dependendo da distribuição
# def install_firejail():

#     print("O firejail será instalado automaticamente. Para confirmar tecle Enter")
#     input()
#     subprocess.run(f"clear", shell=True)
#     distrib = platform.linux_distribution()[0].lower()
#     try:
#         if "debian" in distrib or "ubuntu" in distrib:
#             print("Instalando firejail para distribuições Debian/Ubuntu...")
#             subprocess.run(["sudo", "apt", "install", "firejail", "-y"], check=True)
#         elif "fedora" in distrib or "redhat" in distrib:
#             print("Instalando firejail para distribuições Fedora/RedHat...")
#             subprocess.run(["sudo", "dnf", "install", "firejail", "-y"], check=True)
#         elif "arch" in distrib:
#             print("Instalando firejail para distribuições Arch Linux...")
#             subprocess.run(["sudo", "pacman", "-S", "firejail", "-y"], check=True)
#         else:
#             print(f"Distribuição não reconhecida: {distrib}. Não é possível instalar firejail automaticamente.")
#     except subprocess.CalledProcessError as e:
#         print(f"Erro ao tentar instalar firejail: {e}")

# def install_selinux():

#     print("O SELinux será instalado automaticamente. Para confirmar tecle Enter")
#     input()
#     subprocess.run(f"clear", shell=True)
#     distrib = platform.linux_distribution()[0].lower()
#     try:
#         if "debian" in distrib or "ubuntu" in distrib:
#             print("Instalando firejail para distribuições Debian/Ubuntu...")
#             subprocess.run(["sudo", "apt", "install", "policycoreutils", "selinux-utils", "selinux-basics", "selinux-policy-default" "-y"], check=True)
#             print("\nO SELinux será instalado automaticamente. Pressione enter para continuar a instalação...")
#             input()
#             print("\n Habilitando SELinux. Será necessário reiniciar após habilitado.")

#             subprocess.run("selinux-activate", check=True)
#             print("SELinux habilitado. Por favor reinicie o sistema para aplicar as mudanças e rode o AnonSuite novamente.")

#         elif "fedora" in distrib or "redhat" in distrib:
#             print("SELinux é instalado por padrão em sistemas baseados no RedHat")
#             # subprocess.run(["sudo", "dnf", "install", "firejail", "-y"], check=True)
#         elif "arch" in distrib:
#             print("É recomendado a instalação do Apparmor em distribuições baseadas no Archlinux")
#             # subprocess.run(["sudo", "pacman", "-S", "firejail", "-y"], check=True)
#         else:
#             print(f"Distribuição não reconhecida: {distrib}. Não é possível instalar firejail automaticamente.")
#     except subprocess.CalledProcessError as e:
#         print(f"Erro ao tentar instalar SELinux: {e}\n\nPor favor, instale manualmente.")

# def install_macchanger():

#     print("O macchanger será instalado automaticamente. Para confirmar tecle Enter")
#     input()
#     subprocess.run(f"clear", shell=True)
#     distrib = platform.linux_distribution()[0].lower()
#     try:
#         if "debian" in distrib or "ubuntu" in distrib:
#             print("Instalando macchanger para distribuições Debian/Ubuntu...")
#             subprocess.run(["sudo", "apt", "install", "macchanger", "-y"], check=True)
#         elif "fedora" in distrib or "redhat" in distrib:
#             print("Instalando macchanger para distribuições Fedora/RedHat...")
#             subprocess.run(["sudo", "dnf", "install", "macchanger", "-y"], check=True)
#         elif "arch" in distrib:
#             print("Instalando macchanger para distribuições Arch Linux...")
#             subprocess.run(["sudo", "pacman", "-S", "macchanger", "-y"], check=True)
#         else:
#             print(f"Distribuição não reconhecida: {distrib}. Não é possível instalar macchanger automaticamente.")
#     except subprocess.CalledProcessError as e:
#         print(f"Erro ao tentar instalar macchanger: {e}")


                