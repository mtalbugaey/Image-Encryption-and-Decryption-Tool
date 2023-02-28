#image_operations
import base64

def get_image_bytes(image_path):
    """Get the image as bytes"""
    with open(image_path, "rb") as image_file:
        return image_file.read()

def encode_image_bytes(image_bytes):
    """Encode the image bytes to base64"""
    return base64.b64encode(image_bytes)

def decode_image_bytes(base64_bytes):
    """Decode the base64 encoded bytes"""
    return base64.b64decode(base64_bytes)

###################################################

#file_operation
import io
import imghdr
from PIL import Image
import os


def save_credentials_to_files(results):
    """Save the encrypted image and decryption key to a file"""

    with open("encryption.txt", 'w') as file:
        file.write(results['encrypted'])

    with open("decryption_key.txt", 'w') as file:
        file.write(results['decryption_key'])


def read_credentials_from_files():
    encryption_file = open("encryption.txt", 'r')
    decryption_key_file = open("decryption_key.txt", 'r')

    return encryption_file.read(), decryption_key_file.read()


def save_image(base64_bytes, image_name):
    """Save the image to the file"""
    # Decode the base64 string
    image_bytes = base64.b64decode(base64_bytes + b'==')
    # Create a BytesIO object from the image bytes
    image_data = io.BytesIO(image_bytes)
    # detect the image file format
    file_format = imghdr.what(image_data)
    # Open the image file
    image = Image.open(image_data)
    # Save the image to file
    image.save(image_name, format=file_format)

###################################################

#algorithms


import random


def encrypt_encoded_image(base64_bytes):
    """Encrypt the base64 encoded image"""
    encrypted = decryption_key = ""

    string_bytes = base64_bytes.decode('utf-8')
    for i in range(len(string_bytes)):
        char = str(string_bytes)[i]
        if char.isalpha():
            char_ord = ord(char)
            no = random.randint(1, char_ord)

            shifted_char_no = char_ord + no
            encrypted += f'{shifted_char_no}-'
            decryption_key += f'no{no}-'
        else:
            encrypted += f'{char}-'
            decryption_key += f'{char}-'

    # Delete the last dash from the strings.
    encrypted, decryption_key = encrypted[:-1], decryption_key[:-1]

    return {
        'encrypted': encrypted,
        'decryption_key': decryption_key
    }


def decrpyt_encrpyted_image(encrpyted_image, decryption_key):
    """Decrypt the encrypted image with a decryption key"""
    decrypted = ""
    # Get the splitted strings for the decryption key and the encrypted image
    splitted_decryption_key, splitted_encrypted_image = decryption_key.split('-'), encrpyted_image.split('-')

    # Loop through the splitted strings and decrypt the image
    for i in range(len(splitted_decryption_key)):
        char = splitted_encrypted_image[i]
        if (splitted_decryption_key[i].startswith('no')):
            no = int(splitted_decryption_key[i].replace('no', ''))

            shifted_char = chr(int(char) - no)
            decrypted += shifted_char
        else:
            decrypted += splitted_decryption_key[i]
    return bytes(decrypted, 'utf-8')