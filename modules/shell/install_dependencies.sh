#!/bin/bash -p

# Function to install packages on Ubuntu/Debian
install_debian() {
    sudo apt update
    sudo apt install -y firejail macchanger selinux-utils wget git ufw iptables curl
    pip3 install cryptography
}

# Function to install packages on CentOS/RHEL
install_centos() {
    sudo yum install -y firejail macchanger selinux-utils wget git ufw iptables curl
    pip3 install cryptography
}

# Function to install packages on Fedora
install_fedora() {
    sudo dnf install -y firejail macchanger selinux-utils wget git ufw iptables curl
    pip3 install cryptography
}

# Function to install packages on Arch Linux
install_arch() {
    sudo pacman -Syu --noconfirm firejail macchanger selinux-utils wget git ufw iptables curl
    pip install cryptography
}

# Function to check the distro and call the corresponding function
install_dependencies() {
    # Check the distribution
    if [[ -f /etc/os-release ]]; then
        . /etc/os-release
        DISTRO_NAME=$ID
        DISTRO_VERSION=$VERSION_ID
    else
        echo "Could not determine the distribution."
        exit 1
    fi

    # Install packages based on the distribution
    case "$DISTRO_NAME" in
        ubuntu|debian)
            echo "Ubuntu/Debian detected. Installing packages..."
            echo ""
            install_debian
            ;;
        centos|rhel)
            echo "CentOS/RHEL detected. Installing packages..."
            echo ""
            install_centos
            ;;
        fedora)
            echo "Fedora detected. Installing packages..."
            echo ""
            install_fedora
            ;;
        arch)
            echo "Arch Linux detected. Installing packages..."
            echo ""
            install_arch
            ;;
        *)
            echo "Unsupported or unknown distribution."
            echo ""
            exit 1
            ;;
    esac
}

# Run the installation
install_dependencies

# Completion message
echo ""
echo "Installation completed successfully!"
