import os
from subprocess import run

def get_ip():

    os.system("clear")
    ip = run(["curl", "ifconfig.me"], capture_output=True, text=True)
    result = ip.stdout.strip()
    print(f"Your ip is: {result}")
    print("\nPress enter to return to main menu...")
    input()