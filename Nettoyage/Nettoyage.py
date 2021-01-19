
import os
import pandas as pd
import Donnees

# Chemin de l'enregistrement des fichiers netoyes
DOSSIER_DONNEES_P = os.path.realpath("..").replace('\\', '/') + "/Donnees_Propres/"

# Creation du dossier de stockage des donnees propres si non existant
try:
    os.mkdir(DOSSIER_DONNEES_P)
except OSError:
    pass


# Netoyage du fichier Catalogue.csv
# ----------------------------------------------------------------------------
def nettoyage_catalogue(fichier, valeurs_manquantes, valeurs_incorrectes, index=False, encoding='latin-1'):

    # Stockage des donnees du fichier dans la variable donnee et remplacement
    # des valeurs manquantes par "NaN" (reconnue par panda)
    donnees = pd.read_csv(fichier, na_values=valeurs_manquantes["NaN"],
                          encoding=encoding)
    donnees = donnees.dropna()

    colonnes_a_modifier = ["longueur", "marque"]
    indices_longueur = []
    indice_hyundai = []
    indices_longueur += donnees.index[donnees[colonnes_a_modifier[0]].isin(valeurs_incorrectes.get_key("tres longue"))].tolist()
    indice_hyundai += donnees.index[donnees[colonnes_a_modifier[1]].isin(valeurs_incorrectes.get_key("Hyundai"))].tolist()

    indices = {colonnes_a_modifier[0]: indices_longueur, colonnes_a_modifier[1]: indice_hyundai}

    # Correction des valeurs
    for colonne in colonnes_a_modifier:
        for c in indices[colonne]:
            k = donnees[colonne][c]
            donnees.at[c, colonne] = valeurs_incorrectes[k]

    # Suppression doublons
    donnees = donnees.drop_duplicates()

    # Ecriture des donnees dans un nouveau fichier CSV
    donnees.to_csv(DOSSIER_DONNEES_P + fichier.split("/")[-1], index=index,
                   encoding=encoding)


# Netoyage des fichiers Clients_n.csv
# ----------------------------------------------------------------------------
def nettoyage_clients(fichier, valeurs_manquantes, valeurs_incorrectes,
                      index=False, encoding='latin-1'):

    donnees = pd.read_csv(fichier, na_values=valeurs_manquantes["NaN"],
                          encoding=encoding)

    # Renommage colonne "2eme voiture" en "deuxieme_voiture"
    donnees = donnees.rename(columns={"2eme voiture": "deuxiemeVoiture"})
    donnees = donnees.dropna()

    colonnes_a_modifier = ["sexe", "situationFamiliale"]

    indices_sexe = []
    indices_situationFamiliale = []

    # Stockage des indices des valeurs a modifier
    indices_sexe += donnees.index[donnees[colonnes_a_modifier[0]].isin(valeurs_incorrectes.get_key("F"))].tolist()
    indices_sexe += donnees.index[donnees[colonnes_a_modifier[0]].isin(valeurs_incorrectes.get_key("M"))].tolist()
    indices_situationFamiliale += donnees.index[donnees[colonnes_a_modifier[1]].isin(valeurs_incorrectes.get_key("Celibataire"))].tolist()
    indices_situationFamiliale += donnees.index[donnees[colonnes_a_modifier[1]].isin(valeurs_incorrectes.get_key("Divorce"))].tolist()
    indices_situationFamiliale += donnees.index[donnees[colonnes_a_modifier[1]].isin(valeurs_incorrectes.get_key("Marie"))].tolist()

    indices = {colonnes_a_modifier[0]: indices_sexe, colonnes_a_modifier[1]: indices_situationFamiliale}

    for colonne in colonnes_a_modifier:
        for c in indices[colonne]:
            k = donnees[colonne][c]
            donnees.at[c, colonne] = valeurs_incorrectes[k]

    # Convertion des entiers en int (transformee en float lors de la lecture du fichier)
    donnees["age"] = donnees["age"].astype(dtype=pd.Int64Dtype())
    donnees["taux"] = donnees["taux"].astype(dtype=pd.Int64Dtype())
    donnees["nbEnfantsAcharge"] = donnees["nbEnfantsAcharge"].astype(dtype=pd.Int64Dtype())

    donnees = donnees.drop_duplicates()
    donnees.to_csv(DOSSIER_DONNEES_P + fichier.split("/")[-1], index=index,
                   encoding=encoding)


# Netoyage du fichier CO2.csv
# ----------------------------------------------------------------------------
def nettoyage_co2(fichier, valeurs_manquantes, index=False, encoding='utf16'):

    # Suppression de la colonne index (Unnamed)
    donnees = pd.read_csv(fichier, index_col=[0],
                          na_values=valeurs_manquantes["NaN"])

    donnees = donnees.dropna()

    donnees = donnees.drop_duplicates()

    # Encodage en utf16 pour les caracteres non reconnu
    donnees.to_csv(DOSSIER_DONNEES_P + fichier.split("/")[-1], index=index,
                   encoding=encoding)


# Netoyage du fichier Immatriculations.csv
# ----------------------------------------------------------------------------
def nettoyage_immatriculations(fichier, valeurs_manquantes, valeurs_incorrectes, index=False,
                               encoding='latin-1'):

    donnees = pd.read_csv(fichier, na_values=valeurs_manquantes["NaN"],
                          encoding=encoding)

    donnees = donnees.dropna()

    colonne_a_modifier = "longueur"
    indices_longueur = donnees.index[donnees[colonne_a_modifier].isin(valeurs_incorrectes.get_key("tres longue"))]\
        .tolist()

    donnees.dropna()
    for c in indices_longueur:
        k = donnees[colonne_a_modifier][c]
        donnees.at[c, colonne_a_modifier] = valeurs_incorrectes[k]

    donnees = donnees.drop_duplicates()

    donnees.to_csv(DOSSIER_DONNEES_P + fichier.split("/")[-1], index=index,
                   encoding=encoding)


# Netoyage du fichier Marketing.csv
# ----------------------------------------------------------------------------
def nettoyage_marketing(fichier, valeurs_manquantes, valeurs_incorrectes,
                        index=False, encoding='latin-1'):

    donnees = pd.read_csv(fichier, na_values=valeurs_manquantes["NaN"],
                          encoding=encoding)

    donnees = donnees.rename(columns={"2eme voiture": "deuxiemeVoiture"})

    colonne_a_modifier = "situationFamiliale"

    indices_situationFamiliale = donnees.index[donnees[colonne_a_modifier].isin(valeurs_incorrectes.get_key("Celibataire"))].tolist()

    for c in indices_situationFamiliale:
        k = donnees[colonne_a_modifier][c]
        donnees.at[c, colonne_a_modifier] = valeurs_incorrectes[k]


    donnees = donnees.drop_duplicates()

    donnees.to_csv(DOSSIER_DONNEES_P + fichier.split("/")[-1], index=index,
                   encoding=encoding)


def show_time(deb, fin):
    print("Temps d execution : " + str(fin - deb) + " s")

    return fin


# Execution des fonctions de nettoyage
# ----------------------------------------------------------------------------
def netoyage_donnees(d):
    print("\nnettoyage catalogue")
    nettoyage_catalogue(Donnees.CATALOGUE, Donnees.VALEURS_MANQUANTES, Donnees.VALEURS_CLIENTS_INCORRECTES)
    d1 = show_time(d, time())

    print("\nnettoyage clients 3")
    nettoyage_clients(Donnees.CLIENTS_3, Donnees.VALEURS_MANQUANTES, Donnees.VALEURS_CLIENTS_INCORRECTES)
    d2 = show_time(d1, time())

    print("\nnettoyage clients 11")
    nettoyage_clients(Donnees.CLIENTS_11, Donnees.VALEURS_MANQUANTES, Donnees.VALEURS_CLIENTS_INCORRECTES)
    d3 = show_time(d2, time())

    print("\nnettoyage co2")
    nettoyage_co2(Donnees.CO2, Donnees.VALEURS_MANQUANTES)
    d4 = show_time(d3, time())

    print("\nnettoyage immatriculations")
    nettoyage_immatriculations(Donnees.IMMATRICULATIONS, Donnees.VALEURS_MANQUANTES, Donnees.VALEURS_CLIENTS_INCORRECTES)
    d5 = show_time(d4, time())

    print("\nnettoyage marketing")
    nettoyage_marketing(Donnees.MARKETING, Donnees.VALEURS_MANQUANTES, Donnees.VALEURS_CLIENTS_INCORRECTES)
    show_time(d5, time())


if __name__ == "__main__":
    from time import time

    print("Debut nettoyage")
    debut = time()
    netoyage_donnees(debut)
    print("\nFin nettoyage")
    show_time(debut, time())
