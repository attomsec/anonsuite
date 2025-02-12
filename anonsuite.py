from modules import auto_install
from modules import TorRamJail
from modules import func
import subprocess
from modules import verify

def main():

    subprocess.run(f"clear", shell=True)

    if not verify.verify_firejail_install():

        # Caso não esteja instalado, tenta instalar
        print("Firejail não está instalado.")
        auto_install.auto_install("firejail")

    else:

        print("Firejail está instalado.")
    
    print("\nVerificando status do SELinux...")
    print(verify.verify_selinux_install())

    if not verify.verify_macchanger_install():

        print("Macchanger não está instalado.")
        auto_install.auto_install("macchanger")
    else:
        print("Macchanger está instalado.")
    
    func.continue_key()

    # Exibe o menu de opções após a instalação (ou verificação de instalação) do firejail
    func.show_menu()

if __name__ == "__main__":
    main()