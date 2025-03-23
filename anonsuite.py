import json
import os
import time

from modules import functions
import subprocess

def main():

    # Abre o arquivo info.json
    with open("modules/json/info.json") as info:
        data = json.load(info)

    try:
        functions.splash_screen()

        while True:
            functions.show_menu(data)
            functions.cmd_console()
    except Exception:
        os.system("clear")
        print("!!! Error. Exiting. !!!")
        time.sleep(2)
        functions.clean_bash()


if __name__ == "__main__":
    main()