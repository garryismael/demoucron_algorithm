import numpy as np
from numpy import copy

from api.constants import MINIMISER


class Demoucron:
    def __init__(self, matrice: np.ndarray, choix: str):
        self._origin = np.copy(matrice)
        self._matrice: np.ndarray[np.float64] = matrice
        self.valid_elem = Demoucron.notNan if choix == MINIMISER else Demoucron.greater
        self.valeur = Demoucron.min_val if choix == MINIMISER else Demoucron.max_val
        self.choix = choix
        self.calculer()

    def entrer(self, k):
        """
        Récupération des indices de la colonne k
        """
        return [i for i, elem in enumerate(self._matrice[:, k]) if self.valid_elem(elem)]

    def sortir(self, k):
        """
        Récupération des indices la ligne k
        """
        return [i for i, elem in enumerate(self._matrice[k]) if self.valid_elem(elem)]

    def calculer(self):
        for k in range(1, self.sommets-1):
            entrees = self.entrer(k)
            sorties = self.sortir(k)
            items: list[dict[str, int]] = []
            for entree in entrees:
                self.set_items(k, entree, sorties, items)
            self.set_matrice(items)

    def set_matrice(self, items: list[dict[str, int]]):
        for item in items:
            entree = item.get('entree')
            sortie = item.get('sortie')
            distance = item.get('distance')
            self._matrice[entree, sortie] = distance
        
    def set_items(self, k: int, entree: np.float64, sorties: list[np.float64], items: list[dict[str, int]]):
        entree_to_k = self._matrice[entree, k]
        for sortie in sorties:
            k_to_sortie = self._matrice[k, sortie]
            vecteur = self._matrice[entree, sortie]
            distance = self.distance(vecteur, entree_to_k, k_to_sortie)
            items.append({
                'entree': entree,
                'sortie': sortie,
                'distance': distance
            })

    def distance(self, vecteur: np.float64, entree_to_k: np.float64, k_to_sortie: np.float64):
        somme = entree_to_k + k_to_sortie
        return somme if np.isnan(vecteur) else self.valeur(somme, vecteur)

    @property
    def minimiser(self):
        line = self.sommets-1
        paths: list[int] = []
        paths.append(line)
        while line > 0:
            line = np.nanargmin(self._matrice[:, line])
            paths.append(int(line))
        paths.reverse()
        return paths

    @property
    def maximiser(self):
        colonne = self.sommets-1
        marquages = np.amax(self._matrice, axis=0)
        res = []
        while colonne > 0:
            val_max = marquages[colonne]
            distances = self._origin[:, colonne]
            for i, v in enumerate(distances):
                if v > 0 and distances[i] + marquages[i] == val_max:
                    res.append(colonne)
                    colonne = i
                    break
        res.append(0)
        res.reverse()
        return res

    def find_path(self) -> list[int]:
        return getattr(self, self.choix)

    @staticmethod
    def notNan(elem: np.float64):
        return not np.isnan(elem)

    @staticmethod
    def greater(elem: np.float64):
        if elem > 0:
            return True
        return False

    @staticmethod
    def max_val(val: np.float64, vecteur: np.float64):
        if val > vecteur:
            return val
        return vecteur

    @staticmethod
    def min_val(val: np.float64, vecteur: np.float64):
        if val < vecteur:
            return val
        return vecteur

    @property
    def sommets(self):
        return len(self._matrice)
