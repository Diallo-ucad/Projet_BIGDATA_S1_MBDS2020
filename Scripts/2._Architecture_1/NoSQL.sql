execute 'drop table CATALOGUE_Groupe4';
execute 'drop table CLIENTS_3_Groupe4';
execute 'drop table CLIENTS_11_Groupe4';
execute 'drop table CO2_Groupe4';
execute 'drop table IMMATRICULATION_Groupe4';
execute 'drop table MARKETING_Groupe4';


execute  'CREATE TABLE CATALOGUE_Groupe4(
	MARQUE 		STRING, 
	NOM 		STRING,
	PUISSANCE 	INTEGER,
	LONGUEUR 	STRING, 
	NB_PLACES 	INTEGER,
	NB_PORTES 	INTEGER,
	COULEUR 	STRING, 
	OCCASION 	BOOLEAN,
	PRIX 		INTEGER
)';

execute  'CREATE TABLE CLIENTS_3_Groupe4(
	AGE 					INTEGER, 
	SEXE 					STRING,
	TAUX 					INTEGER,
	SITUATION_FAMILIALE 	STRING, 
	NB_ENFANT_A_CHARGE 		INTEGER,
	2_EME_VOITURE 			BOOLEAN,
	IMMATRICULATION 		STRING
)';

execute  'CREATE TABLE CLIENTS_11_Groupe4(
	AGE 					INTEGER, 
	SEXE 					STRING,
	TAUX 					INTEGER,
	SITUATION_FAMILIALE 	STRING, 
	NB_ENFANT_A_CHARGE 		INTEGER,
	2_EME_VOITURE 			BOOLEAN,
	IMMATRICULATION 		STRING
)';

execute  'CREATE TABLE CO2_Groupe4(
	MARQUE_MODELE 	STRING, 
	BONUS_MALUS 	INTEGER,
	REJETS_CO2 		INTEGER,
	COUT_ENERGIE 	STRING 
)';

execute  'CREATE TABLE IMMATRICULATION_Groupe4(
	IMMATRICULATION 		STRING, 
	MARQUE 					STRING,
	NOM 					INTEGER,
	PUISSANCE 				STRING, 
	LONGUEUR 				INTEGER,
	NB_PLACES 				INTEGER,
	NB_PORTES 				INTEGER, 
	COULEUR					STRING,
	OCCASION 				BOOLEAN,
	PRIX 					INTEGER
)';

execute  'CREATE TABLE MARKETING_Groupe4(
	AGE 					INTEGER, 
	SEXE 					STRING,
	TAUX 					INTEGER,
	SITUATION_FAMILIALE 	STRING, 
	NB_ENFANT_A_CHARGE 		INTEGER,
	2_EME_VOITURE 			BOOLEAN
)';