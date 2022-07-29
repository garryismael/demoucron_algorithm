MATRICE_MIN = [
    [None, 2, 3, 5, None, None, None, None, None],
    [None, None, None, 3, 5, None, None, None, None],
    [None, None, None, 4, None, None, 4, None, None],
    [None, None, None, None, None, 4, 7, 2, None],
    [None, None, None, None, None, 1, None, None, None],
    [None, None, None, None, None, None, None, None, 5],
    [None, None, None, None, None, None, None, 3, None],
    [None, None, None, None, None, None, None, None, 3],
    [None, None, None, None, None, None, None, None, None]
]

MATRICE_MIN_INVALID = [
    [2, 2, 3, 5, None, None, None, None, None],
    [None, 2, None, 3, 5, None, None, None, None],
    [None, None, 2, 4, None, None, 4, None, None],
    [None, None, None, 2, None, 4, 7, 2, None],
    [None, None, None, None, 2, 1, None, None, None],
    [None, None, None, None, None, 5, None, None, 5],
    [None, None, None, None, None, None, 3, 3, None],
    [None, None, None, None, None, None, None, 32, 3],
    [None, None, None, None, None, None, None, None, 2]
]


MAX_BIG_MATRIX = [
    [0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 15, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 16, 0, 0, 0, 0, 0],
    [0, 0, 8, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 5, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 8, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 3, 0, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 12, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 6],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

MATRICE_MAX = [
    [0, 3, 0, 5, 0, 0, 0],
    [0, 0, 4, 2, 6, 0, 0],
    [0, 0, 0, 0, 4, 0, 5],
    [0, 0, 3, 0, 0, 7, 0],
    [0, 0, 0, 0, 0, 0, 3],
    [0, 0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 0, 0],
]

MATRICE_MAX_INVALID = [
    [3, 3, 0, 5, 0, 0, 0],
    [0, 3, 4, 2, 6, 0, 0],
    [0, 0, 3, 0, 4, 0, 5],
    [0, 0, 3, 5, 0, 7, 0],
    [0, 0, 0, 0, 5, 0, 3],
    [0, 0, 0, 0, 0, 6, 2],
    [0, 0, 0, 0, 0, 0, 6],
]


MATRICE_LENGTH_NOT_EQUAL = [
    [0, 3, 0, 5, 0, 0, 0],
    [0, 0, 4, 2, 6, 0, 0],
    [0, 0, 0, 0, 4, 0, 5],
    [0, 0, 3, 0, 0, 7, 0],
    [0, 0, 0, 0, 0, 0, 3],
    [0, 0, 0, 0, 0, 0, 2]
]


PATH_MIN = "/min"
PATH_MAX = "/max"
MATRICE = "matrice"
RESULTAT = "resultat"
DETAIL = "detail"
