import os
import subprocess
import modules.functions


def change_mac():
    subprocess.run(f"clear", shell=True)

    mac = input("Enter the desired MAC: ")
    print(f"\nThe chosen MAC was: {mac}\n")

    interface = input("Enter the network interface to change the MAC: ")

    print("\nWarning: You will be asked for the user's password to allow macchanger execution!")

    print("\nChanging MAC with macchanger using the command>")
    print(f"\nsudo macchanger --mac={mac} {interface}")

    change_command = f"sudo macchanger --mac={mac} {interface}"
    print("\n")
    try:
        modules.functions.command_exec(change_command)
    except subprocess.CalledProcessError as e:
        print("Error trying to change the MAC: " + f"\n{e}")
