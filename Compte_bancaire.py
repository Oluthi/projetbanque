from Personne import Personne


class Compte_bancaire():
    """
    Définition d'un compte bancaire.

    Attributs
    ---------
    - proprietaire : Personne
        Personne propriétaire du compte. Initialisé à la création de l'objet.
    - identifiant : int
        Identifiant unique du compte. Initialisé à la création de l'objet par un calcul réalisé par une méthode statique.
    - solde : float
        Solde du compte. Initialisé à la création de l'objet.
    """

    def __init__(self, proprietaire: Personne, montant_initial: float) -> None:
        """
        Initialisation des attributs.
        """
        self.proprietaire = proprietaire
        self.montant_init = montant_initial


    @staticmethod
    def determine_id(proprietaire: Personne) -> int:
        """
        Détermine l'identifiant du compte aléatoirement à partir du
        nom et du prénom du propriétaire.
        NB : Possibilité de s'inspirer du MD5, faites une recherche sur les fonctions de hachage, soyez créatifs.

        Méthode statique
        """


    def obtenir_solde(self) -> float:
        """
        Retourne le solde du compte.
        """
        return self.montant_init


    def depot(self, montant: float) -> None:
        """
        Ajoute montant au solde
        """


    def retrait(self, montant: float) -> None:
        """
        Retire le montant montant du solde à la condition qu'il y ait suffisamment d'argent.
        Une exception de type ValueError est levée si le montant est trop important
        """


    def infos(self) -> str:
        """
        Informations sur le compte.
        """
        chaine = """
        Compte numéro : {}
        Solde : {}
        """.format(self.identifiant, self.solde)

        chaine = chaine + self.proprietaire.infos()

        return chaine
