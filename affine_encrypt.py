import string
import random
import userinput

string.printable += '@'



# Fonction de chiffrement
def encrypt_affine(plaintext, a, b):

    ciphertext = ""
    n = len(string.printable)  # nombre total de caractères imprimables
    for char in plaintext:
        if char in string.printable:
            x = string.printable.index(char)
            y = (a * x + b) % n
            ciphertext += string.printable[y]
        else:
            ciphertext += char
    return ciphertext

#----------Générateur a-------------------------
def generate_random_a(lower, upper):
    return random.randint(lower, upper)
#-----------------------------------------------

def main():
    m = len(string.printable)
    message = userinput.main()
    #message = input("Le message à chiffrer :")
    a = generate_random_a(2*m+1, 10*m)
    b = generate_random_a(2, m-1)

    ciphertext = encrypt_affine(message, a, b)
    print("Le message à chiffrer est: ", message)
    print("Votre message est chiffré correctement: ", ciphertext)
    with open("affine_encrypted.txt", 'w+') as cipherfile:
        cipherfile.write(ciphertext)

    print("Voici votre clé de déchiffrement A : ", a)
    with open("affine_key_a.txt", 'w') as keya:
        keya.write(str(a))
    print("Voici votre clé de déchiffrement B : ", b)
    with open("affine_key_b.txt", 'w') as keyb:
        keyb.write(str(b))