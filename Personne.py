# Créé par DABLANCF, le 16/01/2025 en Python 3.7

class Personne():
  """
  Modélisation d'une personne.

  Attributs
  ---------
  - nom : str
      Renseigné à la création de l'objet
  - Prenom : str
      Renseigné à la création de l'objet
  - email : str
      Email. Initialisé à ""
  - telephone : str
      Numéro de téléphone. Initialisé à ""
  - date_naissance : str
      Chaîne de caractères au format jour/mois/année (4 chiffres). Initialisé à ""
  - jour_naissance : int
      Déterminé à partir de la date de naissance. Initialisée à -1
  - mois_naissance : int
      Déterminé à partir de la date de naissance. Initialisée à -1
  - annee_naissance : int
      Déterminé à partir de la date de naissance. Initialisée à -1
  """

  def __init__(self, nom: str, prenom: str,email: str,telephone: str,date_naissance:str,jour_naissance:int,mois_naissance:int,annee_naissance:int) -> None:
      self.nom=nom
      self.prenom=prenom
      self.email=email
      self.telephone=telephone
      self.date_naissance=date_naissance
      self.jour_naissance=jour_naissance
      self.mois_naissance=mois_naissance
      self.annee_naissance=annee_naissance

  def modifier_nom(self, nom: str) -> None:
      """
      Permet de modifier le nom de la personne.
      """
      self.nom=nom

  def obtenir_nom(self) -> str:
      """
      Retourne le nom de la personne.
      """
      return self.nom

  def modifier_prenom(self, prenom: str) -> None:
      """
      Permet de modifier le prénom de la personne.
      """
      self.prenom=prenom

  def obtenir_prenom(self) -> str:
      """
      Retourne le prénom de la personne.
      """
      return self.prenom

  def obtenir_email(self) -> str:
      """
      Retourne l'email de la personne.
      """
      return self.email

  def renseigner_email(self, email: str) -> None:
      """
      Renseigne l'attribut email de la personne.
      """
      self.email = email

  def obtenir_telephone(self) -> str:
      """
      Retourne le numéro de téléphone de la personne.
      """
      return self.telephone

  def renseigner_telephone(self, telephone: str) -> None:
      """
      Renseigne l'attribut telephone de la personne.
      """
      self.telephone = telephone

  def renseigner_date_naissance(self, date: str) -> None:
      """
      Récupère la date de naissance sous la forme jour/mois/année.
      Renseigne l'attribut date_naissance et, après un traitement, les attributs
      jour_naissance, mois_naissance, annee_naissance.

      Lève une exception de type ValueError si l'année ne possède pas le bon format.
      """
      a=self.annee_naissance
      m=self.mois_naissance
      j=self.jour_naissance
      date= str(a)+'/'+str(m)+'/'+str(j)
      self.date_naissance=date


  def obtenir_date_naissance(self) -> str:
      """
      Retourne la date de naissance.
      """
      return self.date_naissance

  def obtenir_age(self, annee_en_cours: int) -> int:
      """
      Retourne l'age de la personne à partir de l'année en cours.

      Lève une exception de type Exception si la date de naissance n'a pas été renseignée au préalable.
      """
      if self.date_naissance=='':
          raise Exception("La date de naissance n'a pas été renseignée")
      else:
        return annee_en_cours-self.annee_naissance

  def infos(self) -> str:
      """
      Retourne toutes les informations relatives à la personne.
      """
      chaine = """
      Prénom : {}
      Nom : {}
      Date de naissance : {}
      Email : {}
      Téléphone : {}
      """.format(self.obtenir_prenom(), self.obtenir_nom(),
                 self.obtenir_date_naissance(), self.obtenir_email(),
                 self.obtenir_telephone())

      return chaine