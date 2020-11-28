IFS=$'\n'
mkdir -p ../Donnees_Concessionnaire
cd ../Donnees_Concessionnaire
for i in ../Donnees_Brut/*.zip
do
      for n in $(unzip -Z -1 "$i"); do 
          echo "$i - $n"
          unzip "$i" "$n"
      done
done