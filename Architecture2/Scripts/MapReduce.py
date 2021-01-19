import sys
from pyspark.sql import SparkSession, functions as fc

from NettoyageCO2 import *
#spark-submit --master "local[2]" MapReduce.py

if __name__ == '__main__':
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
    df_co2_brut = spark.read.csv("file:///home/mbds/spark/CO2.csv", header=True, sep=",")
    print('Dataframe CO2 brut')
    df_co2_brut.show()

    # Nettoyage des donnees CO2.csv 
    df_co2 = nettoyage_co2(df_co2_brut)
    print('Dataframe CO2 nettoye')
    df_co2.show()

    # Reduit les marques en 1 avec les moyennes Bonus / Malus, Rejets CO2 g/km et Cout energie
    df_co2 = df_co2.groupBy('Marque')\
		.agg(fc.avg('Bonus / Malus').alias('Bonus / Malus'),\
		fc.avg('Rejets CO2 g/km').alias('Rejets CO2 g/km'),\
        fc.avg('Cout energie').alias('Cout energie'))\
		.withColumnRenamed('Marque', 'MarqueCo2')
    df_co2.show()

    # Chargement des donnees du fichier csv Catalogue
    # Cree une colonne upper(marque) qui contient les marques en MAJ 
    df_cat = spark.read.csv("file:///home/mbds/spark/Catalogue.csv", header=True, sep=",")\
      .select("*", fc.upper(fc.col('marque')))

    # df : jointure de catalogue et co2 par la marque
    df_cat_co2 = df_cat.join(df_co2, df_cat['upper(marque)'] ==  df_co2['MarqueCo2'], "left")\
		.drop('upper(marque)').drop('MarqueCo2')
    df_cat_co2.show()

    # Bonus / Malus AVG: moyenne de toutes les colonnes 'Bonus / Malus'
    bmAVG = df_cat_co2.select(fc.avg("Bonus / Malus")).collect()[0]['avg(Bonus / Malus)']
    # Rejets CO2 g/km AVG: moyenne de toutes les colonnes 'Rejets CO2 g/km'
    rjAVG = df_cat_co2.select(fc.avg("Rejets CO2 g/km")).collect()[0]['avg(Rejets CO2 g/km)']
    # Cout energie AVG: moyenne de toutes les colonnes 'Cout energie'
    ceAVG = df_cat_co2.select(fc.avg("Cout energie")).collect()[0]['avg(Cout energie)']

    print('bmAVG', bmAVG)
    print('rjAVG', rjAVG)
    print('ceAVG', ceAVG)

    # Remplissage des case vides de la colonne 'Bonus / Malus' par bmAVG
    df_cat_co2 = df_cat_co2.na.fill(value = bmAVG, subset = ["Bonus / Malus"])
    # Remplissage des case vides de la colonne 'Rejets CO2 g/km' par rjAVG
    df_cat_co2 = df_cat_co2.na.fill(value = rjAVG, subset = ["Rejets CO2 g/km"])
    # Remplissage des case vides de la colonne 'Cout energie' par ceAVG
    df_cat_co2 = df_cat_co2.na.fill(value = ceAVG, subset = ["Cout energie"])
    
    # export du csv
    df_cat_co2.write.format('csv').option('header',True).mode('overwrite').option('sep',',').save('file:///home/mbds/spark/catalogue_co2')