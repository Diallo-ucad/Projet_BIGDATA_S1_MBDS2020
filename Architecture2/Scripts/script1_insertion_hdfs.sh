cd "$(dirname "$0")"
cd ../../Donnees_Propres
for i in *
do
    echo "insertion du fichier $i dans hdfs /bigDataProject2020Groupe4/a2"
    cat $i | ssh $1@134.59.152.111 -p 443 "hdfs dfs -put - /bigDataProject2020Groupe4/a2/$i"
done 