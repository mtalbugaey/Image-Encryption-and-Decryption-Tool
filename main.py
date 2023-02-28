from colorama import Fore
import colorama
import getpass
import os
import shutil
import sys
import pyfiglet
from time import sleep
import subprocess
from itertools import cycle
import numpy as np
from operations_AND_algorithms import *
import numpy as np
from PIL import Image


def menu():
    subprocess.run('cls', shell=True)
    ascii_art = pyfiglet.figlet_format("!   I C R Y P T   !")
    print(ascii_art)

    colorama.init(autoreset=True)

    print(Fore.LIGHTCYAN_EX + "[1] RAIL Cipher Encryption/Decryption")
    print(Fore.LIGHTCYAN_EX + "[2] To Text Encryption/Decryption")
    print(Fore.LIGHTCYAN_EX + "[3] Rail Cipher + To Text Encryption/Decryption")
    print(Fore.LIGHTCYAN_EX + "[0] Exit The Program")
    print("")

    while True:
        option = int(input("Enter your option:"))


        if option == 1:
            subprocess.run('cls', shell=True)
            print(Fore.CYAN + pyfiglet.figlet_format("!  RAIL Cipher  !"))
            os.system("python rail_fence_cipher.py")



        elif option == 2:
            subprocess.run('cls', shell=True)
            print(Fore.GREEN + pyfiglet.figlet_format("!  Te x t  !"))
            os.system("python image2text.py")

        elif option == 3:
            subprocess.run('cls', shell=True)
            print(Fore.LIGHTMAGENTA_EX + pyfiglet.figlet_format("!  RAIL & Text  !"))
            os.system("python both.py")

        elif option == 0:
            colorama.init(autoreset=True)
            subprocess.run('cls', shell=True)
            print(pyfiglet.figlet_format("!   I C R Y P T   !"))
            print(pyfiglet.figlet_format("By  Group   6"))
            sleep(0.7)
            print("--CREATED BY:")
            print(Fore.YELLOW + "[*] Juri Alaqeel")
            sleep(0.7)
            print(Fore.YELLOW + "[*] Lulwah Alduwaihi")
            sleep(0.7)
            print(Fore.YELLOW + "[*] Maryam Tariq AlBugaey")
            sleep(0.7)
            print(Fore.YELLOW + "[*] Fatima Husain Abujaid")
            sleep(0.7)
            print(Fore.YELLOW + "[*] Sara Nasser AlSubaie")
            print("\n")
            sleep(0.7)
            print(Fore.YELLOW + "--> Instructor: Mr. Hussain Alattas")

            exit()

        else:
            print("invalid option")

        menu()
        option = int(input("Enter your option:"))

menu()
