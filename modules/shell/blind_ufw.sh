#!/bin/bash -p

# Function to detect the distribution
detect_distro() {
    if [ -f /etc/os-release ]; then
        . /etc/os-release
        echo $ID
    else
        echo "unknown"
    fi
}

# Detecting the distribution
DISTRO=$(detect_distro)

clear
echo "AnonSuite is making UFW more secure. Please wait and follow the instructions ahead."
echo ""
# Updating packages based on the distribution
if [[ "$DISTRO" == "ubuntu" || "$DISTRO" == "debian" ]]; then
    echo ""
    echo "Updating packages for Ubuntu/Debian..."
    echo ""
    sudo apt update -y
elif [[ "$DISTRO" == "centos" || "$DISTRO" == "fedora" || "$DISTRO" == "rhel" ]]; then
    echo ""
    echo "Updating packages for CentOS/Fedora/RHEL..."
    echo ""
    sudo yum update -y
else
    echo ""
    echo "Unknown distribution, skipping package update..."
    echo ""
fi

# Installing UFW if not installed based on the distribution
if [[ "$DISTRO" == "ubuntu" || "$DISTRO" == "debian" ]]; then
    echo ""
    echo "Installing UFW..."
    sudo apt install ufw -y
elif [[ "$DISTRO" == "centos" || "$DISTRO" == "fedora" || "$DISTRO" == "rhel" ]]; then
    echo ""
    echo "Updating packages for CentOS/Fedora/RHEL..."
    sudo yum install ufw -y
else
    echo ""
    echo "Unknown distribution, skipping package update..."
fi

# Ask the user for the network interface name


echo "Warning: The current configurations of your firewall will be reset. Before continuing, AnonSuite will create a backup at $HOME/.suite_backups/ufw/"
echo "Anyway, ufw will make own backup."
echo""
mkdir $HOME/.suite_backups
mkdir $HOME/.suite_backups/ufw
sudo cp /etc/ufw/before.rules $HOME/.suite_backups/ufw/ufw_before.rules.bak
sudo cp /etc/ufw/after.rules $HOME/.suite_backups/ufw/ufw_after.rules.bak
sudo cp /etc/ufw/before6.rules $HOME.suite_backups/ufw//ufw_before6.rules.bak
sudo cp /etc/ufw/after6.rules $HOME.suite_backups/ufw//ufw_after6.rules.bak
echo ""
sudo ufw reset
read -p "Please enter your network interface name (e.g., eth0, ens33, wlan0): " NETWORK_INTERFACE

# Setting default policies
clear
echo "--------------------------------------"
echo ""
echo "Setting default UFW policies..."
echo ""
sudo ufw default deny incoming  # Deny all incoming connections by default
sudo ufw default allow outgoing # Allow all outgoing connections

# Allowing necessary traffic
echo "--------------------------------------"
echo ""
echo "Allowing traffic for SSH, HTTP, and HTTPS..."
echo ""
sudo ufw allow ssh           # Allow SSH
sudo ufw allow http          # Allow HTTP
sudo ufw allow https         # Allow HTTPS

# Blocking common attack ports
echo "--------------------------------------"
echo ""
echo "Blocking common attack ports..."
echo ""
sudo ufw deny 21             # FTP
sudo ufw deny 23             # Telnet
sudo ufw deny 25             # SMTP
sudo ufw deny 3306           # MySQL
sudo ufw deny 3389           # RDP

# Enabling UFW logging
echo "--------------------------------------"
echo ""
echo "Disabling UFW logging..."
echo ""
sudo ufw logging off

# Allowing only HTTP/HTTPS outbound traffic on the specified network interface
echo "--------------------------------------"
echo ""
echo "Allowing only outbound HTTP/HTTPS traffic on interface $NETWORK_INTERFACE..."
echo ""
sudo ufw allow out on $NETWORK_INTERFACE to any port 80,443 proto tcp

# Enabling UFW
echo "--------------------------------------"
echo ""
echo "Enabling UFW..."
echo ""
sudo ufw enable

# Checking UFW status
echo "--------------------------------------"
echo ""
echo "UFW Status:"
echo ""
sudo ufw status verbose

echo "UFW configuration completed successfully!"

echo "Press any key to continue..."
input