import numpy as np


def magnitude(x):
    """
    Complex magnitude
    """
    return np.abs(x)


def power(x):
    """
    Power = |x|^2
    """
    return np.abs(x) ** 2


def db(x, eps=1e-12):
    """
    Linear → dB
    """
    return 10 * np.log10(np.maximum(x, eps))


def phase(x):
    """
    Complex phase
    """
    return np.angle(x)


def normalize(x, axis=None):
    """
    Max normalization
    """
    max_val = np.max(np.abs(x), axis=axis, keepdims=True)
    return x / (max_val + 1e-12)
