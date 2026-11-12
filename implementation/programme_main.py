from calculs import Calculs
from worker import Workers
from fields import Fields
from affichage_planning import afficher

# =========================================================
# Programme principal
# Permet d'afficher les informations des travailleurs,
# des champs et le planning généré automatiquement.
# =========================================================

if __name__ == "__main__":

    # =====================================================
    # AFFICHAGE DES TRAVAILLEURS
    # =====================================================

    w = Workers()

    print("\n======== Informations des travailleurs ========")

    for i, work in enumerate(w.works.values(), start=1):

        print(
            "Worker", i, ":",
            "ID:", work.get_id(),
            "FIRST NAME:", work.get_first_name(),
            "LAST NAME:", work.get_last_name(),
            "START DAY:", work.get_start_day(),
            "END DAY:", work.get_end_day(),
            "EFFICIENCY:", work.get_efficiency()
        )

    # =====================================================
    # AFFICHAGE DES CHAMPS
    # =====================================================

    f = Fields()

    print("\n======== Informations des champs ========")

    for i, field in enumerate(f.fields.values(), start=1):

        print(
            "Champ", i, ":",
            "ID:", field.get_id(),
            "HECTARE:", field.get_hectare()
        )

    # =====================================================
    # CALCUL ET CREATION DU PLANNING
    # =====================================================

    c = Calculs()

# Calcul des temps nécessaires
c.calcule_number_hours()


# =====================================================
# AFFICHAGE DU PLANNING
# =====================================================

# Création de l'objet Calculs
c = Calculs()

# Calcul des heures
c.calcule_number_hours()

# Création du planning
planning = c.planning()

# Affichage du planning regroupé

print("\n======== PLANNING ========")
afficher(planning)