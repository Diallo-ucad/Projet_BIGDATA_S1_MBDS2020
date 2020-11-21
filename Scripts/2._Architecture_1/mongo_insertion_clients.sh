cd "$(dirname "$0")"
cd ../../Donnees_Propres
ls
mongoimport --host=tpambdsg4client11-shard-00-02.m7r9v.mongodb.net:27017 --db=sample_client11 --collection=Client11 --type=csv --file=Clients_11.csv --authenticationDatabase=admin --ssl --username=tpambdsg4 --password=DIALLO2B2001 --headerline