def afficher(planning):

    planning_regroupe = []

    for jour in sorted(set(ligne[0] for ligne in planning)):
        for moment in ["morning", "afternoon"]:
            for worker in ["father", "son", "together"]:

                champs = []

                for ligne in planning:
                    if (
                        ligne[0] == jour
                        and ligne[1] == moment
                        and ligne[3] == worker
                    ):
                        champs.append(str(ligne[2]))

                if champs:
                    planning_regroupe.append(
                        [jour, moment, ", ".join(champs), worker]
                    )

    print("\n" + "=" * 70)
    print("PLANNING DE RÉCOLTE FINAL")
    print("=" * 70)

    print(
        f"{'Jour':<8}"
        f"{'Moment':<15}"
        f"{'Champs':<20}"
        f"{'Worker':<15}"
    )

    for ligne in planning_regroupe:
        print(
            f"{ligne[0]:<8}"
            f"{ligne[1]:<15}"
            f"{ligne[2]:<20}"
            f"{ligne[3]:<15}"
        )

    print("=" * 70)