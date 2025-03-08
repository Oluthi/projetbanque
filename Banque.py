from Compte_bancaire import Compte_bancaire
from Personne import Personne


class Banque():
    """
    Modélisation d'une banque.

    Attributs
    ---------
    - nom : str
        Nom de la banque. Initialisé lors de la création de l'objet.
    - comptes : Liste[Compte_bancaire]
        Liste des comptes bancaires au sein de la banque.
    """

    def __init__(self, nom: str) -> None:
        """
        Initialisation de l'objet
        """
        self.nombanque = nom
        pass

    def creation_compte(self) -> None:
        """
        Prend en charge l'ouverture d'un compte au sein de la banque.
        """
        print("Procédure de création du compte :")
        print("---------------------------------")

        nom = input("Nom du propriétaire du compte : ")
        prenom = input("Prenom du propriétaire du compte : ")
        montant_initial = float(input("Montant du dépôt initial : "))

        p = Personne(nom, prenom)
        c = Compte_bancaire(p, montant_initial)

        self.comptes.append(c)

    def infos(self) -> str:
        """
        Informations sur la banque
        """
        chaine = """
        -----------
        """

        for compte in self.comptes:
            chaine = chaine + compte.infos()
            chaine = """
            -----------

            """

        return chaine
