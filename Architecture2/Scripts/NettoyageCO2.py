import sys

from pyspark.sql import SparkSession, functions

NOMS = ["Marque", "Bonus / Malus", "Rejets CO2 g/km", "Cout energie"]


def quiet_logs(sc):
    """
    Limite l'affichage des logs.
    :param sc: Le SparkSession
    """

    logger = sc._jvm.org.apache.log4j
    logger.LogManager.getLogger("org").setLevel(logger.Level.ERROR)
    logger.LogManager.getLogger("akka").setLevel(logger.Level.ERROR)


def nettoyage_co2(data):
    """
    Netoyage du fichier co2.csv avant le map reduce:
      - Suppression du modele dans la colonne "Marque / Modele"
      - Suppression de caracteres inutiles et convertion des valeurs
        des colonnes "Bonus / Malus", "Rejets CO2 g/km", "Cout energie"
        en int.
    :param data: Dataframe du fichier csv
    :return data_m : Un nouveau dataFrame netoye
    """

    # Split nos marques et cree une nouvelle colonne Marque
    split_col = functions.split(data['Marque / Modele'], ' ')
    data_m = data.withColumn("Marque", split_col.getItem(0))

    # Supprime la colonne Marque / Modele
    data_m = data_m.drop('Marque / Modele')

    # Renomme la colonne Cout enerie en Cout energie
    data_m = data_m.withColumnRenamed('Cout enerie', NOMS[3])

    # Rerganise le tabbleau selon la liste des noms de olonnes
    data_m = data_m.select(NOMS)

    # Convertion de la colone Rejets CO2 en int
    data_m = data_m.withColumn(NOMS[2], data_m[NOMS[2]].cast("Integer"))

    # COLONNE ENERGIE
    # ===========================================================================

    # Split et convertie de la colonne Cout Energie en int
    split_energie = functions.split(data_m[NOMS[3]], "\\xa0")
    data_m = data_m.withColumn(NOMS[3], split_energie.getItem(0))
    data_m = data_m.withColumn(NOMS[3], data_m[NOMS[3]].cast("Integer"))

    # COLONNE BONUS /MALUS
    # ===========================================================================

    # Split et convertie de la colonne Bonus / Malus en int
    split_BM = functions.split(data_m[NOMS[1]], "\\xa0")

    # Creation de 2 nouvelles colonnes contenant les valeurs splittees (a:-6, b:000e)
    data_m = data_m.withColumn("a", split_BM.getItem(0)).withColumn("b", split_BM.getItem(1))

    # Split du caractere bizarre representant l'euro
    split_BMA = functions.split(data_m["b"], "\\u20ac")

    # Remplace l'ancienne colonne b, par une nouvelle colonne b sans l'euro
    data_m = data_m.withColumn("b", split_BMA.getItem(0))

    # Fusion nos 2 colonnes a et b en ecrasant la colonne Bonus / Malus
    data_m = data_m.withColumn(NOMS[1], functions.concat(functions.col("a"), functions.lit(""), functions.col("b")))
    data_m = data_m.withColumn(NOMS[1], data_m[NOMS[1]].cast("Integer"))

    # Suppression des colonnes a et b
    data_m = data_m.drop("a")
    data_m = data_m.drop("b")

    data_m.show()

    print(data_m.dtypes)

    return data_m


if __name__ == "__main__":
    reload(sys)
    sys.setdefaultencoding('utf8')

    # Crzation du point d'entree de la session
    spark = SparkSession \
        .builder \
        .appName("Python Spark SQL basic example") \
        .config("spark.some.config.option", "some-value") \
        .getOrCreate()

    # Limitation des logs
    quiet_logs(spark)

    # Chargement des donnees du fichier csv dans un dataFrame et nettoyage
    DATA = spark.read.csv("file:///home/mbds/CO2.csv", header=True, sep=",")
    DATA = nettoyage_co2(DATA)
