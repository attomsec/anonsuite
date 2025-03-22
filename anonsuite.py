from modules import functions
import subprocess

def main():

    subprocess.run("clear", shell=True)
    print("Initializing... \n")
    print("Welcome to " + '\033[1;32m' + "AnonSuite" + '\033[0;97m')
    print('\033[1;31m' + "\nWarning: "+ '\033[0;97m' + "From the main menu, run the 'install dependencies' command to install all required dependencies.")
    functions.continue_key()


    while True:
        functions.show_menu()
        functions.cmd_console()

if __name__ == "__main__":
    main()