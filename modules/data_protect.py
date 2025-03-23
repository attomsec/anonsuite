import getpass
import os  # Manipulação de diretórios e arquivos
import base64  # Codificação/decodificação da chave
import subprocess
import time

import cryptography.fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC  # Derivação da chave da passphrase
from cryptography.hazmat.primitives import hashes  # Algoritmos de hash (SHA256)
from cryptography.hazmat.backends import default_backend  # Backend para PBKDF2HMAC
from cryptography.fernet import Fernet  # Criptografia e descriptografia com Fernet

def protect_data(opt):

    if opt == "encrypt":
        os.system("clear")
        print('\033[1;31m' + "Warning:" + '\033[0;33m' + "\n\nAnonSuite will encrypt all files within the directory you specify. You should place all the files you want to encrypt in a dedicated folder." + '\033[0;97m')

    if opt == "decrypt":
        os.system("clear")
        print('\033[1;31m' + "Warning:" + '\033[0;33m' + "\n\nAnonSuite will decrypt all files within the directory you specify. You should place all the files you want to encrypt in a dedicated folder." + '\033[0;97m')

    path = str(input("\n\nInsert directory path: "))

    if os.path.isdir(path):

        if opt == "encrypt":
            os.system("clear")
            encrypt_directory(path)
        if opt == "decrypt":
            os.system("clear")
            decrypt_file(path)
    else:
        print("\nInvalid path. Try again.")
        time.sleep(2)
        return protect_data(opt)

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
    passphrase = getpass.getpass("\nInsert a strong password: ")
    passphrase_confirm = getpass.getpass("Confirm password: ")
    abort = False

    if passphrase == passphrase_confirm:

        salt = os.urandom(16)
        key = generate_key_from_passphrase(passphrase, salt)
        b64_key = base64.urlsafe_b64encode(key)
        cipher = Fernet(b64_key)

        os.system("clear")
        option = input('\033[1;31m' + "Warning:" + '\033[0;33m' + "\n\nThis action is irreversible. Do you wish to continue? (y/N)" + '\033[0;97m')
        print("")

        if option.lower() == "y":
            for root, dirs, files in os.walk(path):

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
                    print(f"The {file_path} was encrypted. Is now {new_file_path}")
        else:
            print("")
            print("Aborting...")
            print("\nYour data was not encrypted and still unsafe!\n\nPress enter to return to main menu...")
            input()
            abort = True
    else:
        print("\nPassword not match! Try again.")
        time.sleep(2)
        os.system("clear")
        return protect_data("encrypt")

    if not abort:
        print("\nYour data is now encrypted! Keep your password safe. Stay anon.")
        print("\n\nPress enter to return to main menu...")
        input()

def decrypt_file(path: str):

    path = path
    os.system("clear")
    passphrase = getpass.getpass("Insert your password: ")
    print("")
    try:
        for root, dirs, files in os.walk(path):
            for fi in files:
                file_path = os.path.join(root, fi)
                with open(file_path, 'rb') as f:
                    salt = f.read(16)
                    encrypted_data = f.read()

                key = generate_key_from_passphrase(passphrase, salt)
                b64_key = base64.urlsafe_b64encode(key)
                cipher = Fernet(b64_key)
                decrypted_data = cipher.decrypt(encrypted_data)

                with open(file_path, 'wb') as f:
                    f.write(decrypted_data)

                new_file_path = file_path[:-9]
                os.rename(file_path, new_file_path)
                print(f"The {file_path} was decrypted. Is now {new_file_path}")

    except (cryptography.fernet.InvalidToken, TypeError):
        print("Invalid password ! Please try again.")
        time.sleep(2)
        return decrypt_file(path)

    print("\n\nPress enter to return to the main menu.")
    input()

