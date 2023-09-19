## classe de base appelée Vaisseaux qui représente tous les types de vaisseaux de la flotte

import random


class Vaisseaux:
    def __init__(self, nom, type, coordinates):
        self.nom = nom ## attribut non identifie de manière unique le vaisseau
        self.type = type ##  l'attribut type identifie le type de vaisseau
        self.coordinates = coordinates ## l'attribut coordinates représente les coordonnées du vaisseau



## Sous-classes pour représenter les différents types de vaisseaux : soutien et offensif 
# chaque sous-classe hérite des méthodes définies dans la classe mère (Vaisseaux)


class Soutien(Vaisseaux):
     def __init__(self, nom, type, coordinates, unite_medical):
        super().__init__(nom, type, coordinates)
        self.unite_medical = unite_medical

class Offensif(Vaisseaux):
    def __init__(self, nom, type, coordinates, canons, boucliers):
        super().__init__(nom, type, coordinates)
        self.canons = canons
        self.boucliers = boucliers



flotte = []

# Ajouter 50 vaisseaux à la flotte
for i in range(50):

    # Créer un type de vaisseau aléatoire
    vaisseaux_type = random.choice(['soutien', 'offensif'])

    # Créer un nom de vaisseau aléatoire
    vaisseaux_nom = f'Vaisseaux {i}'

    # Créer une coordonnée de vaisseau aléatoire
    vaisseaux_coordinates = (random.randint(0, 100), random.randint(0, 100))

    # Créer un objet vaisseau
    if vaisseaux_type == 'soutien':
        vaisseaux = Soutien(vaisseaux_nom, vaisseaux_type, vaisseaux_coordinates, unite_medical=True)
    else:
        vaisseaux = Offensif(vaisseaux_nom, vaisseaux_type, vaisseaux_coordinates, canons=random.randint(12, 24), boucliers=random.randint(1, 3))

    # Ajouter le vaisseau à la flotte
    flotte.append(vaisseaux)

