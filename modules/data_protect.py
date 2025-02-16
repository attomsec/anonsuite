import os  # Manipulação de diretórios e arquivos
import base64  # Codificação/decodificação da chave
import subprocess
import time

from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC  # Derivação da chave da passphrase
from cryptography.hazmat.primitives import hashes  # Algoritmos de hash (SHA256)
from cryptography.hazmat.backends import default_backend  # Backend para PBKDF2HMAC
from cryptography.fernet import Fernet  # Criptografia e descriptografia com Fernet
import hashlib  # Para criar hashes como SHA256
import shutil  # (Opcional) Para cópia/movimentação de arquivos

def protect_data(opt):

    if opt == "encrypt":
        subprocess.run("clear", shell=True)
        print('\033[1;31m' + "Warning:" + '\033[0;33m' + "\n\nAnonSuite will encrypt all files within the directory you specify. You should place all the files you want to encrypt in a dedicated folder." + '\033[0;97m')

    if opt == "decrypt":
        subprocess.run("clear", shell=True)
        print('\033[1;31m' + "Warning:" + '\033[0;33m' + "\n\nAnonSuite will decrypt all files within the directory you specify. You should place all the files you want to encrypt in a dedicated folder." + '\033[0;97m')

    path = str(input("\n\nInsert directory path: "))

    if path == "":
        print("\nInvalid path. Try again.")
        time.sleep(2)
        protect_data(opt)

    if os.path.isdir(path):

        if opt == "encrypt":
            subprocess.run("clear", shell=True)
            encrypt_directory(path)
        if opt == "decrypt":
            subprocess.run("clear", shell=True)
            decrypt_file(path)
    else:
        print("\nInvalid path. Try again.")
        time.sleep(2)
        protect_data(opt)

def generate_key_from_passphrase(passphrase: str, salt: bytes) -> bytes:

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=300000,
        backend=default_backend()
    )
    return kdf.derive(passphrase.encode())


def encrypt_directory(path: str):

    path = path
    passphrase = str(input("\nInsert a strong password: "))
    passphrase_confirm = str(input("Confirm password: "))

    if passphrase == passphrase_confirm:

        salt = os.urandom(16)
        # b64_salt = base64.urlsafe_b64encode(salt)
        key = generate_key_from_passphrase(passphrase, salt)
        b64_key = base64.urlsafe_b64encode(key)
        cipher = Fernet(b64_key)
        # salt_config = str(os.path.join(os.path.expanduser('~'), ".suite", ".crypt", "salt_config.txt"))

        for root, dirs, files in os.walk(path):

            subprocess.run("clear", shell=True)
            option = input('\033[1;31m' + "Warning:" + '\033[0;33m' + "\n\nThis action is irreversible. Do you wish to continue? (y/N)" + '\033[0;97m')
            print("")

            if option == "y" or option == "Y":

                for fi in files:
                    file_path = os.path.join(root, fi)

                    with open(file_path, 'rb') as fp:
                        file_data = fp.read()

                    encrypted_data = cipher.encrypt(file_data)
                    encrypted_file_data = salt + encrypted_data

                    with open(file_path, 'wb') as encrypted_file:
                        encrypted_file.write(encrypted_file_data)

                    # new_file = str(file_path)
                    new_file_path = file_path + ".AnonData"
                    os.rename(file_path, new_file_path)
                    print(f"The {file_path} was encrypted.")
            else:
                subprocess.run("clear", shell=True)
                print("Aborting...\nPress enter to return to main menu...")
                break

            print("\nYour data is safe now!\n\nPress enter to return to main menu...")

        # with open(salt_config, 'r') as file:
        #     data = file.read()


        # b64_salt_str = b64_salt.decode('utf-8')

        # subprocess.run('sudo rm -rf suite/lock.img', shell=True)
        input()
    else:
        print("\nPassword not match! Try again.")
        time.sleep(2)
        subprocess.run("clear", shell=True)
        protect_data("encrypt")

def decrypt_file(path: str):

    path = path
    passphrase = str(input("Insert your password: "))
    print("")

    for root, dirs, files in os.walk(path):
        for fi in files:
            file_path = os.path.join(root, fi)
            with open(file_path, 'rb') as f:
                salt = f.read(16)
                encrypted_data = f.read()

            # b64_salt = base64.urlsafe_b64decode(salt)
            key = generate_key_from_passphrase(passphrase, salt)
            b64_key = base64.urlsafe_b64encode(key)
            cipher = Fernet(b64_key)
            decrypted_data = cipher.decrypt(encrypted_data)
    # b64_salt_str = salt_data
            with open(file_path, 'wb') as f:
                f.write(decrypted_data)

            new_file_path = file_path[:-9]
            os.rename(file_path, new_file_path)
            print(f"The {file_path} was decrypted.")

    # with open(anon_img, 'rb') as file:
    #     crypt_data = file.read()
    print("\nYour files are unprotected.\n\nPress enter to return to the main menu.")
    # chamar função de montar a imagem no diretorio seguro na home
    # subprocess.run('sudo rm -rf suite/lock.img.anon', shell=True)
    input()

