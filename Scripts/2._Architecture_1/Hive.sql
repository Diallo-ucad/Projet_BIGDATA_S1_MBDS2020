

CREATE EXTERNAL TABLE CATALOGUE_Groupe4_ONS_H_EXT (
	MARQUE 		STRING, 
	NOM 		STRING,
	PUISSANCE 	INT,
	LONGUEUR 	STRING, 
	NB_PLACES 	INT,
	NB_PORTES 	INT,
	COULEUR 	STRING, 
	OCCASION 	BOOLEAN,
	PRIX 		INT)
STORED BY 'oracle.kv.hadoop.hive.table.TableStorageHandler'
TBLPROPERTIES (
"oracle.kv.kvstore" = "kvstore",
"oracle.kv.hosts" = "bigdatalite.localdomain:5000", 
"oracle.kv.hadoop.hosts" = "bigdatalite.localdomain/127.0.0.1", 
"oracle.kv.tableName" = "CATALOGUE_Groupe4");


CREATE EXTERNAL TABLE CLIENTS_3_Groupe4_ONS_H_EXT (
	AGE 					INT, 
	SEXE 					STRING,
	TAUX 					INT,
	SITUATION_FAMILIALE 	STRING, 
	NB_ENFANT_A_CHARGE 		INT,
	2_EME_VOITURE 			BOOLEAN,
	IMMATRICULATION 		STRING)
STORED BY 'oracle.kv.hadoop.hive.table.TableStorageHandler'
TBLPROPERTIES (
"oracle.kv.kvstore" = "kvstore",
"oracle.kv.hosts" = "bigdatalite.localdomain:5000", 
"oracle.kv.hadoop.hosts" = "bigdatalite.localdomain/127.0.0.1", 
"oracle.kv.tableName" = "CLIENTS_3_Groupe4");


CREATE EXTERNAL TABLE CLIENTS_11_Groupe4_ONS_H_EXT (
	AGE 					INT, 
	SEXE 					STRING,
	TAUX 					INT,
	SITUATION_FAMILIALE 	STRING, 
	NB_ENFANT_A_CHARGE 		INT,
	2_EME_VOITURE 			BOOLEAN,
	IMMATRICULATION 		STRING)
STORED BY 'oracle.kv.hadoop.hive.table.TableStorageHandler'
TBLPROPERTIES (
"oracle.kv.kvstore" = "kvstore",
"oracle.kv.hosts" = "bigdatalite.localdomain:5000", 
"oracle.kv.hadoop.hosts" = "bigdatalite.localdomain/127.0.0.1", 
"oracle.kv.tableName" = "CLIENTS_11_Groupe4");


CREATE EXTERNAL TABLE CO2_Groupe4_ONS_H_EXT (
	MARQUE_MODELE 	STRING, 
	BONUS_MALUS 	INT,
	REJETS_CO2 		INT,
	COUT_ENERGIE 	STRING )
STORED BY 'oracle.kv.hadoop.hive.table.TableStorageHandler'
TBLPROPERTIES (
"oracle.kv.kvstore" = "kvstore",
"oracle.kv.hosts" = "bigdatalite.localdomain:5000", 
"oracle.kv.hadoop.hosts" = "bigdatalite.localdomain/127.0.0.1", 
"oracle.kv.tableName" = "CO2_Groupe4");


CREATE EXTERNAL TABLE IMMATRICULATION_Groupe4_ONS_H_EXT (
	IMMATRICULATION 		STRING, 
	MARQUE 					STRING,
	NOM 					INT,
	PUISSANCE 				STRING, 
	LONGUEUR 				INT,
	NB_PLACES 				INT,
	NB_PORTES 				INT, 
	COULEUR					STRING,
	OCCASION 				BOOLEAN,
	PRIX 					INT)
STORED BY 'oracle.kv.hadoop.hive.table.TableStorageHandler'
TBLPROPERTIES (
"oracle.kv.kvstore" = "kvstore",
"oracle.kv.hosts" = "bigdatalite.localdomain:5000", 
"oracle.kv.hadoop.hosts" = "bigdatalite.localdomain/127.0.0.1", 
"oracle.kv.tableName" = "IMMATRICULATION_Groupe4");


CREATE EXTERNAL TABLE MARKETING_Groupe4_ONS_H_EXT (
	AGE 					INT, 
	SEXE 					STRING,
	TAUX 					INT,
	SITUATION_FAMILIALE 	STRING, 
	NB_ENFANT_A_CHARGE 		INT,
	2_EME_VOITURE 			BOOLEAN)
STORED BY 'oracle.kv.hadoop.hive.table.TableStorageHandler'
TBLPROPERTIES (
"oracle.kv.kvstore" = "kvstore",
"oracle.kv.hosts" = "bigdatalite.localdomain:5000", 
"oracle.kv.hadoop.hosts" = "bigdatalite.localdomain/127.0.0.1", 
"oracle.kv.tableName" = "MARKETING_Groupe4");