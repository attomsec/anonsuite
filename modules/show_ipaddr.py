from subprocess import run

def get_ip():

    run("clear", shell=True)
    ip = run(["curl", "ifconfig.me"], capture_output=True, text=True)
    result = ip.stdout.strip()
    print(f"Your ip is: {result}")
    print("\nPress enter to return to main menu...")
    input()