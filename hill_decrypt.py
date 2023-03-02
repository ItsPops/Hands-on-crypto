from tkinter import filedialog, simpledialog, messagebox
import tkinter as tk
import sys
# def open_encrypted_file():
#             file_path = filedialog.askopenfilename(filetypes=[('Hill encrypted file', '*.txt')])
#             with open(file_path, 'r') as fichier:
#                 content = fichier.read()
#                 return content
            

# def open_private_key():
#             file_path = filedialog.askopenfilename(filetypes=[('Private key', '*.pem')])
#             with open(file_path, 'r') as f:
#                 content = f.read()
#                 return content
            


def input_cipher_text():
    root = tk.Tk()
    root.withdraw()
    message = simpledialog.askstring("Saisir le message chiffré", "Saisissez le message chiffré (ciphertext) :", parent=root)
    if len(message) == 0:
        messagebox.showerror("Erreur", "Le message ne peut  être vide.")
        sys.exit(1)
    return message



import tkinter as tk
from tkinter import simpledialog, messagebox
import sys
import ast

def input_matrix_key():
    root = tk.Tk()
    root.withdraw()
    while True:
        message = simpledialog.askstring("Saisir la clé", "Saisissez la matrice clé (au format [[x1, y1], [x2, y2]]):", parent=root)
        if message is None:
            sys.exit(1)
        try:
            matrix = ast.literal_eval(message)
            if len(matrix) != 2 or len(matrix[0]) != 2 or len(matrix[1]) != 2:
                raise ValueError
            break
        except ValueError:
            messagebox.showerror("Erreur", "La clé doit être une matrice 2x2 au format [[x1, y1], [x2, y2]].")
    return matrix





def hill_decrypt(ciphertext, key):
    # Compute the inverse of the key matrix
    a, b = key[0]
    c, d = key[1]
    det = a*d - b*c
    if det % 2 == 0 or det % 13 == 0:
        return "Error: invalid key matrix"
    det_inv = pow(det, -1, 26)
    key_inv = [[(det_inv*d) % 26, (-det_inv*b) % 26], [(-det_inv*c) % 26, (det_inv*a) % 26]]

    # Convert ciphertext to numerical values (A=0, B=1, ..., Z=25)
    ciphertext = [ord(c) - ord("A") for c in ciphertext]

    # Reshape ciphertext as a matrix
    ciphertext = [[ciphertext[i], ciphertext[i+1]] for i in range(0, len(ciphertext), 2)]

    # Compute the plaintext as the product of the inverse key matrix and the ciphertext matrix
    plaintext = ""
    for i in range(len(ciphertext)):
        row = key_inv[0][0]*ciphertext[i][0] + key_inv[0][1]*ciphertext[i][1]
        col = key_inv[1][0]*ciphertext[i][0] + key_inv[1][1]*ciphertext[i][1]
        plaintext += chr((row % 26) + ord("A")) + chr((col % 26) + ord("A"))

    # If the length of the plaintext is odd, add an "X" to the end
    if len(plaintext) % 2 == 1:
        plaintext += " "

    return plaintext
######################################################### OK SANS ESPACES MAIS KO AVEC ############################################################


def main():
    ciphertext = input_cipher_text()
    key = input_matrix_key()
    plaintext = hill_decrypt(ciphertext, key)
    print("Ciphertext:", ciphertext)
    print("Key matrix:", key)
    print("Plaintext:", plaintext)
    with open ("hill_decrypted.txt", "w+") as f:
         f.write(plaintext)
    