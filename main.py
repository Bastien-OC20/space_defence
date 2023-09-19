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


"""  PART 2 
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

"""
# PART 3
# Classe pour représenter la flotte
class Flotte:
    def __init__(self, size):
        self.navires = []
        for i in range(size):
            type = random.choice(['soutien', 'offensif'])
            coordinates = (random.randint(0, 100), random.randint(0, 100))
            self.navires.append(Vaisseaux(type, coordinates))

    def paire_navires(self):

         # Crée une liste de paires de navires
        paires =[]

        # Parcourt tous les navires de la flotte
        for i in range (len(self.navires)):
             
             # Parcourt tous les navires de la flotte à partir de l'indice i + 1 ( indices paire : 2)
             for j in range(i + 1, len(self.navires)):

                # Si deux navires sont dans des positions adjacentes et ont le même type on ajoute ces deux navires en tant que couple
                if self.navires[i].type != self.navires[j].type:
                    paires.append((self.navires[i], self.navires[j]))

    # Retourne la liste des paires de navires
        return paires

    def move_paires(self, paires):
        # Déplace les paires de navires vers des positions adjacentes
        for paire in paires:

            # Déplace le navire offensif
            paire[0].coordinates = (paire[0].coordinates[0] +  paire[0].coordinates[1])

            # Déplace le navire de soutien
            paire[1].coordinates = (paire[1].coordinates[0] -  paire[1].coordinates[1])


# Crée une flotte
flotte = Flotte(50)

# Génère les paires de navires
paires = flotte.paire_navires()

# Déplace les paires de navires
flotte.move_paires(paires)