import os

DOSSIER_DONNEES_CS = os.path.realpath("../..").replace('\\', '/') + "/Donnees_Concessionnaire/"

CATALOGUE = DOSSIER_DONNEES_CS + "Catalogue.csv"
CLIENTS_3 = DOSSIER_DONNEES_CS + "Clients_3.csv"
CLIENTS_11 = DOSSIER_DONNEES_CS + "Clients_11.csv"
CO2 = DOSSIER_DONNEES_CS + "CO2.csv"
IMMATRICULATIONS = DOSSIER_DONNEES_CS + "Immatriculations.csv"
MARKETING = DOSSIER_DONNEES_CS + "Marketing.csv"

VALEURS_MANQUANTES = {"NaN": ("?", " ", "N/D", "-")}

VALEURS_CLIENTS_INCORECTES = {"F": ("Féminin", "Femme"), "M": ("Masculin", "Homme"),
                              "Célibataire": ("Seule", "Seul")}

VALEURS_CLIENTS_INCORECTES = {"F": ["Féminin", "Femme"], "M": ["Masculin", "Homme"],
                              "Célibataire": ["Seule", "Seul"]}

