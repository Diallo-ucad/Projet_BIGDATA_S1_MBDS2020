import os


class LazyDict(dict):
    def keylist(self, keys, value):
        for key in keys:
            self[key] = value

    def get_key(self, value):
        return tuple([key for key, values in self.items() if values == value])


DOSSIER_DONNEES_CS = os.path.realpath("..").replace('\\', '/') + "/Donnees_Concessionnaire/"
CATALOGUE = DOSSIER_DONNEES_CS + "Catalogue.csv"
CLIENTS_3 = DOSSIER_DONNEES_CS + "Clients_3.csv"
CLIENTS_11 = DOSSIER_DONNEES_CS + "Clients_11.csv"
CO2 = DOSSIER_DONNEES_CS + "CO2.csv"
IMMATRICULATIONS = DOSSIER_DONNEES_CS + "Immatriculations.csv"
MARKETING = DOSSIER_DONNEES_CS + "Marketing.csv"

VALEURS_MANQUANTES = {"NaN": ("?", " ", "N/D", "-", "-1")}

VALEURS_CLIENTS_INCORRECTES = LazyDict()
VALEURS_CLIENTS_INCORRECTES.keylist(["Féminin", "Femme"], "F")
VALEURS_CLIENTS_INCORRECTES.keylist(["Masculin", "Homme"], "M")
VALEURS_CLIENTS_INCORRECTES.keylist(["Seule", "Seul", "Célibataire"], "Celibataire")
VALEURS_CLIENTS_INCORRECTES.keylist(["Divorcée"], "Divorce")
VALEURS_CLIENTS_INCORRECTES.keylist(["Marié(e)"], "Marie")
VALEURS_CLIENTS_INCORRECTES.keylist(["très longue"], "tres longue")
