## Creation des tables et Insertions des tables dans ORACLE

## Etape0 

lancer 2 terminals

## Etape1

Dans le premier terminal 

Se connecter sur la machine : ip = 134.59.152.111

## Etape2 

Dans le premier terminal

Créer un dossier bigDataProject2020Groupe4/

mkdir /bigDataProject2020Groupe4/

Grâce à WinSCP deplacer le fichier client_3.csv dans le dossier bigDataProject2020Groupe4/

## Etape3

Dans le 2ème terminal

Lancer les commandes
sql> sqlplus username2B20@orcl/username2B2001
sql> connect username@orcl/motDepasse (  exemple connect niteka@orcl/niteka14)

## Etape4

Dans le 2ème terminal

Lancer la commande
sql> CREATE TABLE CLIENTS_3_Groupe4 
(
    age                     number(3), 
    sexe                     varchar2(2),
    taux                     number(6),
    situationFamiliale     varchar2(10), 
    nbEnfantsAcharge         number(3),
    deuxiemeVoiture     varchar2(5),
    immatriculation         varchar2(20)
);


## Etape5

Dans le premier terminal

Créer un fichier client_3.ctl 
copie le script suivant : 

LOAD DATA
INFILE 'Clients_3.csv'
INTO TABLE CLIENTS_3_Groupe4
FIELDS TERMINATED BY ','
(age,sexe,taux,situationFamiliale,nbEnfantsAcharge,deuxiemeVoiture,immatriculation)


## Etape6

Dans le premier terminal

Lancer la commande pour importer les données
[niteka@bigdatalite bigDataProject2020Groupe4/]$ sqlldr NITEKA2B20@ORCL/NITEKA2B2001 CONTROL=client_3.ctl LOG=client_3.log BAD=clients_3.bad
