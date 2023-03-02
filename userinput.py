import tkinter as tk
from tkinter import simpledialog, messagebox
import sys

def main():
    root = tk.Tk()
    root.withdraw()
    message = simpledialog.askstring("Chiffrer un message", "Saisissez le message à chiffrer, maximum 125 caractères :", parent=root)
    if len(message) > 125:
        messagebox.showerror("Erreur", "Le message ne doit pas dépasser 125 caractères.")
        sys.exit(1)
    if len(message) == 0:
        messagebox.showerror("Erreur", "Le message ne doit pas être vide.")
        sys.exit(1)
    return message
