import os
import pandas as pd
import Donnees

# Chemin de l'enregistrement des fichiers netoyes
DOSSIER_DONNEES_P = os.path.realpath("../..").replace('\\', '/') + "/Donnees_Propres/"

# Création du dossier de stockage des données propres si non existant
try:
    os.mkdir(DOSSIER_DONNEES_P)
except OSError:
    pass


# Netoyage du fichier Catalogue.csv
# ----------------------------------------------------------------------------
def nettoyage_catalogue(fichier, valeurs_manquantes, index=False, encoding='latin-1'):

    # Stockage des donnees du fichier dans la variable donnee et remplacement
    # des valeurs manquantes par "NaN" (reconnue par panda)
    donnees = pd.read_csv(fichier, na_values=valeurs_manquantes["NaN"],
                          encoding=encoding)

    # Ecriture des donnees dans un nouveau fichier CSV
    donnees.to_csv(DOSSIER_DONNEES_P + fichier.split("/")[-1], index=index,
                   encoding=encoding)


# Netoyage des fichiers Clients_n.csv
# ----------------------------------------------------------------------------
def nettoyage_clients(fichier, valeurs_manquantes, valeurs_incorrectes,
                      index=False, encoding='latin-1'):

    donnees = pd.read_csv(fichier, na_values=valeurs_manquantes["NaN"],
                          encoding=encoding)

    colonnes_a_modifier = ["sexe", "situationFamiliale"]

    indices = []

    # Stockage des indices des valeurs à modifier
    indices += donnees.index[donnees[colonnes_a_modifier[0]].isin(valeurs_incorrectes["F"])].tolist()
    indices += donnees.index[donnees[colonnes_a_modifier[0]].isin(valeurs_incorrectes["M"])].tolist()
    indices += donnees.index[donnees[colonnes_a_modifier[1]].isin(valeurs_incorrectes["Célibataire"])].tolist()

    # Correction des valeurs
    for colonne in colonnes_a_modifier:
        for c in indices:
            for correction, erreurs in valeurs_incorrectes.items():
                if donnees[colonne][c] in erreurs:
                    donnees[colonne][c] = correction

    # Convertion des entiers en int (transformés en float lors de la lecture du fichier)
    donnees["age"] = donnees["age"].astype(dtype=pd.Int64Dtype())
    donnees["taux"] = donnees["taux"].astype(dtype=pd.Int64Dtype())
    donnees["nbEnfantsAcharge"] = donnees["nbEnfantsAcharge"].astype(dtype=pd.Int64Dtype())

    donnees.to_csv(DOSSIER_DONNEES_P + fichier.split("/")[-1], index=index,
                   encoding=encoding)


# Netoyage du fichier CO2.csv
# ----------------------------------------------------------------------------
def nettoyage_co2(fichier, valeurs_manquantes, index=False, encoding='utf16'):

    # Suppression de la colonne index (Unnamed)
    donnees = pd.read_csv(fichier, index_col=[0],
                          na_values=valeurs_manquantes["NaN"])

    # Encodage en utf16 pour les caractères non reconnu
    donnees.to_csv(DOSSIER_DONNEES_P + fichier.split("/")[-1], index=index,
                   encoding=encoding)


# Netoyage du fichier Immatriculations.csv
# ----------------------------------------------------------------------------
def nettoyage_immatriculations(fichier, valeurs_manquantes, index=False,
                               encoding='latin-1'):

    donnees = pd.read_csv(fichier, na_values=valeurs_manquantes["NaN"],
                          encoding=encoding)

    donnees.to_csv(DOSSIER_DONNEES_P + fichier.split("/")[-1], index=index,
                   encoding=encoding)


# Netoyage du fichier Marketing.csv
# ----------------------------------------------------------------------------
def nettoyage_marketing(fichier, valeurs_manquantes, index=False, encoding='latin-1'):

    donnees = pd.read_csv(fichier, na_values=valeurs_manquantes["NaN"],
                          encoding=encoding)

    donnees.to_csv(DOSSIER_DONNEES_P + fichier.split("/")[-1], index=index,
                   encoding=encoding)


# Execution des fonctions de nettoyage
# ----------------------------------------------------------------------------
def netoyage_donnees():

    nettoyage_catalogue(Donnees.CATALOGUE, Donnees.VALEURS_MANQUANTES)
    nettoyage_clients(Donnees.CLIENTS_3, Donnees.VALEURS_MANQUANTES, Donnees.VALEURS_CLIENTS_INCORECTES)
    nettoyage_clients(Donnees.CLIENTS_11, Donnees.VALEURS_MANQUANTES, Donnees.VALEURS_CLIENTS_INCORECTES)
    nettoyage_co2(Donnees.CO2, Donnees.VALEURS_MANQUANTES)
    nettoyage_immatriculations(Donnees.IMMATRICULATIONS, Donnees.VALEURS_MANQUANTES)
    nettoyage_marketing(Donnees.MARKETING, Donnees.VALEURS_MANQUANTES)


if __name__ == "__main__":
    from time import time

    debut = time()

    netoyage_donnees()

    fin = time()
    print("Temps d'execution : ", fin - debut, "s")
