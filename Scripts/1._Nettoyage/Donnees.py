#!/usr/bin/python
# -*- coding: latin-1 -*-
import os

class LazyDict(dict):
    def keylist(self, keys, value):
        for key in keys:
            self[key] = value

DOSSIER_DONNEES_CS = os.path.realpath("..").replace('\\', '/') + "/Donnees_Concessionnaire/"
CATALOGUE = DOSSIER_DONNEES_CS + "Catalogue.csv"
CLIENTS_3 = DOSSIER_DONNEES_CS + "Clients_3.csv"
CLIENTS_11 = DOSSIER_DONNEES_CS + "Clients_11.csv"
CO2 = DOSSIER_DONNEES_CS + "CO2.csv"
IMMATRICULATIONS = DOSSIER_DONNEES_CS + "Immatriculations.csv"
MARKETING = DOSSIER_DONNEES_CS + "Marketing.csv"

VALEURS_MANQUANTES = {"NaN": ("?", " ", "N/D", "-")}

VALEURS_CLIENTS_INCORECTES = LazyDict()
VALEURS_CLIENTS_INCORECTES.keylist(("Féminin", "Femme", "F"), "F")
VALEURS_CLIENTS_INCORECTES.keylist(("Masculin", "Homme", "M"), "M")
VALEURS_CLIENTS_INCORECTES.keylist(("Seule", "Seul", "Célibataire"), "Célibataire")
