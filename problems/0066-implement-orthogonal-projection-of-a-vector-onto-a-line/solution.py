
import numpy as np

def orthogonal_projection(v, L):
    """
    Compute the orthogonal projection of vector v onto line L.
    """
    v = np.array(v)
    L = np.array(L)

    projection = (np.dot(v, L) / np.dot(L, L)) * L

    return np.round(projection, 3).tolist()
