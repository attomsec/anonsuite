#!/bin/bash

# Função para instalar pacotes no Ubuntu/Debian
install_debian() {
    sudo apt update
    sudo apt install -y firejail macchanger selinux-utils wget git
}

# Função para instalar pacotes no CentOS/RHEL
install_centos() {
    sudo yum install -y firejail macchanger selinux-utils wget git
}

# Função para instalar pacotes no Fedora
install_fedora() {
    sudo dnf install -y firejail macchanger selinux-utils wget git
}

# Função para instalar pacotes no Arch Linux
install_arch() {
    sudo pacman -Syu --noconfirm firejail macchanger selinux-utils wget git
}

# Função para verificar a distro e chamar a função correspondente
install_dependencies() {
    # Verifica a distribuição
    if [[ -f /etc/os-release ]]; then
        . /etc/os-release
        DISTRO_NAME=$ID
        DISTRO_VERSION=$VERSION_ID
    else
        echo "Não foi possível determinar a distribuição."
        exit 1
    fi

    # Instala pacotes conforme a distribuição
    case "$DISTRO_NAME" in
        ubuntu|debian)
            echo "Detectado Ubuntu/Debian. Instalando pacotes..."
            install_debian
            ;;
        centos|rhel)
            echo "Detectado CentOS/RHEL. Instalando pacotes..."
            install_centos
            ;;
        fedora)
            echo "Detectado Fedora. Instalando pacotes..."
            install_fedora
            ;;
        arch)
            echo "Detectado Arch Linux. Instalando pacotes..."
            install_arch
            ;;
        *)
            echo "Distribuição não suportada ou desconhecida."
            exit 1
            ;;
    esac
}

# Executa a instalação
install_dependencies

# Mensagem de conclusão
echo "Instalação concluída com sucesso!"
