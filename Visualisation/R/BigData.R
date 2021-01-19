setwd(dirname(rstudioapi::getActiveDocumentContext()$path))
library(wordcloud)
library(tidyverse)
library(scales)
library(RColorBrewer)
library(jsonlite)


# Importation des fichiers nécessaires
# ==============================================================================
CLIENTS3 <- read_csv('../../Donnees_Propres/Clients_3.csv')
CLIENTS11 <- read_csv('../../Donnees_Propres/Clients_11.csv')

# Fusion des fichiers [CLIENTS3, CLIENTS11] et suppressionn des doublons
CLIENTS = unique(rbind(CLIENTS3, CLIENTS11))
IMMATRICULATIONS <- read_csv('../../Donnees_Propres/Immatriculations.csv')


# ==============================================================================
# ================================ HISTOGRAMME =================================
# ==============================================================================

# Nombre de voiture achetees par marques par les clients selon leur situation
# familiale
# ==============================================================================

col_situation <- CLIENTS %>% select(situationFamiliale, immatriculation)
col_immatriculation_m <- select(IMMATRICULATIONS, immatriculation, marque)

join_situation_immatriculation_m <- inner_join(col_situation, col_immatriculation_m,
                                               by="immatriculation")
variables_histogramme <- join_situation_immatriculation_m %>% 
                         group_by(situationFamiliale, marque) %>%
                         summarise(Achats=n())


# Test 1
graphe_histogramme <- ggplot(variables_histogramme) +
                      ggtitle("Nombre de voiture achetees par marques par les
                               clients selon leur situation familiale") +
                      geom_col(aes(x=marque, y=Achats, fill=situationFamiliale))
graphe_histogramme


# Test 2
graphe_histogramme <- ggplot(variables_histogramme) +
                      ggtitle("Nombre de voiture achetees par marques par les
                               clients selon leur situation familiale") +
                      geom_col(aes(x=marque, y=Achats, fill=situationFamiliale),
                               position='dodge')
graphe_histogramme


# Test 3
graphe_histogramme <- ggplot(variables_histogramme) +
                      ggtitle("Nombre de voiture achetees par marques par les
                               clients selon leur situation familiale") +
                      geom_col(aes(x=situationFamiliale, y=Achats, fill=marque), 
                               position='dodge')
graphe_histogramme

write_csv(variables_histogramme, 'Variables/Graphe1 - Histogramme.csv')
write_json(variables_histogramme, "../D3JS/Histogramme/Histogramme.json")


# ==============================================================================
# ================================= CAMEMBERT ==================================
# ==============================================================================

# Le nombre d'achat de vehicule à 5 portes selon le sexe
# ==============================================================================
col_sexe <- CLIENTS %>% select(sexe, immatriculation)
col_immatriculation_mpn <- select(IMMATRICULATIONS, immatriculation, marque, prix,
                                  nbPortes) %>% filter(nbPortes==5) 
join_sexe_immatriculation_mpn <- inner_join(col_sexe, col_immatriculation_mpn,
                                            by="immatriculation")


variables_camembert <- join_sexe_immatriculation_mpn %>%
                       group_by(sexe, nbPortes) %>%
                       summarise(Achat = n())

graphe_camembert <- ggplot(variables_camembert, aes(x="", y=Achat, fill=sexe)) +
                    geom_bar(width=1, stat="identity") +
                    coord_polar("y", start=0)
graphe_camembert

write_csv(variables_camembert, 'Variables/Graphe2 - Camembert.csv')
write_json(variables_camembert, '../D3JS/Camembert/Camembert.json')


# ==============================================================================
# =================================== LIGNES ===================================
# ==============================================================================

# Le prix moyen total et le prix moyen des véhicules achetés par les clients
# selon l'âge
# ==============================================================================

col_age <- CLIENTS %>% select(age, immatriculation)
col_immatriculation_mp <- select(IMMATRICULATIONS, immatriculation, marque, prix)
join_age_immatriculation_mp <- inner_join(col_age, col_immatriculation_mp,
                                          by="immatriculation")


# Prix Moyen Total
# ==============================================================================
variables_ligne_t <- join_age_immatriculation_mp %>%
                     group_by(age) %>%
                     summarise(PrixMoyen=mean(prix))


graphe_ligne_t <- ggplot(data=variables_ligne_t, aes(y=PrixMoyen, x=age)) +
                  geom_line(size=1) +
                  geom_point(size=2.5)
graphe_ligne_t

write_csv(variables_ligne_t, 'Variables/Graphe3 - Ligne - Prix Moyen Total.csv')
write_json(variables_ligne_t, '../D3JS/Lignes/Ligne - Prix Moyen Total.json')


# Prix Moyen Total par marque
# ==============================================================================
variables_ligne_tm <- join_age_immatriculation_mp %>%
                                group_by(age, marque) %>%
                                summarise(PrixMoyenMarque=mean(prix))
variables_ligne_tm <- distinct_all(variables_ligne_tm)



graphe_ligne_tm <- ggplot(data=variables_ligne_tm, aes(y=PrixMoyenMarque, x=age,
                                                       group=marque, colour=marque)) +
                   geom_line(size=0.7) +
                   geom_point(size=1.2)
graphe_ligne_tm

write_csv(variables_ligne_tm, 'Variables/Graphe3 - Ligne - Prix Moyen Total Marque.csv')
write_json(variables_ligne_tm, '../D3JS/Lignes/Ligne - Prix Moyen Total Marque.json')


# ==============================================================================
# ============================== NUAGE DE POINTS ===============================
# ==============================================================================

# Le nombre de clients total et prix moyens des véhicules achetés selon l'âge
# ==============================================================================
variables_nuage_points <- join_age_immatriculation_mp %>%
                          group_by(age) %>%
                          summarise(PrixMoyen=mean(prix), NombreClients=n())

graphe_nuage <- ggplot(variables_nuage_points, aes(x=age, y=PrixMoyen,
                                                   group=NombreClients))+
                geom_point(aes(color=NombreClients, size=NombreClients))
graphe_nuage

write_csv(variables_nuage_points, 'Variables/Graphe4 - Nuages de points.csv')
write_json(variables_nuage_points, '../D3JS/Nuage de points/Nuages de points.json')


# ==============================================================================
# ============================== NUAGE DE TEXTES ===============================
# ==============================================================================

# Le nombre de voiture vendu par prix selon le taux moyen du client
# ==============================================================================
col_taux <- CLIENTS %>% select(immatriculation, taux)
join_taux_immatriculation_m <- inner_join(col_taux, col_immatriculation_m,
                                         by="immatriculation")

variables_nuage_textes <- join_taux_immatriculation_m %>%
                          group_by(marque) %>%
                          summarise(TauxMoyen=mean(taux), NombreMarque=n())

wordcloud(words=variables_nuage_textes$marque,
          freq=variables_nuage_textes$NombreMarque, min.freq=1, max.words=200,
          random.order=FALSE, rot.per=0.35, colors=brewer.pal(8, "Dark2"))

write_csv(variables_nuage_textes, 'Variables/Graphe5 - Nuages de textes.csv')
write_json(variables_nuage_textes, '../D3JS/Nuage de textes/Nuages de textes.json')
