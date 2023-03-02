import random
from math import gcd
import userinput

def generate_invertible_matrix():
    while True:
        # Generate a random 2x2 matrix
        key = [[random.randint(0, 25) for _ in range(2)] for _ in range(2)]

        # Check if the determinant is invertible (i.e., coprime to 26)
        det = key[0][0]*key[1][1] - key[0][1]*key[1][0]
        if gcd(det, 26) == 1:
            return key

def hill_encrypt(plaintext):
    # Define the key matrix (2x2)
    key = generate_invertible_matrix()
    print("Matrice clé utilisée:", key)
    with open ("hill_key.txt", "w+") as f:
        f.write(str(key))

    # Convert plaintext to uppercase and remove spaces
    plaintext = plaintext.upper().replace(" ", "")

    # Add padding if necessary
    if len(plaintext) % 2 != 0:
        plaintext += " "

    # Convert plaintext to numerical values (A=0, B=1, ..., Z=25)
    plaintext = [ord(c) - ord("A") for c in plaintext]

    # Reshape plaintext as a matrix
    plaintext = [[plaintext[i], plaintext[i+1]] for i in range(0, len(plaintext), 2)]

    # Compute the ciphertext as the product of the key matrix and the plaintext matrix
    ciphertext = ""
    for i in range(len(plaintext)):
        row = key[0][0]*plaintext[i][0] + key[0][1]*plaintext[i][1]
        col = key[1][0]*plaintext[i][0] + key[1][1]*plaintext[i][1]
        ciphertext += chr((row % 26) + ord("A")) + chr((col % 26) + ord("A"))

    return ciphertext

def main():
    message = userinput.main()
    ciphertext = hill_encrypt(message)
    print("Message à chiffrer:", message)
    print("Message chiffré:", ciphertext)
    with open ("hill_encrypted.txt", "w") as f: 
        f.write(ciphertext)