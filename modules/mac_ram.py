import os
import subprocess
import modules.functions

directory = os.path.expanduser("~/Downloads/mullvad-browser/")
html_file = "modules/html/mac-random.html"
app_id = "mac-ram"

# Function to check if the tor-browser directory exists
def check_directory(directory):

    if os.path.isdir(directory):
        subprocess.run(f"clear", shell=True)
        print(f"Warning: The directory '{directory}' exists.\n")
        mac_ram()
    else:
        print(f"The directory '{directory}' does not exist.")
        print(f"\nWarning: You must extract the Mullvad Browser Tarball in {directory}")
        print("The folder name must be 'mullvad-browser' !!!")
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

def mac_ram():

    # subprocess.run(f"clear", shell=True)

    # Copy the Mullvad directory to RAM
    print("Copying Mullvad Browser to RAM...")
    subprocess.run(f"cp -r {directory} /dev/shm", shell=True)
    subprocess.run(f"cp -r {html_file} /dev/shm", shell=True)
    subprocess.run(f"rm -rf /dev/shm/mullvad-browser/Browser/distribution/*", shell=True)
    print("\nStatus: Completed")

    print("\n")
    print("Running Mullvad Browser (offline) in RAM in failsafe using the firejail command ->")
    print(f"\nfirejail --noprofile --ipc-namespace --machine-id --novideo --nosound --caps.drop=all --private-tmp --net=none /dev/shm/mullvad-browser/Browser/start-mullvad-browser file:///dev/shm/mac-random.html")
    print("\n")
    print("Press enter to execute...")
    input()

    subprocess.run(f"clear", shell=True)

    # Run Mullvad Browser with firejail
    firejail_command = f"firejail --noprofile --ipc-namespace --machine-id --novideo --nosound --caps.drop=all --private-tmp --net=none /dev/shm/mullvad-browser/Browser/start-mullvad-browser file:///dev/shm/mac-random.html"
    modules.functions.command_exec(firejail_command)

    subprocess.run(f"clear", shell=True)

    # Clear shared memory
    modules.functions.clean_memory(app_id)

def mac_ram_script_exec():

    subprocess.run(f"clear", shell=True)

    # directory = os.path.expanduser("~/Downloads/mullvad-browser/")

    check_directory(directory)
