from operations_AND_algorithms import *
from colorama import Fore
import colorama
from time import sleep


def encrpyt_image(image_path):
    """Encrypt an image"""
    try:
        # Combine the functions from the other files
        image_bytes = get_image_bytes(image_path)
        encoded = encode_image_bytes(image_bytes)
        results = encrypt_encoded_image(encoded)
        save_credentials_to_files_1(results)

        print("The image has been encrypted and saved to the files " + Fore.GREEN + "encryption.txt " + Fore.WHITE + "and " + Fore.GREEN + "decryption_key.txt")
        sleep(4)
    except Exception as e:
        print(Fore.LIGHTRED_EX + "An error occured while encrypting the image: " + str(e))
        sleep(2)


def decrppt_image():
    try:
        encrypted, decryption_key = read_credentials_from_files()
        decrypted = decrpyt_encrpyted_image(encrypted, decryption_key)
        save_image(decrypted, 'out.png')
        print("The image has been decrypted and saved to the file" + Fore.GREEN + " out.png")
        sleep(3)
    except Exception as e:
        print(Fore.LIGHTRED_EX + "An error occured while decrypting the image: " + str(e))
        sleep(2)


def save_credentials_to_files_1(results):
    """Save the encrypted image and decryption key to a file"""
    dirname = input("Enter the name of the folder where you want to save the results: ")
    dirpath = os.path.join(dirname)
    os.makedirs(dirpath)
    os.chdir(dirname)
    with open("encryption.txt", 'w') as file:
        file.write(results['encrypted'])

    with open("decryption_key.txt", 'w') as file:
        file.write(results['decryption_key'])


def main():
    mode = input('Do you want to encrypt or decrypt the image [E/D]? ')

    if mode == 'e' or mode == 'E':
        path = input("Please enter image filename you want to encrypt:")
        encrpyt_image(path)

    elif mode == 'd' or mode == 'D':
        enFolder = input("Enter the filename that contains the encrypted image:")
        os.chdir(enFolder)

        you_sure = input("Do you have the encrypted and decryption_key files in the same directory? (y/n): ")

        if (you_sure != "y"):
            print("Please make sure you have the files in the same directory as this script and try again!")
            return
        decrppt_image()

    else:
        print(Fore.LIGHTRED_EX + "Invalid option!")


if __name__ == '__main__':
    main()
