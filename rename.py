import os

def renommer_fichiers(dossier, prefixe, suffixe):
    fichiers = os.listdir(dossier)
    fichiers.sort()

    for index, fichier in enumerate(fichiers, start=1):
        nouveau_nom = f"{prefixe}_{index}_{suffixe}{os.path.splitext(fichier)[1]}"

        chemin_actuel = os.path.join(dossier, fichier)
        nouveau_chemin = os.path.join(dossier, nouveau_nom)

        os.rename(chemin_actuel, nouveau_chemin)

if __name__ == "__main__":
    # Remplacez le chemin par le dossier où se trouvent vos fichiers
    # Change the path to the folder where your files are located
    dossier_cible = ""

    # Remplacez ces valeurs par le préfixe et le suffixe souhaités
    # Replace these values with the desired prefix and suffix
    prefixe = ""
    suffixe = ""

    renommer_fichiers(dossier_cible, prefixe, suffixe)
