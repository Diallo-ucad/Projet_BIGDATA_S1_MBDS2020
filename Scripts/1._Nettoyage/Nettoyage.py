#!/usr/bin/python
# -*- coding: latin-1 -*-

import os
import pandas as pd
import Donnees

# Chemin de l'enregistrement des fichiers netoyes
DOSSIER_DONNEES_P = os.path.realpath("..").replace('\\', '/') + "/Donnees_Propres/"

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

    indices_sexe = []
    indices_situationFamiliale = []

    # Stockage des indices des valeurs à modifier
    indices_sexe += donnees.index[donnees[colonnes_a_modifier[0]].isin(("Féminin", "Femme"))].tolist()
    indices_sexe += donnees.index[donnees[colonnes_a_modifier[0]].isin(("Masculin", "Homme"))].tolist()
    indices_situationFamiliale += donnees.index[donnees[colonnes_a_modifier[1]].isin(("Seule", "Seul"))].tolist()

    indices = {"sexe" : indices_sexe, "situationFamiliale": indices_situationFamiliale}

    # Correction des valeurs
    for colonne in colonnes_a_modifier:  
        for c in indices[colonne]:
            k = donnees[colonne][c]
            donnees.at[c, colonne] = valeurs_incorrectes[k]
         

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

    # Encodage en utf16 pour les caracteres non reconnu
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

def showTime(debut, fin):
    print ("Temps d'execution : " + str(fin - debut) + " s") 
    return fin
# Execution des fonctions de nettoyage
# ----------------------------------------------------------------------------
def netoyage_donnees(d):
    print("\nnettoyage catalogue")
    nettoyage_catalogue(Donnees.CATALOGUE, Donnees.VALEURS_MANQUANTES)
    d1 = showTime(d, time())

    print("\nnettoyage clients 3")
    nettoyage_clients(Donnees.CLIENTS_3, Donnees.VALEURS_MANQUANTES, Donnees.VALEURS_CLIENTS_INCORECTES)
    d2 = showTime(d1, time())

    print("\nnettoyage clients 11")
    nettoyage_clients(Donnees.CLIENTS_11, Donnees.VALEURS_MANQUANTES, Donnees.VALEURS_CLIENTS_INCORECTES)
    d3 = showTime(d2, time())

    print("\nnettoyage co2")
    nettoyage_co2(Donnees.CO2, Donnees.VALEURS_MANQUANTES)
    d4 = showTime(d3, time())

    print("\nnettoyage immatriculations")
    nettoyage_immatriculations(Donnees.IMMATRICULATIONS, Donnees.VALEURS_MANQUANTES)
    d5 = showTime(d4, time())

    print("\nnettoyage marketing")
    nettoyage_marketing(Donnees.MARKETING, Donnees.VALEURS_MANQUANTES)
    showTime(d5, time())


if __name__ == "__main__":
    from time import time
    print ("debut nettoyage")
    debut = time()
    netoyage_donnees(debut)
    print ("\nfin nettoyage")
    showTime(debut, time())
