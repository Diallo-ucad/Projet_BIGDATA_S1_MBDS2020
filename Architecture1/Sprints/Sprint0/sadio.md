# Creation du dossier architecture1 dans le dossier bigDataProject2020Groupe4
hdfs dfs -mkdir /bigDataProject2020Groupe4/architecture1

# Creation du dossier architecture2 dans le dossier bigDataProject2020Groupe4
hdfs dfs -mkdir /bigDataProject2020Groupe4/architecture2

# Deplacement du fichier CO2.csv du dossier bigDataProject2020Groupe4 vers architecture2
hdfs dfs -mv /bigDataProject2020Groupe4/CO2.csv /bigDataProject2020Groupe4/architecture2/CO2.csv

# Deplacement du fichier catalogue.csv du dossier bigDataProject2020Groupe4 vers architecture2
hdfs dfs -mv /bigDataProject2020Groupe4/catalogue.csv /bigDataProject2020Groupe4/architecture2/catalogue.csv

# Deplacement du fichier client12.csv du dossier bigDataProject2020Groupe4 vers architecture2
hdfs dfs -mv /bigDataProject2020Groupe4/client12.csv /bigDataProject2020Groupe4/architecture2/client12.csv

# Deplacement du fichier client4.csv du dossier bigDataProject2020Groupe4 vers architecture2
hdfs dfs -mv /bigDataProject2020Groupe4/client4.csv /bigDataProject2020Groupe4/architecture2/client4.csv

# Deplacement du fichier immatriculation.csv du dossier bigDataProject2020Groupe4 vers architecture1
hdfs dfs -mv /bigDataProject2020Groupe4/immatriculation.csv /bigDataProject2020Groupe4/architecture1/immatriculation.csv

