
from Banque import Banque
from Compte_bancaire import Compte_bancaire
from Personne import Personne
from customtkinter import*
from tkinter import *


set_appearance_mode("dark")
set_default_color_theme("blue")


fen = CTk()
fen.title("Sigma Banque")
fen.geometry("350x400")
fen.resizable(width=False, height=False)
fen.grid_columnconfigure((0,5), weight=1)
fen.grid_rowconfigure((0,5), weight=1)
CTkLabel(fen, text="Sigma Bank").grid(row=0, column=1)

def creation_compte():
    creation_compte = CTk()
    creation_compte.title("Création de compte")
    creation_compte.geometry("350x400")
    creation_compte.resizable(width=False, height=False)
    creation_compte.grid_columnconfigure((0,5), weight=1)
    creation_compte.grid_rowconfigure((0,5), weight=1)
    CTkLabel(creation_compte, text="Création de compte").grid(row=0, column=0)
    CTkLabel(creation_compte, text="Nom du propriétaire du compte :").grid(row=1, column=0)
    nom = CTkEntry(creation_compte)
    nom.grid(row=1, column=1)
    CTkLabel(creation_compte, text="Prénom du propriétaire du compte :").grid(row=2, column=0)
    prenom = CTkEntry(creation_compte)
    prenom.grid(row=2, column=1)
    creation_compte.mainloop()

def connexion():
    connexion = CTk()
    connexion.title("Connexion")
    connexion.geometry("350x400")
    connexion.resizable(width=False, height=False)
    connexion.grid_columnconfigure((0,5), weight=1)
    connexion.grid_rowconfigure((0,5), weight=1)
    CTkLabel(connexion, text="Connexion").grid(row=0, column=0)
    CTkLabel(connexion, text="Nom du propriétaire du compte :").grid(row=1, column=0)
    nom = CTkEntry(connexion)
    nom.grid(row=1, column=1)
    CTkLabel(connexion, text="Prénom du propriétaire du compte :").grid(row=2, column=0)
    prenom = CTkEntry(connexion)
    prenom.grid(row=2, column=1)
    connexion.mainloop()






CTkButton(fen, text="Créer un compte", command=creation_compte).grid(row=1, column=1)
CTkButton(fen, text="Se connecter", command=connexion).grid(row=2, column=1)



fen.mainloop()
