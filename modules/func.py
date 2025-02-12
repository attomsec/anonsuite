import random
import json
import subprocess
import modules.macchanger
import modules.run_session
import modules.TorRamJail, modules.verify

def continue_key():

    print("\nPressione uma tecla para continuar...")
    input()

def show_menu():

    while True:

        with open('modules/info.json') as f:
            data = json.load(f)

        subprocess.run(f"clear")
        
        presentation()
        
        print("versão:" ,data['version'])
        print("autor:", data["author"]["name"])
        
        print("\nMenu:\n")
        
        print("Tor Browser:")
        print(51*"-")
        print("1. Run Tor Browser isolated (no audio)")
        print("2. Run Tor Browser isolated with audio (less safe)")
        print(51*"-")
        
        print("\nMac Spoofing:")
        print(51*"-")
        print("3. Change device MAC address")
        print(51*"-")

        print("\nSecure communication:")
        print(51*"-")
        print("4. Run Session App fully isolated (amnesia mode)")
        print(51*"-")

        print("\n0. Sair")
        
        opcao = input("\nconsole: ").strip()
        
        if opcao == "1" or opcao == "2":
            modules.TorRamJail.tor_script_exec(opcao)
        elif opcao == "3":
            modules.macchanger.change_mac()
        elif opcao == "4":
            modules.run_session.session_script_exec()
                        
        elif opcao == "0":
            subprocess.run(f"clear")
            print("Exiting...")
            clean_bash()
            break
        else:
            print("Invalid option. Try again.")

def clean_memory():
    subprocess.run(f"clear", shell=True)
    print("Cleaning shared memory (ram, failsafe)...")
    print("\n")
    subprocess.run("rm -rf /dev/shm/tor-browser/", shell=True)
    print("Status: Clean")

def command_exec(comando):

    try:
        subprocess.run(comando, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"{e}")
        print("\nPressione uma tecla para continuar...")
        input()

def clean_bash():

    print("\nCleaning bash_history file")
    subprocess.run("echo -n > ~/.bash_history", shell=True)
    print("\nStatus: bash_history file cleaned\n")

def presentation():

#     str1 = str('\033[1;32m'+"""
#      **                                 ********         **   **          
#     ****                               **//////         //   /**          
#    **//**   *******   ******  ******* /**        **   ** ** ******  ***** 
#   **  //** //**///** **////**//**///**/*********/**  /**/**///**/  **///**
#  ********** /**  /**/**   /** /**  /**////////**/**  /**/**  /**  /*******
# /**//////** /**  /**/**   /** /**  /**       /**/**  /**/**  /**  /**//// 
# /**     /** ***  /**//******  ***  /** ******** //******/**  //** //******
# //      // ///   //  //////  ///   // ////////   ////// //    //   ////// 
# """)

#     str2 = str('\033[1;32m'+"""
#     #                          #####                        
#    # #   #    #  ####  #    # #     # #    # # ##### ###### 
#   #   #  ##   # #    # ##   # #       #    # #   #   #      
#  #     # # #  # #    # # #  #  #####  #    # #   #   #####  
#  ####### #  # # #    # #  # #       # #    # #   #   #      
#  #     # #   ## #    # #   ## #     # #    # #   #   #      
#  #     # #    #  ####  #    #  #####   ####  #   #   ###### 
                                                            
# """)

#     str3 = str('\033[1;32m'+"""
#    __    _  _  _____  _  _  ___  __  __  ____  ____  ____ 
#   /__\  ( \( )(  _  )( \( )/ __)(  )(  )(_  _)(_  _)( ___)
#  /(__)\  )  (  )(_)(  )  ( \__ \ )(__)(  _)(_   )(   )__) 
# (__)(__)(_)\_)(_____)(_)\_)(___/(______)(____) (__) (____)
# """)

    str4 = str('\033[1;32m'+"""
  ____  ____    ___   ____   _____ __ __  ____  ______    ___ 
 /    ||    \  /   \ |    \ / ___/|  |  ||    ||      |  /  _]
|  o  ||  _  ||     ||  _  (   \_ |  |  | |  | |      | /  [_ 
|     ||  |  ||  O  ||  |  |\__  ||  |  | |  | |_|  |_||    _]
|  _  ||  |  ||     ||  |  |/  \ ||  :  | |  |   |  |  |   [_ 
|  |  ||  |  ||     ||  |  |\    ||     | |  |   |  |  |     |
|__|__||__|__| \___/ |__|__| \___| \__,_||____|  |__|  |_____|
""")

    str5 = str('\033[1;32m'+"""
d s.   d s  b   sSSSs   d s  b   sss. d       b d sss sssss d sss   
S  ~O  S  S S  S     S  S  S S d      S       S S     S     S       
S   `b S   SS S       S S   SS Y      S       S S     S     S       
S sSSO S    S S       S S    S   ss.  S       S S     S     S sSSs  
S    O S    S S       S S    S      b S       S S     S     S       
S    O S    S  S     S  S    S      P  S     S  S     S     S       
P    P P    P   "sss"   P    P ` ss'    "sss"   P     P     P sSSss 
                                                                    
""")

    # str6 = str('\033[1;32m'+"""01000001 01101110 01101111 01101110 01010011 01110101 01101001 01110100 01100101\n""")

#     str7 = str('\033[1;32m'+"""__   __ _   __   __ _  ____  _  _  __  ____  ____ 
#  / _\ (  ( \ /  \ (  ( \/ ___)/ )( \(  )(_  _)(  __)
# /    \/    /(  O )/    /\___ \) \/ ( )(   )(   ) _) 
# \_/\_/\_)__) \__/ \_)__)(____/\____/(__) (__) (____)
# """)

    str8 = str('\033[1;32m'+"""
 ▄▄▄       ███▄    █  ▒█████   ███▄    █   ██████  █    ██  ██▓▄▄▄█████▓▓█████ 
▒████▄     ██ ▀█   █ ▒██▒  ██▒ ██ ▀█   █ ▒██    ▒  ██  ▓██▒▓██▒▓  ██▒ ▓▒▓█   ▀ 
▒██  ▀█▄  ▓██  ▀█ ██▒▒██░  ██▒▓██  ▀█ ██▒░ ▓██▄   ▓██  ▒██░▒██▒▒ ▓██░ ▒░▒███   
░██▄▄▄▄██ ▓██▒  ▐▌██▒▒██   ██░▓██▒  ▐▌██▒  ▒   ██▒▓▓█  ░██░░██░░ ▓██▓ ░ ▒▓█  ▄ 
 ▓█   ▓██▒▒██░   ▓██░░ ████▓▒░▒██░   ▓██░▒██████▒▒▒▒█████▓ ░██░  ▒██▒ ░ ░▒████▒
 ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░░▒▓▒ ▒ ▒ ░▓    ▒ ░░   ░░ ▒░ ░
  ▒   ▒▒ ░░ ░░   ░ ▒░  ░ ▒ ▒░ ░ ░░   ░ ▒░░ ░▒  ░ ░░░▒░ ░ ░  ▒ ░    ░     ░ ░  ░
  ░   ▒      ░   ░ ░ ░ ░ ░ ▒     ░   ░ ░ ░  ░  ░   ░░░ ░ ░  ▒ ░  ░         ░   
      ░  ░         ░     ░ ░           ░       ░     ░      ░              ░  ░
                                                                               
""")

    str9 = str('\033[1;32m'+"""
 █████  ███    ██  ██████  ███    ██ ███████ ██    ██ ██ ████████ ███████ 
██   ██ ████   ██ ██    ██ ████   ██ ██      ██    ██ ██    ██    ██      
███████ ██ ██  ██ ██    ██ ██ ██  ██ ███████ ██    ██ ██    ██    █████   
██   ██ ██  ██ ██ ██    ██ ██  ██ ██      ██ ██    ██ ██    ██    ██      
██   ██ ██   ████  ██████  ██   ████ ███████  ██████  ██    ██    ███████ 
                                                                          
                                                                          
""")

    lista = [str4, str5, str8, str9]
    random.shuffle(lista)
    bem_vindo = random.choice(lista)
    print(bem_vindo)