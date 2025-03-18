# Créé par 33603, le 17/03/2025 en Python 3.7
from Banque import Banque
from Compte_bancaire import Compte_bancaire
from Personne import Personne
from tkinter import *

fen = Tk()
fen.title("Sigma Banque")
fen.geometry("350x400")
fen.resizable(width=False, height=False)

Label(fen, text="Sigma Bank").grid(row=0, column=1)

comptes_crees = {}

def creation_compte():
    creation_compte = Tk()
    creation_compte.title("Création de compte")
    creation_compte.geometry("350x400")
    creation_compte.resizable(width=False, height=False)

    Label(creation_compte, text="Création de compte").grid(row=0, column=1)
    Label(creation_compte, text="Nom du propriétaire du compte :").grid(row=1, column=0)
    nom = Entry(creation_compte)
    nom.grid(row=1, column=1)
    Label(creation_compte, text="Prénom du propriétaire du compte :").grid(row=2, column=0)
    prenom = Entry(creation_compte)
    prenom.grid(row=2, column=1)

    def creer_compte():
        nom_val = nom.get()
        prenom_val = prenom.get()
        if nom_val and prenom_val:
            comptes_crees[(nom_val, prenom_val)] = True
            print(f"Compte créé pour {nom_val} {prenom_val}")
        else:
            print("Veuillez remplir tous les champs.")

    Button(creation_compte, text='Créer', command=creer_compte).grid(row=3, column=1, pady=10)
    Button(creation_compte, text='Retour', command=creation_compte.destroy).grid(row=4, column=1, pady=10)

    creation_compte.mainloop()

def connexion():
    connexion = Tk()
    connexion.title("Connexion")
    connexion.geometry("350x400")
    connexion.resizable(width=False, height=False)

    Label(connexion, text="Connexion").grid(row=0, column=1)
    Label(connexion, text="Nom du propriétaire du compte :").grid(row=1, column=0)
    nom = Entry(connexion)
    nom.grid(row=1, column=1)
    Label(connexion, text="Prénom du propriétaire du compte :").grid(row=2, column=0)
    prenom = Entry(connexion)
    prenom.grid(row=2, column=1)

    def verifier_connexion():
        nom_val = nom.get()
        prenom_val = prenom.get()
        if (nom_val, prenom_val) in comptes_crees:
            print(f"Connexion réussie pour {nom_val} {prenom_val}")
        else:
            print("Compte non existant.")

    Button(connexion, text='Se connecter', command=verifier_connexion).grid(row=3, column=1, pady=10)
    Button(connexion, text='Retour', command=connexion.destroy).grid(row=4, column=1, pady=10)

    connexion.mainloop()

Button(fen, text="Créer un compte", command=creation_compte).grid(row=1, column=1, pady=10)
Button(fen, text="Se connecter", command=connexion).grid(row=2, column=1, pady=10)

fen.mainloop()




