import base64
import sys
import os
import subprocess
import rsa_keygen
import userinput
from tkinter import messagebox


def bytes_to_int(b):
    return int.from_bytes(b, byteorder='big')

def int_to_bytes(n):
    return n.to_bytes((n.bit_length() + 7) // 8, byteorder='big')

def opening_key():
    with open('rsa_pubkey.txt', 'r') as f:
        public_key_file = f.read()
    start_marker = '-----BEGIN PUBLIC KEY-----'
    end_marker = '-----END PUBLIC KEY-----'
    start_index = public_key_file.find(start_marker) + len(start_marker)
    end_index = public_key_file.find(end_marker)
    if start_index == -1:
        raise ValueError("Is the provided file a valid public key file ?")
    elif end_index == -1:
        raise ValueError("Is the provided file a valid public key file ?")
    else:
        public_key = public_key_file[start_index:end_index].strip()
    decoded_pubkey = str(base64.b64decode(public_key).decode("utf-8"))
    n, e = decoded_pubkey.split('_')
    n = int(n)
    e = int(e)
    tab = [n, e]
    return tab

def encrypt(message, n, e):
    message_int = bytes_to_int(message.encode("utf-8"))
    cipher_int = pow(message_int, e, n)
    cipherchar = base64.b64encode(int_to_bytes(cipher_int))
    return cipherchar.decode()


def main():
        rsa_keygen.generate_key_pair()
        tab = opening_key()
        n = tab[0]
        e = tab[1]
        message = userinput.main()
        cipherchar = ""
        ciphertext = ""
        charlist = list(message)
        encrypted_file = open("rsa_encrypted.txt", "w+")
        for character in charlist:
            cipherchar = encrypt(character, n, e)
            ciphertext += cipherchar
        encrypted_file.write(ciphertext)