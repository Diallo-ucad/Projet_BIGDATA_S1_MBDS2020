import os
import pandas as pd
import Donnees

# Chemin de l'enrigistrement des fichiers netoyés
DOSSIER_DONNEES_P = os.path.realpath("../..").replace('\\', '/') + "/Données_Propres/"


# Netoyage du fichier Catalogue.csv
# ----------------------------------------------------------------------------
def nettoyage_catalogue(fichier, valeurs_manquantes, index=False, encoding='latin-1'):

    donnees = pd.read_csv(fichier, na_values=valeurs_manquantes["NaN"],
                          encoding=encoding)

    donnees.to_csv(DOSSIER_DONNEES_P + fichier.split("/")[-1], index=index,
                   encoding=encoding)


# Netoyage des fichiers Clients_n.csv
# ----------------------------------------------------------------------------
def nettoyage_clients(fichier, valeurs_manquantes, valeurs_incorrectes,
                      index=False, encoding='latin-1'):

    donnees = pd.read_csv(fichier,na_values=valeurs_manquantes["NaN"],
                          encoding=encoding)
    taille = donnees.shape[0]
    for colonne in donnees:
        for c in range(taille):
            for correction, erreurs in valeurs_incorrectes.items():
                if donnees[colonne][c] in erreurs:
                    donnees[colonne][c] = correction
                    #donnees[colonne][c] = donnees[colonne][c].replace(donnees[colonne][c], correction)

    donnees["age"] = donnees["age"].astype(dtype=pd.Int64Dtype())
    donnees["taux"] = donnees["taux"].astype(dtype=pd.Int64Dtype())
    donnees["nbEnfantsAcharge"] = donnees["nbEnfantsAcharge"].astype(dtype=pd.Int64Dtype())

    donnees.to_csv(DOSSIER_DONNEES_P + fichier.split("/")[-1], index=index,
                   encoding=encoding)


# Netoyage dufichier CO2.csv
# ----------------------------------------------------------------------------
def nettoyage_co2(fichier, valeurs_manquantes, index=False, encoding='utf16'):

    # Suppression de la colonne index (Unnamed)
    donnees = pd.read_csv(fichier, index_col=[0],
                          na_values=valeurs_manquantes["NaN"])

    # Encodage en utf16 pour les caractères non reconnu
    donnees.to_csv(DOSSIER_DONNEES_P + fichier.split("/")[-1], index=index,
                   encoding=encoding)


# Netoyage dufichier Immatriculations.csv
# ----------------------------------------------------------------------------
def nettoyage_immatriculations(fichier, valeurs_manquantes, index=False,
                               encoding='latin-1'):

    donnees = pd.read_csv(fichier, na_values=valeurs_manquantes["NaN"],
                          encoding=encoding)

    donnees.to_csv(DOSSIER_DONNEES_P + fichier.split("/")[-1], index=index,
                   encoding=encoding)


# Netoyage dufichier Marketing.csv
# ----------------------------------------------------------------------------
def nettoyage_marketing(fichier, valeurs_manquantes, index=False, encoding='latin-1'):

    donnees = pd.read_csv(fichier, na_values=valeurs_manquantes["NaN"],
                          encoding=encoding)

    donnees.to_csv(DOSSIER_DONNEES_P + fichier.split("/")[-1], index=index,
                   encoding=encoding)


# Exécution des fonctions de nettoyage
# ----------------------------------------------------------------------------
def netoyage_donnees():
    nettoyage_catalogue(Donnees.CATALOGUE, Donnees.VALEURS_MANQUANTES)
    nettoyage_clients(Donnees.CLIENTS_3, Donnees.VALEURS_MANQUANTES, Donnees.VALEURS_CLIENTS_INCORECTES)
    nettoyage_clients(Donnees.CLIENTS_11, Donnees.VALEURS_MANQUANTES, Donnees.VALEURS_CLIENTS_INCORECTES)
    nettoyage_co2(Donnees.CO2, Donnees.VALEURS_MANQUANTES)
    nettoyage_immatriculations(Donnees.IMMATRICULATIONS, Donnees.VALEURS_MANQUANTES)
    nettoyage_marketing(Donnees.MARKETING, Donnees.VALEURS_MANQUANTES)


if __name__ == "__main__":

    netoyage_donnees()

