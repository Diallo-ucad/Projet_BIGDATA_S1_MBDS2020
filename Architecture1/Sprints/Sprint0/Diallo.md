## Choix et Utilisation d'Atlas MongoDB (Solution cloud)
# Installations effectuées: 
    -Mongo shell
    -MongoDB Compass
# Utilisations: 
    -Création d'un compte sur https://cloud.mongodb.com/
    -Connexion et deploiement d'un Cluster TPAMBDSG4Client11 
    -Géneration d'une adresse IP pour le cluster 46.193.0.228
    -Création d'un compte utilisateur (identifiant et mot de passe) "user: tpambdsg4/mdp:DIALLO2B2001" pard defaut
    -Création d'une base de données sample_client11 pour abriter le fichier client11.csv
    -Création d'une collection Client11
# Connexion à distance
    -MongoDB Compass:
        mongodb+srv://tpambdsg4:DIALLO2B2001@tpambdsg4client11.m7r9v.mongodb.net/sample_client11
    -Mongo shell
        mongo "mongodb+srv://tpambdsg4client11.m7r9v.mongodb.net/sample_client11" --username tpambdsg4
        saisir le mdp sur l'invite de commande: DIALLO2B2001
# Chargement des données de client11.csv
    -MongoDB Compass: 
        se connecter sur le cluster + sample_client11 + Documents + ADD DATA + Import file + choisir le fichier client11.csv
    -MongoDB shell
        mongoimport --host=tpambdsg4client11-shard-00-02.m7r9v.mongodb.net:27017 --db=sample_client11 --collection=client11 --type=csv --file=Clients_3.csv --authenticationDatabase=admin --ssl --username=tpambdsg4 --password=DIALLO2B2001 --headerline

        

