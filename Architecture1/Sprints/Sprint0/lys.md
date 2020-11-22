## Creation des tables et Insertions des tables dans ORACLE

## Etape0 

lancer 2 terminals

## Etape1

Dans le premier terminal 

Se connecter sur la machine : ip = 134.59.152.111

## Etape2 

Dans le premier terminal

Grâce à WinSCP deplacer le fichier client_3.csv dans le dossier TPBigData

## Etape3

Dans le premier terminal

Créer un fichier client3.ctl 
copie le script suivant : 

LOAD DATA
INFILE 'Clients_3.csv'
INTO TABLE CLIENTS_3_Groupe4
FIELDS TERMINATED BY ','
(age,sexe,taux,situationFamiliale,nbEnfantsAcharge,deuxieme_voiture,immatriculation)

## Etape4

Dans le 2ème terminal

Lancer les commandes
sql> sqlplus username2B20@orcl/username2B2001
sql> connect username@orcl/motDepasse (  exemple connect niteka@orcl/niteka14)

## Etape5

Dans le 2ème terminal

Lancer la commande
sql> CREATE TABLE CLIENTS_3_Groupe4 
(
    age                     number(3), 
    sexe                     varchar2(2),
    taux                     number(6),
    situationFamiliale     varchar2(10), 
    nbEnfantsAcharge         number(3),
    Deuxieme_voiture     varchar2(5),
    immatriculation         varchar2(20)
);

## Etape6

Dans le premier terminal

Lancer la commande pour importer les données
[niteka@bigdatalite TpBigData]$ sqlldr NITEKA2B20@ORCL/NITEKA2B2001 CONTROL=client3.ctl LOG=client3.log BAD=clients_3.bad
