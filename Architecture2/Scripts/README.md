# Connection à la base en SSH
    IP address: 134.59.152.111
    Port: 443
# Création du dossier /bigDataProject2020Groupe4
    hdfs dfs -mkdir /bigDataProject2020Groupe4
# Insertion des fichiers dans hdfs /bigDataProject2020Groupe4
lancer le script 'script_insertion_hdfs.sh' avec comme argument votre username.
Exemple: user abdallah
    sh ./Scripts/3._Architecture_2/script_insertion_fichiers.sh abdallah
Un mot de passe vous sera demandé au cours de l'exécution du script.

