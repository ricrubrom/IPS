import numpy as np
from typing import Callable

def even(t:np.ndarray, x:Callable):
    result=(x(t)+x(-t))/2
    return result
