from calculs import Calculs
import matplotlib.pyplot as plt
import numpy as np


# =========================================================
# Création des graphiques d'analyse du planning
# =========================================================
def graphiques():

    # =====================================================
    # Récupération des données
    # =====================================================

    c = Calculs()

    c.calcule_number_hours()

    planning = c.planning()

    # =====================================================
    # Variables pour le graphique 1
    # Répartition matin / après-midi
    # =====================================================

    father_morning = 0
    father_afternoon = 0

    son_morning = 0
    son_afternoon = 0

    together_morning = 0
    together_afternoon = 0

    # =====================================================
    # Variables pour le graphique 2
    # Surface totale récoltée
    # =====================================================

    father_surface = 0
    son_surface = 0
    together_surface = 0

    # =====================================================
    # Calcul des hectares
    # =====================================================

    for day, moment, field_id, worker in planning:

        hectare = c.number_hours[field_id]["hectare"]

        # ==============================================
        # Graphique 1 : matin / après-midi
        # ==============================================

        if moment == "morning":

            if worker == "father":
                father_morning += hectare

            elif worker == "son":
                son_morning += hectare

            elif worker == "together":
                together_morning += hectare

        elif moment == "afternoon":

            if worker == "father":
                father_afternoon += hectare

            elif worker == "son":
                son_afternoon += hectare

            elif worker == "together":
                together_afternoon += hectare

        # ==============================================
        # Graphique 2 : surface totale
        # ==============================================

        if worker == "father":
            father_surface += hectare

        elif worker == "son":
            son_surface += hectare

        elif worker == "together":
            together_surface += hectare

    # =====================================================
    # Création de la figure
    # =====================================================

    fig, (ax1, ax2) = plt.subplots(1,2,figsize=(12, 5))

    # =====================================================
    # Graphique 1
    # Répartition des hectares selon le moment
    # =====================================================

    labels = ["Matin", "Après-midi"]

    father_values = [father_morning,father_afternoon]

    son_values = [son_morning,son_afternoon]

    together_values = [together_morning,together_afternoon]

    x = np.arange(len(labels))

    width = 0.25

    ax1.bar(x - width,father_values, width,label="Father")

    ax1.bar( x,son_values,width,label="Son")

    ax1.bar( x + width,together_values,width,label="Together")

    ax1.set_title("Répartition des hectares selon le moment de la journée")

    ax1.set_ylabel("Hectares")

    ax1.set_xticks(x)

    ax1.set_xticklabels(labels)

    ax1.legend()

    ax1.grid(axis="y",linestyle="--",alpha=0.5)

    # =====================================================
    # Graphique 2
    # Surface totale récoltée
    # =====================================================

    travailleurs = ["Father","Son","Together"]

    surfaces = [father_surface,son_surface,together_surface]

    ax2.bar(travailleurs, surfaces )

    ax2.set_title( "Surface totale récoltée par type de travail" )

    ax2.set_ylabel("Hectares")

    ax2.grid(axis="y",linestyle="--",alpha=0.5)

    # =====================================================
    # Affichage
    # =====================================================

    plt.tight_layout()

    plt.show()


graphiques()