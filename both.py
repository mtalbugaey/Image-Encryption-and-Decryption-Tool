import getpass
import os
import shutil
import sys
from itertools import cycle
import numpy as np
from operations_AND_algorithms import *
from colorama import Fore
import colorama
from time import sleep


class rail_fence():
    colorama.init(autoreset=True)
    def __init__(self, password):
        self.password = password

    def encrypt(self, filename):

        colorama.init(autoreset=True)

        new_filename = self.new_filename('rail_fence_encrypt', filename)
        if new_filename is None:
            print(Fore.LIGHTRED_EX + f'Error: file {new_filename} already exists')
            sleep(3)
        else:
            try:
                im = Image.open(filename)
                encrypted = self.get_pixels(im)
                numbers = self.password_to_numbers(self.password)
                for i in progress_bar(numbers, 'Encryption: '):
                    encrypted = self.rail_fence_encrypt(encrypted, i)
                self.create_and_save_image(encrypted, im.width, im.height, new_filename)
                print("Encrypted image saved as " + Fore.GREEN + new_filename)
            except FileNotFoundError as error:
                print(error)
                sleep(3)
                return

    def decrypt(self, filename,file_loc):
            colorama.init(autoreset=True)

            #################3
            new_filename = self.new_filename('d', filename)
            if new_filename is None:
                print(Fore.LIGHTRED_EX + f'Error: file {new_filename} already exists')
                sleep(3)
            else:
                try:

                    im = Image.open(filename)
                    decrypted = self.get_pixels(im)
                    numbers = self.password_to_numbers(self.password[::-1])
                    for i in progress_bar(numbers, 'Decryption: '):
                        decrypted = self.rail_fence_decrypt(decrypted, i)
                    self.create_and_save_image(decrypted, im.width, im.height, new_filename)
                    shutil.move(file_loc, os.getcwd())
                    print("Decrypted image saved as " + Fore.GREEN + new_filename)

                except FileNotFoundError as error:
                    print(error)
                    sleep(3)
                    return

    @staticmethod
    def get_pixels(im):
        colorama.init(autoreset=True)
        print('Scanning...')
        colors = []
        for x in range(im.width):
            for y in range(im.height):
                color = im.getpixel((x, y))
                colors.append(color)
        return colors

    @staticmethod
    def password_to_numbers(password):
        colorama.init(autoreset=True)
        numbers = [ord(i) for i in password]
        return numbers

    def rail_fence_encrypt(self, plaintext, rails):
        colorama.init(autoreset=True)
        p = self.rail_pattern(rails)
        return sorted(plaintext, key=lambda i: next(p))

    def rail_fence_decrypt(self, ciphertext, rails):
        colorama.init(autoreset=True)
        p = self.rail_pattern(rails)
        indexes = sorted(range(len(ciphertext)), key=lambda i: next(p))
        result = [''] * len(ciphertext)
        for i, c in zip(indexes, ciphertext):
            result[i] = c
        return result

    @staticmethod
    def rail_pattern(n):
        colorama.init(autoreset=True)
        r = list(range(n))
        return cycle(r + r[-2:0:-1])

    @staticmethod
    def new_filename(mode, filename):
        colorama.init(autoreset=True)
        new_filename = f'{filename[:len(filename) - 4]}-{mode}.png'
        if os.path.exists(new_filename):
            return None
        else:
            return new_filename

    @staticmethod
    def create_and_save_image(colors, width, height, filename):
        colorama.init(autoreset=True)
        dirname = input("Enter the name of the file where you want to save the results: ")
        dirpath = os.path.join(dirname)
        os.makedirs(dirpath)
        os.chdir(dirname)
        print('Creation...')
        im = Image.new('RGB', (width, height))
        image_array = np.array(im)
        i = 0
        for x in range(width):
            for y in range(height):
                r = colors[i][0]
                g = colors[i][1]
                b = colors[i][2]
                image_array[y][x] = (r, g, b)
                i += 1
        new_image = Image.fromarray(image_array, 'RGB')
        new_image.save(filename)

class image_to_text():
    def __init__(self):
        pass

    def encrpyt_image(self,image_path):
        colorama.init(autoreset=True)
        """Encrypt an image"""
        try:
            # Combine the functions from the other files

            image_bytes = get_image_bytes(image_path)
            encoded = encode_image_bytes(image_bytes)
            results = encrypt_encoded_image(encoded)
            save_credentials_to_files(results)

            print(Fore.WHITE + "The image has been encrypted and saved to the files " + Fore.GREEN + "encryption.txt " + Fore.WHITE + "and " + Fore.GREEN + "decryption_key.txt")
            sleep(3)

        except Exception as e:
            print(Fore.LIGHTRED_EX + "An error occured while encrypting the image: " + str(e))
            sleep(3)

    def decrppt_image(self):
        colorama.init(autoreset=True)
        try:
            encrypted, decryption_key = read_credentials_from_files()
            decrypted = decrpyt_encrpyted_image(encrypted, decryption_key)
            save_image(decrypted, 'out.png')
            print("The image has been decrypted and saved to the file" + Fore.GREEN + " out.png")
            sleep(3)
        except Exception as e:
            print(Fore.LIGHTRED_EX + "An error occured while decrypting the image: " + str(e))
            sleep(3)






def progress_bar(it, prefix='', size=60, out=sys.stdout):
    count = len(it)

    def show(j):
        x = int(size * j / count)
        print(f"{prefix}[{u'=' * x}{('·' * (size - x))}]", end='\r', file=out, flush=True)

    show(0)
    for i, item in enumerate(it):
        yield item
        show(i + 1)
    print('', flush=True, file=out)


def main():

            mode = input('Do you want to encrypt or decrypt the image [E/D]? ')
            if mode == 'e' or mode == 'E':
                filename = input('Enter image filename: ')
                password = getpass.getpass(prompt='Enter the password that will be used in the encryption process (at least 8 digits): ', stream=None)
                if len(password) >= 8 and password.isdigit():
                    rail_fence(password).encrypt(filename)
                    a = os.listdir(os.getcwd())
                    a = str(a)
                    a = a[2:-2]
                    #print("a is:  "+a)
                    image_to_text().encrpyt_image(a)
                else:
                    print(Fore.LIGHTRED_EX + 'Error: minimum password length: 8')
                    sleep(3)

            else:

                enFolder=input("Enter the filename that contains the encrypted image:")
                password = getpass.getpass(prompt='Enter the password that was used in the encryption process (at least 8 digits): ', stream=None)
                os.chdir(enFolder)
                image_to_text().decrppt_image()

                # This will get the current file's directory
                # Path of the current file
                #print(os.getcwd())

                dir_path = enFolder

                # To get the parent directory of this file
                parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))

                # To get the specific file
                file_name = 'out.png'  # File Name
                file_loc = os.path.join(parent_dir_path, file_name)  # Complete file name with path

                rail_fence(password).decrypt('out.png', file_loc)

            return



if __name__ == '__main__':
    main()

