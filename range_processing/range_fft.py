import numpy as np
from ..core.fft import fft_1d, power_spectrum


class RangeFFT:
    """
    FMCW Range Processing

    Performs FFT along fast-time (ADC samples).

    Physical meaning:
        beat frequency → range
    """

    def __init__(self, sample_rate, slope, n_fft=None):
        """
        Parameters
        ----------
        sample_rate : Hz
        slope : Hz/s (chirp slope)
        n_fft : optional zero padding size
        """
        self.fs = sample_rate
        self.slope = slope
        self.n_fft = n_fft

    def compute(self, iq_chirps):
        """
        Parameters
        ----------
        iq_chirps : ndarray (num_chirps, num_samples)

        Returns
        -------
        range_fft : complex ndarray
        range_axis : meters
        """

        if self.n_fft is not None:
            pad = self.n_fft - iq_chirps.shape[-1]
            iq_chirps = np.pad(iq_chirps, ((0, 0), (0, pad)))

        spectrum = fft_1d(iq_chirps, axis=-1, window="hann")
        power = power_spectrum(spectrum)

        num_samples = spectrum.shape[-1]
        freq = np.fft.fftfreq(num_samples, d=1/self.fs)

        c = 3e8
        range_axis = (c * freq) / (2 * self.slope)

        return spectrum, power, range_axis
