from typing import Callable

import numpy as np
from fastapi import Depends, HTTPException, Path, status
from pydantic import BaseModel

from api.constants import INVALID_GRAPH, MAXIMISER, MINIMISER
from api.demoucron import Demoucron
from api.utils import invalid_max, invalid_min


class Graph(BaseModel):
    matrix: list[list[float | None]]


def raiseException():
    raise HTTPException(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        detail=INVALID_GRAPH
    )


def valid_array(arr: np.ndarray, choice: str, i: int, invalid: Callable[[float], bool]):
    j = 0
    while j < len(arr):
        if j == i:
            if invalid(arr[i]):
                return False
        elif choice == MAXIMISER and np.isnan(arr[j]):
            return False
        j += 1
    if i < len(arr)-1:
        return True
    elif choice == MAXIMISER:
        return np.all(arr == 0)
    else:
        return np.all(np.isnan(arr))

def not_reversed(graph: Graph, choice: str = Path(..., regex=f"^({MINIMISER}|{MAXIMISER})$")):
    try:
        matrix = np.array(graph.matrix, dtype=np.float64)
    except ValueError:
        raiseException()
    
    if matrix.shape[0] != matrix.shape[1]:
        raiseException()
    
    map: dict[str, list[int]] = dict()
    i = 0
    for arr in matrix:
        j = 0
        map[i] = []
        while j < len(arr):
            if j != i:
                if choice == MINIMISER and not np.isnan(arr[j]):
                    map[i].append(j)
                elif not np.isnan(arr[j]) and arr[j] > 0:
                    map[i].append(j)
            j+=1
        i += 1
    
    for key, values in map.items():
        for val in values:
            items = map.get(val, [])
            if key in items:
                raiseException()
    return matrix, choice

def valid_matrix(data: tuple[np.ndarray, str] = Depends(not_reversed)):
    matrix, choice = data
    invalid = invalid_max if choice == MAXIMISER else invalid_min
    i = 0
    for arr in matrix:
        if not valid_array(arr, choice, i, invalid):
            raiseException()
        i += 1
    return Demoucron(matrix, choice)
