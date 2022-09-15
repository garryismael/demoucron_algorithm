import numpy as np


def invalid_max(val: np.float64):
    if np.isnan(val):
        return True
    elif val > 0:
        return True
    else:
        return False


def invalid_min(val: np.float64):
    return not np.isnan(val)
