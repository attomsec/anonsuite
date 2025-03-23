import os
import subprocess
import time
import modules.functions

directory = os.path.expanduser("~/Downloads/tor-browser/")
app_id = "tor-browser"

# Function to check if the tor-browser directory exists
def check_directory(directory, option):

    if os.path.isdir(directory):
        os.system("clear")
        print(f"Warning: The directory '{directory}' exists.\n")
        ram_jail(option)
    else:
        print(f"The directory '{directory}' does not exist.")
        print(f"\nWarning: You need to extract the Tor Browser Tarball in {directory}")
        print("The folder name must be 'tor-browser' !!!")
        print("\n")
        print("Press any key to return to the menu...")
        input()

def display_file(file):

    if os.path.exists(file):
        with open(file, 'r') as file:
            print(file.read())
    else:
        print(f"The file {file} does not exist.")

def command_exec(command):

    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"{e}")
        print("\nPress any key to continue...")
        input()

def ram_jail(option):

    option = option

    print("Insert a never used different vendor MAC address to improve anonymity")
    print('\033[1;90m' + "\nTip: You can generate a MAC address with AnonSuite. Check menu." + '\033[1;97m')
    mac = input("\nNew mac: ")
    print(f"\nChosen MAC: {mac}")

    print("\nChoose network interface to be used by Firejail")
    interface = input("\nInterface: ")
    print(f"\nChosen interface: {interface}\n")
    time.sleep(1)

    # Copy the Tor directory to RAM
    print("\nCopying Tor Browser to RAM...")
    subprocess.run(f"cp -r {directory} /dev/shm", shell=True)
    print("\nStatus: Completed")
    time.sleep(1)

    os.system("clear")

    if option == "1":
        print("Running Tor Browser (no audio) in RAM in failsafe mode with the command:")
        print(f"\nfirejail --noprofile --ipc-namespace --machine-id --novideo --nosound --caps.drop=all --private-tmp --net={interface} --mac={mac} /dev/shm/tor-browser/Browser/start-tor-browser;")
        print("\n")
        print("Press enter to execute...")
        input()

        os.system("clear")

        # Run the Tor Browser with firejail
        firejail_command = f"firejail --noprofile --ipc-namespace --machine-id --novideo --nosound --caps.drop=all --private-tmp --net={interface} --mac={mac} /dev/shm/tor-browser/Browser/start-tor-browser"
        modules.functions.command_exec(firejail_command)

    elif option == "2":
        print("Running Tor Browser (with audio) in RAM in failsafe mode with the command:")
        print(f"\nfirejail --noprofile --ipc-namespace --machine-id --caps.drop=all --private-tmp --net={interface} --mac={mac} /dev/shm/tor-browser/Browser/start-tor-browser;")
        print("\n")
        print("Press enter to execute...")
        input()

        os.system("clear")

        # Run the Tor Browser with firejail
        firejail_command = f"firejail --noprofile --ipc-namespace --machine-id --caps.drop=all --private-tmp --net={interface} --mac={mac} /dev/shm/tor-browser/Browser/start-tor-browser"
        command_exec(firejail_command)
    else:
        print("Invalid option")

    os.system("clear")

    # Clear shared memory
    modules.functions.clean_memory(app_id)

def tor_script_exec(option):

    os.system("clear")

    # directory = os.path.expanduser("~/Downloads/tor-browser/")

    check_directory(directory, option)
