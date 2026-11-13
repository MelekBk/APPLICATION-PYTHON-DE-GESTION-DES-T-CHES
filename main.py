# Application de gestion des tâches (console) - Version 1

taches = []  # liste des titres de tâches


def afficher_menu():
    print("\n=== GESTION DES TÂCHES ===")
    print("1. Ajouter une tâche")
    print("2. Afficher les tâches")
    print("3. Rechercher une tâche")
    print("0. Quitter")


def ajouter_tache():
    titre = input("Titre de la tâche : ").strip()
    if titre == "":
        print("Erreur : le titre ne peut pas être vide.")
    else:
        taches.append(titre)
        print("Tâche ajoutée avec succès.")


def afficher_taches():
    if len(taches) == 0:
        print("Aucune tâche pour le moment.")
    else:
        print("\n--- Liste des tâches ---")
        for i in range(len(taches)):
            print(f"{i + 1}. {taches[i]}")





def main():
    choix = ""
    while choix != "0":
        afficher_menu()
        choix = input("Votre choix : ").strip()
        if choix == "1":
            ajouter_tache()
        elif choix == "2":
            afficher_taches()
        elif choix == "3":
            rechercher_tache()
        elif choix == "0":
            print("Au revoir !")
        else:
            print("Erreur : option invalide, choisissez 1, 2, 3 ou 0.")


main()
