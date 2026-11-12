import pandas as pd


# =========================================================
# Classe représentant un champ agricole
# Chaque objet contient un identifiant et une surface
# exprimée en hectares
# =========================================================
class Field:

    def __init__(self, id, hectare):

        self.id = id
        self.hectare = hectare

    # Retourne l'identifiant du champ
    def get_id(self):
        return self.id

    # Retourne la surface du champ
    def get_hectare(self):
        return self.hectare


# =========================================================
# Classe gérant l'ensemble des champs agricoles
# Elle lit le fichier Excel, crée les objets Field
# et les stocke dans un dictionnaire
# =========================================================
class Fields():

    def __init__(self):

        # Lecture du fichier Excel contenant les champs
        # Les champs sont triés du plus grand au plus petit
        self.df = pd.read_excel("Annexe/Annexe1.xlsx").sort_values(by="HECTARES",ascending=False)

        # Dictionnaire contenant tous les champs
        self.fields = {}

        # Chargement des champs
        self.charger_fields()

    # =====================================================
    # Lecture du fichier Excel et création des objets Field
    # Les objets créés sont stockés dans un dictionnaire
    # dont la clé est l'identifiant du champ
    # =====================================================
    def charger_fields(self):

        for index, row in self.df.iterrows():

            field = Field(
                row['ID'],
                row['HECTARES']
            )

            self.fields[row['ID']] = field

    # =====================================================
    # Retourne un champ à partir de son identifiant
    # =====================================================
    def get_field(self, field_id):

        return self.fields.get(field_id)
