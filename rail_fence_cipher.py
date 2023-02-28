import getpass
import os
from colorama import Fore
import colorama
import random
from time import sleep
import sys
from itertools import cycle
try:
    import numpy as np
    from PIL import Image
except ModuleNotFoundError:
    print('Enter the command: pip install numpy pillow')
    sleep(2)
    sys.exit()


class ImageCrypt():
    def __init__(self, password):
        self.password = password

    def encrypt(self, filename):
        new_filename = self.new_filename('e', filename)
        if new_filename is None:
            print(Fore.LIGHTRED_EX + f'Error: file {new_filename} already exists')
            sleep(2)
        else:
            try:
                im = Image.open(filename)
                encrypted = self.get_pixels(im)
                numbers = self.password_to_numbers(self.password)
                for i in progress_bar(numbers, 'Encryption: '):
                    encrypted = self.rail_fence_encrypt(encrypted, i)
                self.create_and_save_image(encrypted, im.width, im.height, new_filename)
                print("Encrypted image saved as " + Fore.GREEN + new_filename)
                sleep(3)
            except FileNotFoundError as error:
                print(error)
                sleep(2)
                return

    def decrypt(self, filename):
        new_filename = self.new_filename('d', filename)
        if new_filename is None:
            print(Fore.LIGHTRED_EX + f'Error: file {new_filename} already exists')
            sleep(2)
        else:
            try:
                im = Image.open(filename)
                decrypted = self.get_pixels(im)
                numbers = self.password_to_numbers(self.password[::-1])
                for i in progress_bar(numbers, 'Decryption: '):
                    decrypted = self.rail_fence_decrypt(decrypted, i)

                self.create_and_save_image(decrypted, im.width, im.height, new_filename)
                colorama.init(autoreset=True)
                print("Decrypted image saved as " + Fore.GREEN + new_filename)
                sleep(3)
            except FileNotFoundError as error:
                print(error)
                sleep(3)
                return

    @staticmethod
    def get_pixels(im):
        print('Scanning...')
        colors = []
        for x in range(im.width):
            for y in range(im.height):
                color = im.getpixel((x, y))
                colors.append(color)
        return colors

    @staticmethod
    def password_to_numbers(password):
        numbers = [ord(i) for i in password]
        return numbers

    def rail_fence_encrypt(self, plaintext, rails):
        p = self.rail_pattern(rails)
        return sorted(plaintext, key=lambda i: next(p))

    def rail_fence_decrypt(self, ciphertext, rails):
        p = self.rail_pattern(rails)
        indexes = sorted(range(len(ciphertext)), key=lambda i: next(p))
        result = [''] * len(ciphertext)
        for i, c in zip(indexes, ciphertext):
            result[i] = c
        return result

    @staticmethod
    def rail_pattern(n):
        r = list(range(n))
        return cycle(r + r[-2:0:-1])

    @staticmethod
    def new_filename(mode, filename):
        new_filename = f'{filename[:len(filename) - 4]}-{mode}.png'
        if os.path.exists(new_filename):
            return None
        else:
            return new_filename

    @staticmethod
    def create_and_save_image(colors, width, height, filename):
        dirname = input("Enter the name of the folder where you want to save the results: ")
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


def progress_bar(it, prefix='', size=60, out=sys.stdout):
    count = len(it)

    def show(j):
        x = int(size*j/count)
        print(f"{prefix}[{u'='*x}{('·'*(size-x))}]", end='\r', file=out, flush=True)
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    print('', flush=True, file=out)



def main():
            colorama.init(autoreset=True)

            mode = input('Do you want to encrypt or decrypt the image [E/D]? ')
            if mode == 'e' or mode == 'E':
                filename = input('Enter image filename: ')
                password = getpass.getpass(prompt='Enter the password that will be used in the encryption process (at least 8 digits): ', stream=None)
                if len(password) >= 8 and password.isdigit():
                    ImageCrypt(password).encrypt(filename)

                else:
                    print(Fore.LIGHTRED_EX + 'Error: minimum password length: 8')
                    sleep(2)

            else:

                enFolder=input("Enter the filename that contains the encrypted image:")
                password = getpass.getpass(prompt='Enter the password that was used in the encryption process (at least 8 digits): ', stream=None)
                os.chdir(enFolder)

                # This will get the current file's directory
                # Path of the current file
                #print(os.getcwd())

                dir_path = enFolder

                # To get the parent directory of this file
                parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))

                a = os.listdir(os.getcwd())
                a = str(a)
                a = a[2:-2]

                # To get the specific file
                #file_name = 'out.png'  # File Name
                #file_loc = os.path.join(parent_dir_path, a)  # Complete file name with path

                ImageCrypt(password).decrypt(a)

            return



if __name__ == '__main__':
    main()

