import os
import subprocess
import time
import modules.functions

def session_script_exec():

    directory = os.path.expanduser("~/Downloads/session/session.AppImage")
    check_directory(directory)

def run_session():

    print('\033[1;31m' + "Warning:" + '\033[0;33m' + " Session will run in amnesia mode. This means that once you close the app, everything will be permanently deleted! Make sure to back up your recovery key or you won't be able to recover your account (if needed)" + '\033[0;97m')
    print('\n\033[1;32m' + "Notice:" + '\033[0;33m' + " Session operates on an encrypted Onion routing system, similar to the Tor network. However, it is recommended to use a 'trusted VPN' to prevent your internet service provider from knowing that you are using Session. This is similar to what we do on the Tor network when using Bridges." + '\033[0;97m')
    modules.functions.continue_key()

    print("Insert a never used different vendor MAC address to improve anonymity")
    print('\033[1;90m' + "\nTip: You can generate a MAC address with AnonSuite. Check menu." + '\033[1;97m')
    mac = input("\nNew mac: ")
    print(f"\nChosen MAC: {mac}\n")
    time.sleep(1)

    print("\nChoose network interface to be used by Firejail")
    interface = input("\nInterface: ")
    print("\nChosen interface: " + interface)
    time.sleep(1)

    subprocess.run(f"clear", shell=True)

    print("Running Session App in amnesia mode in RAM in failsafe using the command:")
    print(f"\nfirejail --noprofile --private --private-tmp --ipc-namespaces --nosound --novideo --net={interface} --mac={mac} --appimage ~/Downloads/session/session.AppImage")
    print("\n")
    print("Press enter to execute...")
    input()

    command = f"firejail --noprofile --private --private-tmp --ipc-namespaces --nosound --novideo --net={interface} --mac={mac} --appimage ~/Downloads/session/session.AppImage"
    modules.functions.command_exec(command)

    subprocess.run(f"clear", shell=True)
    print("Session App " + '\033[1;31m' + "killed." + '\033[0;97m' + " Contracted amnesia.")
    time.sleep(3)

def check_directory(directory):

    if os.path.isfile(directory):
        subprocess.run(f"clear", shell=True)
        print(f"Status: The directory '{directory}' exists.\n")
        run_session()
    else:
        subprocess.run(f"clear", shell=True)
        print(f"The directory '{directory}' does not exist.")
        print("\nWarning: You must copy the Session AppImage to /home/your_user/Downloads/session/ !!!")
        print("The folder name containing the AppImage must be 'session' !!!")
        print("\n")
        print("Press any key to return to the menu...")
        input()
