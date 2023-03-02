#-----------------------------------------
# Titre de la feuille : Générateur de clés ( Keygen ) 
# Description de la feuille : Réalisation d'un programme de chiffrement

# 1 : Génération d'une paire de clés ( pub et priv )
# 2 : Chiffrement d'un message provenant d'un fichier
# 3 : Déchiffrement 

# Nombre de caractères maximum 125, ne pas dépasser cette valeur

#-----------------------------------------

#Importation des modules
import random
import base64
from math import *
import sympy

# Fonction pour savoir si un nomber est premier
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_prime(nbits):
    while True:
        p = random.getrandbits(nbits)
        if is_prime(p):
            return p


def generate_key_pair():
    p = generate_prime(32)
    q = generate_prime(32)
    n = p * q
    phi_n = (p - 1) * (q - 1)
    while True:
        e = random.randrange(3, phi_n)
        if gcd(e, phi_n) == 1:
            break
    d = sympy.mod_inverse(e, phi_n)

    public_key_bytes = "{}_{}".format(n, e).encode('utf-8')
    private_key_bytes = "{}_{}".format(n, d).encode('utf-8')

    public_key_base64 = base64.b64encode(public_key_bytes).decode('utf-8')
    private_key_base64 = base64.b64encode(private_key_bytes).decode('utf-8')

    fichier = open ("rsa_pubkey.txt", "w+") 
    fichier.write("-----BEGIN PUBLIC KEY-----\n")
    fichier.write(f'{public_key_base64}\n')
    fichier.write("-----END PUBLIC KEY-----")
    fichier.close

    fichier = open ("rsa_privkey.txt", "w+") 
    fichier.write("-----BEGIN PRIVATE KEY-----\n")
    fichier.write(f'{private_key_base64}\n')
    fichier.write("-----END PRIVATE KEY-----\n")
    fichier.close