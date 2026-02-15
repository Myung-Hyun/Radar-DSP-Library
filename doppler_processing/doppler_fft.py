import numpy as np
from ..core.fft import fft_1d, power_spectrum


class DopplerFFT:
    """
    Doppler Processing

    Performs FFT across chirps (slow-time).

    Physical meaning:
        phase change across chirps → velocity
    """

    def __init__(self, prf, fc):
        """
        Parameters
        ----------
        prf : pulse repetition frequency (chirp rate)
        fc : carrier frequency
        """
        self.prf = prf
        self.fc = fc

    def compute(self, range_fft):
        """
        Parameters
        ----------
        range_fft : ndarray (num_chirps, num_range_bins)

        Returns
        -------
        doppler_map : complex ndarray
        velocity_axis : m/s
        """

        doppler = fft_1d(range_fft, axis=0, window="hann", shift=True)
        power = power_spectrum(doppler)

        num_chirps = range_fft.shape[0]
        freq = np.fft.fftfreq(num_chirps, d=1/self.prf)
        freq = np.fft.fftshift(freq)

        c = 3e8
        velocity_axis = (c * freq) / (2 * self.fc)

        return doppler, power, velocity_axis
