import numpy as np


def apply_window(x, window_type="hann"):
    """
    Apply window function along last axis.

    Parameters
    ----------
    x : ndarray
        Input signal
    window_type : str
        'hann', 'hamming', 'blackman', None
    """
    N = x.shape[-1]

    if window_type is None:
        return x

    if window_type == "hann":
        w = np.hanning(N)
    elif window_type == "hamming":
        w = np.hamming(N)
    elif window_type == "blackman":
        w = np.blackman(N)
    else:
        raise ValueError("Unsupported window type")

    return x * w


def fft_1d(x, axis=-1, window="hann", shift=False):
    """
    1D FFT wrapper for radar processing.

    Features
    --------
    - optional windowing
    - axis control
    - optional FFT shift

    Returns
    -------
    X : complex ndarray
    """
    x = apply_window(x, window)
    X = np.fft.fft(x, axis=axis)

    if shift:
        X = np.fft.fftshift(X, axes=axis)

    return X


def power_spectrum(x):
    """
    Compute magnitude squared (power).

    |X|^2
    """
    return np.abs(x) ** 2
