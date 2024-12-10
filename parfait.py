# Fonction pour vérifier si un nombre est parfait
def est_nombre_parfait(n):
    """
    Vérifie si un nombre est un nombre parfait.

    Un nombre parfait est un entier positif égal à la somme de ses diviseurs propres
    (tous ses diviseurs à l'exception de lui-même).

    Paramètres:
    n (int): Le nombre à vérifier.

    Retourne:
    bool: True si le nombre est parfait, False sinon.
    """
    if n <= 1:
        return False
    # Calculer la somme des diviseurs propres de n
    somme_diviseurs = sum(i for i in range(1, n) if n % i == 0)
    return somme_diviseurs == n


# Fonction pour générer une liste de nombres parfaits jusqu'à une limite donnée
def liste_nombres_parfaits(limite):
    """
    Génère une liste de nombres parfaits jusqu'à une limite donnée.

    Paramètres:
    limite (int): La limite supérieure pour rechercher les nombres parfaits.

    Retourne:
    list: Une liste contenant tous les nombres parfaits jusqu'à la limite spécifiée.
    """
    nombres_parfaits = []
    for num in range(2, limite + 1):
        if est_nombre_parfait(num):
            nombres_parfaits.append(num)
    return nombres_parfaits


# Exemple d'utilisation
if __name__ == "__main__":
    limite = 10000  # Limite jusqu'à laquelle chercher les nombres parfaits
    print(f"Les nombres parfaits jusqu'à {limite} sont : {liste_nombres_parfaits(limite)}")
