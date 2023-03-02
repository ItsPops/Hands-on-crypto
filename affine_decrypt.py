import string
import random
from tkinter import filedialog

def open_encrypted_file():
            file_path = filedialog.askopenfilename(filetypes=[('Encrypted file', '*.txt')])
            with open(file_path, 'r') as fichier:
                content = fichier.read()
                return content
            

def open_key_a():
            file_path = filedialog.askopenfilename(filetypes=[('Key A', '*.txt')])
            with open(file_path, 'r') as f:
                key_a = f.read()
                return key_a


def open_key_b():
            file_path = filedialog.askopenfilename(filetypes=[('Key B', '*.txt')])
            with open(file_path, 'r') as f:
                key_b = f.read()
                return key_b
            
                
def inverse(a):
    c=0
    while (a*c%101!=1):
        c=c+1
    return c

def decrypt_affine(ciphertext, a, b):
    plaintext = ""
    n = len(string.printable)  # nombre total de caractères imprimables
    a_inv = inverse(a)  # inverse modulaire de a
    for char in ciphertext:
        if char in string.printable:
            y = string.printable.index(char)
            x = (a_inv * (y - b)) % n
            plaintext += string.printable[x]
        else:
            plaintext += char
    return plaintext

def decrypt():
    string.printable += '@'
    m = len(string.printable)
    message = str(open_encrypted_file())
    a = open_key_a()
    b = open_key_b()
    a = int(a)
    b = int(b)
    plaintext = decrypt_affine(message, a, b)
    print("Message chiffré : ", message)
    print("Message déchiffré : ", plaintext)
    with open("affine_decrypted.txt", 'w+') as f:
        f.write(plaintext)