from Banque import *
from Compte_bancaire import *
from Personne import *
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
    creation_compte.geometry("350x500")
    creation_compte.resizable(width=False, height=False)

    Label(creation_compte, text="Création de compte").grid(row=0, column=1)
    Label(creation_compte, text="Nom :").grid(row=1, column=0)
    nom = Entry(creation_compte)
    nom.grid(row=1, column=1)
    Label(creation_compte, text="Prénom :").grid(row=2, column=0)
    prenom = Entry(creation_compte)
    prenom.grid(row=2, column=1)
    Label(creation_compte, text="Montant initial :").grid(row=3, column=0)
    montant_initial = Entry(creation_compte)
    montant_initial.grid(row=3, column=1)
    Label(creation_compte, text="Email :").grid(row=4, column=0)
    email = Entry(creation_compte)
    email.grid(row=4, column=1)
    Label(creation_compte, text="Téléphone :").grid(row=5, column=0)
    telephone = Entry(creation_compte)
    telephone.grid(row=5, column=1)
    Label(creation_compte, text="Jour de naissance :").grid(row=6, column=0)
    jour_naissance = Entry(creation_compte)
    jour_naissance.grid(row=6, column=1)
    Label(creation_compte, text="Mois de naissance :").grid(row=7, column=0)
    mois_naissance = Entry(creation_compte)
    mois_naissance.grid(row=7, column=1)
    Label(creation_compte, text="Année de naissance :").grid(row=8, column=0)
    annee_naissance = Entry(creation_compte)
    annee_naissance.grid(row=8, column=1)

    def creer_compte():
        nom_val = nom.get()
        prenom_val = prenom.get()
        montant_initial_val = float(montant_initial.get())
        email_val = email.get()
        telephone_val = telephone.get()
        jour_naissance_val = int(jour_naissance.get())
        mois_naissance_val = int(mois_naissance.get())
        annee_naissance_val = int(annee_naissance.get())

        # creer un objet Personne
        p = Personne(nom_val, prenom_val, email_val, telephone_val, jour_naissance_val, mois_naissance_val, annee_naissance_val)
        # cree un objet Compte_bancaire
        c = Compte_bancaire(p, montant_initial_val)
        # sauvarde le compte cree dans le dictionnaire
        comptes_crees[(nom_val, prenom_val)] = c
        print(f"Compte créé pour {nom_val} {prenom_val} avec un montant initial de {montant_initial_val}")
        creation_compte.destroy()
        return 

    Button(creation_compte, text='Créer', command=creer_compte).grid(row=9, column=1, pady=10)
    Button(creation_compte, text='Retour', command=creation_compte.destroy).grid(row=10, column=1, pady=10)

    creation_compte.mainloop()

def connexion():
    connexion = Tk()
    connexion.title("Connexion")
    connexion.geometry("350x400")
    connexion.resizable(width=False, height=False)

    Label(connexion, text="Connexion").grid(row=0, column=1)
    Label(connexion, text="Nom :").grid(row=1, column=0)
    nom = Entry(connexion)
    nom.grid(row=1, column=1)
    Label(connexion, text="Prénom :").grid(row=2, column=0)
    prenom = Entry(connexion)
    prenom.grid(row=2, column=1)

    def verifier_connexion():
        nom_val = nom.get()
        prenom_val = prenom.get()
        if (nom_val, prenom_val) in comptes_crees:
            print(f"Connexion réussie pour {nom_val} {prenom_val}")
            compte = comptes_crees[(nom_val, prenom_val)]

            compte_window = Tk()
            compte_window.title("Compte")
            compte_window.geometry("400x500")
            compte_window.resizable(width=False, height=False)

            Label(compte_window, text="Compte").grid(row=0, column=1)
            Label(compte_window, text=f"Nom : {compte.proprietaire.nom}").grid(row=1, column=0)
            Label(compte_window, text=f"Prénom : {compte.proprietaire.prenom}").grid(row=2, column=0)
            Label(compte_window, text=f"Numéro de compte : {compte.identifiant}").grid(row=3, column=0)
            Label(compte_window, text=f"Solde : {compte.solde}").grid(row=4, column=0)

            def effectuer_depot():
                montant = float(depot_entry.get())
                compte.depot(montant)
                Label(compte_window, text=f"Solde : {compte.solde}").grid(row=4, column=0)

            def effectuer_retrait():
                montant = float(retrait_entry.get())
                compte.retrait(montant)
                Label(compte_window, text=f"Solde : {compte.solde}").grid(row=4, column=0)

            def effectuer_virement():
                destinataire_nom = virement_nom.get()
                destinataire_prenom = virement_prenom.get()
                montant = float(virement_montant.get())

                if (destinataire_nom, destinataire_prenom) in comptes_crees:
                    destinataire_compte = comptes_crees[(destinataire_nom, destinataire_prenom)]
                    if compte.solde >= montant:
                        compte.retrait(montant)
                        destinataire_compte.depot(montant)
                        Label(compte_window, text=f"Solde : {compte.solde}").grid(row=4, column=0)
                        print(f"Virement de {montant}€ effectué vers {destinataire_nom} {destinataire_prenom}")
                    else:
                        erreur = Tk()
                        erreur.title("Erreur")
                        erreur.geometry("200x100")
                        erreur.resizable(width=False, height=False)
                        Label(erreur, text="Fonds insuffisants.").grid(row=0, column=0)
                        Button(erreur, text="OK", command=erreur.destroy).grid(row=1, column=0)
                else:
                    erreur = Tk()
                    erreur.title("Erreur")
                    erreur.geometry("200x100")
                    erreur.resizable(width=False, height=False)
                    Label(erreur, text="Compte destinataire non existant.").grid(row=0, column=0)
                    Button(erreur, text="OK", command=erreur.destroy).grid(row=1, column=0)

            # deposer 
            Label(compte_window, text="Montant à déposer :").grid(row=5, column=0)
            depot_entry = Entry(compte_window)
            depot_entry.grid(row=5, column=1)
            Button(compte_window, text="Déposer", command=effectuer_depot).grid(row=6, column=1)

            # retirer
            Label(compte_window, text="Montant à retirer :").grid(row=7, column=0)
            retrait_entry = Entry(compte_window)
            retrait_entry.grid(row=7, column=1)
            Button(compte_window, text="Retirer", command=effectuer_retrait).grid(row=8, column=1)

            # transfert
            Label(compte_window, text="Nom du destinataire :").grid(row=9, column=0)
            virement_nom = Entry(compte_window)
            virement_nom.grid(row=9, column=1)
            Label(compte_window, text="Prénom du destinataire :").grid(row=10, column=0)
            virement_prenom = Entry(compte_window)
            virement_prenom.grid(row=10, column=1)
            Label(compte_window, text="Montant à transférer :").grid(row=11, column=0)
            virement_montant = Entry(compte_window)
            virement_montant.grid(row=11, column=1)
            Button(compte_window, text="Effectuer le virement", command=effectuer_virement).grid(row=12, column=1)

            compte_window.mainloop()
        else:
            erreur = Tk()
            erreur.title("Erreur")
            erreur.geometry("200x100")
            erreur.resizable(width=False, height=False)
            Label(erreur, text="Compte inexistant.").grid(row=0, column=0)
            Button(erreur, text="OK", command=erreur.destroy).grid(row=1, column=0)

    Button(connexion, text='Se connecter', command=verifier_connexion).grid(row=3, column=1, pady=10)
    Button(connexion, text='Retour', command=connexion.destroy).grid(row=4, column=1, pady=10)

    connexion.mainloop()

Button(fen, text="Créer un compte", command=creation_compte).grid(row=1, column=1, pady=10)
Button(fen, text="Se connecter", command=connexion).grid(row=2, column=1, pady=10)

fen.mainloop()
