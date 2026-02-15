import numpy as np


def hann(length):
    return np.hanning(length)


def hamming(length):
    return np.hamming(length)


def blackman(length):
    return np.blackman(length)


def apply_window(data, window, axis):
    """
    지정 axis에 window 적용
    """
    shape = [1] * data.ndim
    shape[axis] = len(window)

    w = window.reshape(shape)
    return data * w
