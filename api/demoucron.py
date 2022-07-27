import numpy as np


class Demoucron:
    def __init__(self, matrice: np.ndarray, choix: str):
        self._origin = np.copy(matrice)
        self._matrice: np.ndarray = matrice
        self.comparer_elem = Demoucron.notNan if choix == 'minimiser' else Demoucron.greater
        self.comparer_vecteur = min if choix == 'minimiser' else max
        self.choix = choix
        self.calculer()

    def entrer(self, k, entrees: list):
        i = 0
        for tab in self._matrice:
            if self.comparer_elem(tab[k]):
                entrees.append(i)
            i += 1

    def sortir(self, k, sorties: list[int]):
        i = 0
        for item in self._matrice[k]:
            if self.comparer_elem(item):
                sorties.append(i)
            i += 1

    def calculer(self):
        k = 1
        sommets = self.sommets
        while k < sommets:
            entrees = []
            sorties = []
            self.entrer(k, entrees)
            self.sortir(k, sorties)
            for entree in entrees:
                self.set_matrice(k, entree, sorties)
            k += 1

    def set_matrice(self, k: int, entree: float, sorties: list[float]):
        a = self._matrice[entree, k]
        if not np.isnan(a):
            for sortie in sorties:
                b = self._matrice[k, sortie]
                vecteur = self._matrice[entree, sortie]
                self._matrice[entree, sortie] = self.valeur(vecteur, a, b)

    def valeur(self, vecteur: float, a: float, b: float):
        if np.isnan(vecteur):
            return a + b
        return self.comparer_vecteur([a+b, vecteur])

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
        res = []
        while colonne > 0:
            marquages = np.amax(self._matrice, axis=0)
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
    def notNan(a: np.float64):
        return not np.isnan(a)

    @staticmethod
    def greater(a: np.float64):
        return a > 0

    @property
    def sommets(self):
        return self._matrice.shape[0]