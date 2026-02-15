import numpy as np
from ..range_processing.range_fft import RangeFFT
from ..doppler_processing.doppler_fft import DopplerFFT


class RDMGenerator:
    """
    Range-Doppler Map Generator

    Pipeline:
        IQ → Range FFT → Doppler FFT
    """

    def __init__(
        self,
        sample_rate,
        slope,
        prf,
        fc,
        n_fft_range=None
    ):
        self.range_proc = RangeFFT(sample_rate, slope, n_fft_range)
        self.doppler_proc = DopplerFFT(prf, fc)

    def compute(self, iq_frame):
        """
        Parameters
        ----------
        iq_frame : ndarray
            shape (num_chirps, num_samples)

        Returns
        -------
        rdm_power : 2D power map
        range_axis : meters
        velocity_axis : m/s
        """

        range_fft, _, range_axis = self.range_proc.compute(iq_frame)
        doppler_map, power, velocity_axis = self.doppler_proc.compute(range_fft)

        rdm_power = power
        return rdm_power, range_axis, velocity_axis
