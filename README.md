
# Planification des récoltes agricoles

## Présentation du projet

Ce projet consiste à développer un programme en Python permettant de planifier les récoltes de plusieurs champs agricoles en fonction de leur superficie, du temps de travail et des disponibilités des ouvriers.

L'objectif est d'organiser automatiquement les journées de récolte afin de répartir le travail entre les ouvriers et de réduire la durée totale des opérations.

## Objectifs

- Automatiser la création d'un planning de récolte.
- Calculer le temps nécessaire pour récolter chaque champ.
- Prendre en compte les horaires et les capacités de travail des ouvriers.
- Organiser le travail individuellement ou en équipe.
- Représenter graphiquement la répartition des récoltes.

## Fonctionnement du programme

Le programme s'appuie sur deux fichiers Excel contenant les informations relatives aux champs et aux ouvriers.

Les principales étapes sont :

1. Importation des données depuis les fichiers Excel.
2. Création des objets représentant les champs et les ouvriers.
3. Calcul du temps nécessaire pour chaque récolte.
4. Génération automatique du planning journalier.
5. Affichage du planning et représentation graphique des résultats.

## Technologies utilisées

- Python
- Pandas
- NumPy
- Matplotlib
- Excel

## Organisation des fichiers

- `fields.py` : gestion des champs agricoles.
- `worker.py` : gestion des ouvriers.
- `calculs.py` : calcul des temps de travail et génération du planning.
- `affichage_planning.py` : affichage du planning.
- `graphique.py` : visualisation graphique des récoltes.
- `programme_main.py` : programme principal.

## Résultats

Le programme permet de planifier la récolte de 60 champs en environ 11 jours, grâce à une organisation du travail individuel et collectif selon les caractéristiques des champs.

## Pistes d'amélioration

- Ajouter une interface graphique.
- Exporter automatiquement le planning vers Excel.
- Intégrer des méthodes d'optimisation plus avancées.
- Ajouter des statistiques complémentaires.

## Auteur

**MADJITESSEM Bénédicte**

Bachelor Business Data Science — UCO Angers
