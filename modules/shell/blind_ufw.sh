#!/bin/bash



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
echo ""
read -p "Please enter your network interface name (e.g., eth0, ens33, wlan0): " NETWORK_INTERFACE

# Setting default policies
clear
echo "Setting default UFW policies..."
sudo ufw default deny incoming  # Deny all incoming connections by default
sudo ufw default allow outgoing # Allow all outgoing connections

# Allowing necessary traffic
echo "Allowing traffic for SSH, HTTP, and HTTPS..."
sudo ufw allow ssh           # Allow SSH
sudo ufw allow http          # Allow HTTP
sudo ufw allow https         # Allow HTTPS

# Blocking common attack ports
echo "Blocking common attack ports..."
sudo ufw deny 21             # FTP
sudo ufw deny 23             # Telnet
sudo ufw deny 25             # SMTP
sudo ufw deny 3306           # MySQL
sudo ufw deny 3389           # RDP

# Enabling UFW logging
echo "Enabling UFW logging..."
sudo ufw logging on

# Allowing only HTTP/HTTPS outbound traffic on the specified network interface
echo "Allowing only outbound HTTP/HTTPS traffic on interface $NETWORK_INTERFACE..."
sudo ufw allow out on $NETWORK_INTERFACE to any port 80,443 proto tcp

# Enabling UFW
echo "Enabling UFW..."
sudo ufw enable

# Checking UFW status
echo "UFW Status:"
sudo ufw status verbose

echo "UFW configuration completed successfully!"
