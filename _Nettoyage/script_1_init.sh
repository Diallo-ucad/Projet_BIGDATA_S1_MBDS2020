cd "$(dirname "$0")"
./install.sh
./unzip.sh
cp ../Donnees_brut/CO2.csv ../Donnees_Concessionnaire/CO2.csv
mkdir -p ../Donnees_Propres
python Nettoyage.py
rm -r ../Donnees_Concessionnaire