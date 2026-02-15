import numpy as np


class DOAEstimatorFFT:
    """
    Angle estimation using spatial FFT.

    Input
    -----
    antenna_data shape (num_antennas,)
    """

    def __init__(self, num_antennas, d, wavelength):
        self.N = num_antennas
        self.d = d
        self.lam = wavelength

    def estimate(self, antenna_snapshot):
        """
        Compute angle spectrum.

        Returns
        -------
        angle_axis_rad
        spectrum_power
        """

        spectrum = np.fft.fftshift(np.fft.fft(antenna_snapshot, n=self.N))
        power = np.abs(spectrum) ** 2

        # spatial frequency axis
        k = np.arange(-self.N//2, self.N//2)
        spatial_freq = k / self.N

        sin_theta = spatial_freq * self.lam / self.d
        sin_theta = np.clip(sin_theta, -1, 1)

        angle_axis = np.arcsin(sin_theta)
        return angle_axis, power

    def peak_angle(self, angle_axis, power):
        """
        Return dominant angle.
        """
        idx = np.argmax(power)
        return angle_axis[idx]
