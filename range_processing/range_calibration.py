import numpy as np


class RangeCalibration:
    """
    Range Calibration Module

    Handles:
        - range bias compensation
        - resolution calculation
    """

    def __init__(self, slope, sample_rate):
        self.slope = slope
        self.fs = sample_rate
        self.c = 3e8

    def range_axis(self, num_samples):
        """
        Compute physical range axis.

        f = k / N * fs
        R = c * f / (2 * slope)
        """
        freq = np.fft.fftfreq(num_samples, d=1/self.fs)
        return (self.c * freq) / (2 * self.slope)

    def apply_bias(self, range_axis, bias_m):
        """
        Apply constant range bias correction.
        """
        return range_axis - bias_m

    def range_resolution(self, bandwidth):
        """
        FMCW range resolution.

        ΔR = c / (2B)
        """
        return self.c / (2 * bandwidth)
