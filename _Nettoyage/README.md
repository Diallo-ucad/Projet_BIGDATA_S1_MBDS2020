## NETTOYAGE DES DONNES

### Bibliothèques
Utilisation de la librairie [Panda](https://pandas.pydata.org/) permettant
la manipulation de données étiquetée par des colonnes et des lignes.
<br>[Documentation](https://pandas.pydata.org/docs/pandas.pdf).

### Lancement du script
Dans un shell : 
-   sh script_1_init.sh

Ce scipt permettra l'installation de bibliothèques Python nécessaires
au néttoyage, de dézipper les fichiers de données à nettoyer se trouvant
dans le répertoire "Donnee_Brut" et de créer les nouveaux fichiers nétoyés
dans un répertoire nommé "Donnes_Propres".

### Le Nettoyage
#### Liste des valeurs non définies:
    - ?, " ", N/D, -, -1                                        -> NaN
    
#### Catlogue.csv et Immatriculation.csv
    - Colonne "longuer" : très longue                           -> tres longue

#### Clients_n.csv
    - Renommage nom de colonne "2eme voiture" en "DeuxiemeVoiture"
    
    - Colonne "Sexe" :               [Féminin, Femme]           -> F
                                     [Masculin, Homme]          -> M
                                     
    - Colonne "situationFamiliale" : [Seule, Seul, Célibataire] -> Celibataire
                                      Divorcée                  -> Divorce
                                      Marié(e)                  -> Marie
                 
#### Marketing.csv
    - Renommage nom de colonne "2eme voiture" en "deuxiemeVoiture"
    
    - Colonne "situationFamiliale" : Célibataire                -> Celibataire