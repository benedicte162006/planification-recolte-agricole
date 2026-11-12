import pandas as pd

# =========================================================
# Classe représentant un travailleur
# =========================================================
class Worker:

    def __init__(self, id, first_name, last_name,start_day, end_day, efficiency):

        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.start_day = start_day
        self.end_day = end_day
        self.efficiency = efficiency

    # Retourne l'identifiant
    def get_id(self):
        return self.id

    # Retourne le prénom
    def get_first_name(self):
        return self.first_name

    # Retourne le nom
    def get_last_name(self):
        return self.last_name

    # Retourne l'heure de début
    def get_start_day(self):
        return self.start_day

    # Retourne l'heure de fin
    def get_end_day(self):
        return self.end_day

    # Retourne l'efficacité
    def get_efficiency(self):
        return self.efficiency


# =========================================================
# Classe gérant l'ensemble des travailleurs
# =========================================================
class Workers:

    def __init__(self):

        # Lecture du fichier Excel
        self.df = pd.read_excel("Annexe/Annexe2.xlsx")

        # Dictionnaire contenant les travailleurs
        self.works = {}

        # Chargement des travailleurs
        self.charger_workers()

    # =====================================================
    # Lecture du fichier Excel et création des objets Worker
    # =====================================================
    def charger_workers(self):

        for index, row in self.df.iterrows():

            work = Worker(
                row['ID'],
                row['FIRST NAME'],
                row['LAST NAME'],
                row['START DAY'],
                row['END DAY'],
                row['EFFICIENCY']
            )

            self.works[row['ID']] = work

    # =====================================================
    # Retourne un travailleur à partir de son identifiant
    # =====================================================
    def get_worker(self, worker_id):

        return self.works.get(worker_id)