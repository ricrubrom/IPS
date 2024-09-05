import numpy as np

def heaviside(x: np.ndarray, center=0, lim=0.5) -> np.ndarray:
    result = x - center
    return np.where(result > 0, 1.0, np.where(result < 0, 0.0, lim))
