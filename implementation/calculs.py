from fields import Fields
from worker import Workers

# =========================================================
# Cette classe contient tous les calculs nécessaires
# pour la création de l'emploi du temps
# =========================================================

class Calculs:

    def __init__(self):

        # récupération des travailleurs
        self.wor = Workers()

        # récupération des champs
        self.fie = Fields()

        # dictionnaire contenant les heures
        self.number_hours = {}

    # =========================================================
    # Calcul du nombre d'heures pour chaque champ
    # =========================================================
    def calcule_number_hours(self):

        # récupération du père et du fils
        father = self.wor.get_worker(1)
        son = self.wor.get_worker(2)

        # parcours de tous les champs
        for field_id in self.fie.fields:

            # récupération du champ
            field = self.fie.get_field(field_id)

            # récupération du nombre d'hectares
            hectare = field.get_hectare()

            # stockage des calculs dans un dictionnaire
            self.number_hours[str(field_id)] = {

                # nombre d'hectares
                "hectare": int(hectare),

                # temps du père seul
                "father":
                float(hectare /father.get_efficiency()
                      ),

                # temps du fils seul
                "son":
                float(hectare /son.get_efficiency()
                ),

                # temps lorsqu'ils travaillent ensemble
                "together":
                float(
                    hectare /(father.get_efficiency() +son.get_efficiency())
                )
            }

        return self.number_hours

    # =========================================================
    # Création automatique du planning
    # =========================================================
    def planning(self):

        # copie du dictionnaire des champs
        field_stock = self.number_hours.copy()

        # liste finale du planning
        planning = []

        # compteur des jours
        day = 1

        # tant qu'il reste des champs
        while field_stock:

            # =================================================
            # Temps disponibles pour chaque période
            # =================================================

            # heures du matin
            father_morning = 5
            son_morning = 3

            # heures du soir
            father_afternoon = 7
            son_afternoon = 4

            # =================================================
            # MATIN
            # Le père et le fils travaillent séparément
            # =================================================

            for field_id, hours in list(field_stock.items()):

                # =============================================
                # Le père travaille seul
                # =============================================
                if hours["father"] <= father_morning:

                    planning.append([
                        day,
                        "morning",
                        field_id,
                        "father"
                    ])

                    # diminution du temps restant
                    father_morning -= hours["father"]

                    # suppression du champ terminé
                    del field_stock[field_id]

                # =============================================
                # Le fils travaille seul
                # =============================================
                elif hours["son"] <= son_morning:

                    planning.append([
                        day,
                        "morning",
                        field_id,
                        "son"
                    ])

                    # diminution du temps restant
                    son_morning -= hours["son"]

                    # suppression du champ terminé
                    del field_stock[field_id]

            # =================================================
            # SOIR
            # Travail ensemble possible
            # =================================================

            for field_id, hours in list(field_stock.items()):

                # =============================================
                # Grands champs faits ensemble
                # =============================================
                if hours["hectare"] > 35:

                    # vérification du temps disponible
                    if (
                        hours["together"] <= father_afternoon
                        and
                        hours["together"] <= son_afternoon
                    ):

                        planning.append([
                            day,
                            "afternoon",
                            field_id,
                            "together"
                        ])

                        # réduction du temps restant
                        father_afternoon -= (
                            hours["together"]
                        )

                        son_afternoon -= (
                            hours["together"]
                        )

                        # suppression du champ terminé
                        del field_stock[field_id]

                # =============================================
                # Père seul
                # =============================================
                elif hours["father"] <= father_afternoon:

                    planning.append([
                        day,
                        "afternoon",
                        field_id,
                        "father"
                    ])

                    # réduction du temps restant
                    father_afternoon -= (
                        hours["father"]
                    )

                    # suppression du champ terminé
                    del field_stock[field_id]

                # =============================================
                # Fils seul
                # =============================================
                elif hours["son"] <= son_afternoon:

                    planning.append([
                        day,
                        "afternoon",
                        field_id,
                        "son"
                    ])

                    # réduction du temps restant
                    son_afternoon -= (
                        hours["son"]
                    )

                    # suppression du champ terminé
                    del field_stock[field_id]

            # passage au jour suivant
            day += 1

        return planning