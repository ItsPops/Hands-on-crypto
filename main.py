#-----------------------------------------
# Titre du projet : Mini-projet cryptographique 
# Participants du projet : BRILLE François, MOKRANE AKli, KERROUM Soraya, ORTEGA Jean
# Description du projet : Réalisation d'un programme de chiffrement
#-----------------------------------------

#Importation des librairies pour les besoins du menu
import tkinter as tk
from tkinter import filedialog, Menu

#Importation des autres scripts
import rsa_encrypt
import rsa_decrypt
import rsa_keygen

import affine_encrypt
import affine_decrypt

import hill_encrypt
import hill_decrypt


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("800x300")
        self.master.title("Menu")
        self.pack()
        self.create_widgets()

    def clear_confirm_label(self):
        self.confirm_label.destroy()

    def create_widgets(self):
        self.title = tk.Label(self, text="Menu cryptographique", font=("Arial", 24), fg="#202020")
        self.title.pack(side="top", pady=5)

        # Créer la barre de menu
        menubar = Menu(self.master)

        # Création des menu principaux
        sous_menu_chiffrer = Menu(menubar, tearoff=0)
        sous_menu_dechiffrer = Menu(menubar, tearoff=0)
        sous_menu_outils = Menu(menubar, tearoff=0)

        # Ajouter les menus "Chiffrer" et "Déchiffrer" à la barre de menu
        menubar.add_cascade(label="Chiffrer", menu=sous_menu_chiffrer)
        menubar.add_cascade(label="Déchiffrer", menu=sous_menu_dechiffrer)
        menubar.add_cascade(label="Outils", menu=sous_menu_outils)
     
        ####################################################################################################

        # Sous-menu chiffrer
        encrypted_menu_rsa = Menu(sous_menu_chiffrer, tearoff=0)
        encrypted_menu_hill = Menu(sous_menu_chiffrer, tearoff=0)
        encrypted_menu_affines = Menu(sous_menu_chiffrer, tearoff=0)

        # Sous-meneu déchiffrer
        decrypted_menu_rsa = Menu(sous_menu_dechiffrer, tearoff=0)
        decrypted_menu_hill = Menu(sous_menu_dechiffrer, tearoff=0)
        decrypted_menu_affines = Menu(sous_menu_dechiffrer, tearoff=0)

        #sous-menu outils
        keygenrsa = Menu(sous_menu_outils, tearoff=0)

        ####################################################################################################

        # Sous-menu des différents algo ENCRYPTED
        sous_menu_chiffrer.add_cascade(label="RSA", menu=encrypted_menu_rsa)
        sous_menu_chiffrer.add_cascade(label="Hill", menu=encrypted_menu_hill)
        sous_menu_chiffrer.add_cascade(label="Affines", menu=encrypted_menu_affines)

        # Sous-menu des différents algo DECRYPTED
        sous_menu_dechiffrer.add_cascade(label="RSA", menu=decrypted_menu_rsa)
        sous_menu_dechiffrer.add_cascade(label="Hill", menu=decrypted_menu_hill)
        sous_menu_dechiffrer.add_cascade(label="Affines", menu=decrypted_menu_affines)

        ####################################################################################################

        # Sous-sous-menu ENCRYPTED le message pour RSA, hill et affine
        encrypted_menu_rsa.add_command(label="Chiffrer le message", command=self.run_encrypt_rsa)
        encrypted_menu_hill.add_command(label="Chiffrer le message", command=self.run_encrypt_hill)
        encrypted_menu_affines.add_command(label="Chiffrer le message", command=self.run_encrypt_affines)

        # Sous-sous-menu DECRYPTED le message pour RSA, hill et affine
        decrypted_menu_rsa.add_command(label="Déchiffrer le message", command=self.run_decrypt_rsa)
        decrypted_menu_hill.add_command(label="Déchiffrer le message", command=self.run_decrypt_hill)
        decrypted_menu_affines.add_command(label="Déchiffrer le message", command=self.run_decrypt_affines)

        # Sous-menu génération de clés RSA
        sous_menu_outils.add_command(label="Générer une clé RSA", command=self.run_keygen_rsa)

        ####################################################################################################

        # Créer le bouton "Quitter"
        quit_button = tk.Button(root, text="Quitter", command=self.master.destroy)
        quit_button.pack(side="bottom", pady=10)

        # Configurer la barre de menu
        self.master.config(menu=menubar)

###############################################################---APPEL DES SCRIPTS---###############################################################

    ### RSA

    def run_keygen_rsa(self):
        try:
            rsa_keygen.generate_key_pair()
            self.confirm_label = tk.Label(self, text="Commande exécutée avec succès", font=("Arial", 12), fg="green")
            self.confirm_label.pack(side="bottom", pady=10)
        except Exception as e:
            self.confirm_label = tk.Label(self, text=f"Erreur lors de l'exécution de la commande: {e}", font=("Arial", 12), fg="red")
            self.confirm_label.pack(side="bottom", pady=10)

        self.master.after(4000, self.clear_confirm_label)


    def run_encrypt_rsa(self):
        try:
            #Appel de la fonction
            rsa_encrypt.main()
            self.confirm_label = tk.Label(self, text="Commande exécutée avec succès", font=("Arial", 12), fg="green")
            self.confirm_label.pack(side="bottom", pady=10)
        except Exception as e:
            self.confirm_label = tk.Label(self, text=f"Erreur lors de l'exécution de la commande: {e}", font=("Arial", 12), fg="red")
            self.confirm_label.pack(side="bottom", pady=10)

        self.master.after(4000, self.clear_confirm_label)

    def run_decrypt_rsa(self):
        try:
            #Appel de la fonction  
            rsa_decrypt.main()
            self.confirm_label = tk.Label(self, text="Commande exécutée avec succès", font=("Arial", 12), fg="green")
            self.confirm_label.pack(side="bottom", pady=10)
        except Exception as e:
            self.confirm_label = tk.Label(self, text=f"Erreur lors de l'exécution de la commande: {e}", font=("Arial", 12), fg="red")
            self.confirm_label.pack(side="bottom", pady=10)

        self.master.after(4000, self.clear_confirm_label)

    ### Hill

    def run_encrypt_hill(self):
        #Appel de la fonction
        try:
            hill_encrypt.main()
            self.confirm_label = tk.Label(self, text="Commande exécutée avec succès", font=("Arial", 12), fg="green")
            self.confirm_label.pack(side="bottom", pady=10)
        except Exception as e:
            self.confirm_label = tk.Label(self, text=f"Erreur lors de l'exécution de la commande: {e}", font=("Arial", 12), fg="red")
            self.confirm_label.pack(side="bottom", pady=10)

        self.master.after(4000, self.clear_confirm_label)

    def run_decrypt_hill(self):
        #Appel de la fonction
        try:
            hill_decrypt.main()
            self.confirm_label = tk.Label(self, text="Commande exécutée avec succès", font=("Arial", 12), fg="green")
            self.confirm_label.pack(side="bottom", pady=10)
        except Exception as e:
            self.confirm_label = tk.Label(self, text=f"Erreur lors de l'exécution de la commande: {e}", font=("Arial", 12), fg="red")
            self.confirm_label.pack(side="bottom", pady=10)

        self.master.after(4000, self.clear_confirm_label)

    ### Affines

    def run_encrypt_affines(self):
        #Appel de la fonction
        try:
            affine_encrypt.main()
            self.confirm_label = tk.Label(self, text="Commande exécutée avec succès", font=("Arial", 12), fg="green")
            self.confirm_label.pack(side="bottom", pady=10)
        except Exception as e:
            self.confirm_label = tk.Label(self, text=f"Erreur lors de l'exécution de la commande: {e}", font=("Arial", 12), fg="red")
            self.confirm_label.pack(side="bottom", pady=10)

        self.master.after(4000, self.clear_confirm_label)

    def run_decrypt_affines(self):
        #Appel de la fonction
        try:
            affine_decrypt.decrypt()
            self.confirm_label = tk.Label(self, text="Commande exécutée avec succès", font=("Arial", 12), fg="green")
            self.confirm_label.pack(side="bottom", pady=10)
        except Exception as e:
            self.confirm_label = tk.Label(self, text=f"Erreur lors de l'exécution de la commande: {e}", font=("Arial", 12), fg="red")
            self.confirm_label.pack(side="bottom", pady=10)

        self.master.after(4000, self.clear_confirm_label)


root = tk.Tk()
app = Application(master=root)
app.mainloop()