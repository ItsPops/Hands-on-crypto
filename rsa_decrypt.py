import base64
import sys
from tkinter import filedialog


def open_encrypted_file():
            file_path = filedialog.askopenfilename(filetypes=[('Encrypted file', '*.txt')])
            with open(file_path, 'r') as fichier:
                content = fichier.read()
                return content
            

def open_private_key():
            file_path = filedialog.askopenfilename(filetypes=[('Private key', '*.txt')])
            with open(file_path, 'r') as f:
                content = f.read()
                return content
                

# Convert a byte string to an integer
def bytes_to_int(b):
    return int.from_bytes(b, byteorder='big')


# Convert an integer to a byte string
def int_to_bytes(n):
    return n.to_bytes((n.bit_length() + 7) // 8, byteorder='big')


# Decryption function
def decrypt(fichier, n, d):
    ciphertext = fichier
    plaintext = b""
    for i in range(0, len(ciphertext), 12):
        substring = ciphertext[i:i+44]
        cipher_int = bytes_to_int(base64.b64decode(substring.encode()))
        message_int = pow(cipher_int, d, n)
        message_bytes = int_to_bytes(message_int)
        plaintext += message_bytes
    with open("rsa_decrypted.txt", 'w') as f:
        f.write(plaintext.decode())
    print("Le message original est: " + plaintext.decode())

def main():
    fichier = open_encrypted_file()
    private_key_file = open_private_key()
    start_marker = '-----BEGIN PRIVATE KEY-----'
    end_marker = '-----END PRIVATE KEY-----'
    start_index = private_key_file.find(start_marker) + len(start_marker)
    end_index = private_key_file.find(end_marker)
    if start_index == -1:
        raise ValueError("Is the provided file a valid private key file ?")
    elif end_index == -1:
        raise ValueError("Is the provided file a valid private key file ?")
    else:
        private_key = private_key_file[start_index:end_index].strip()
    decoded_privkey = str(base64.b64decode(private_key).decode("utf-8"))
    n, d = decoded_privkey.split('_')
    n = int(n)
    d = int(d)
    decrypt(fichier, n, d)

