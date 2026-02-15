import numpy as np


class SteeringVectorULA:
    """
    Steering vector for Uniform Linear Array (ULA).

    Assumptions
    -----------
    - far-field plane wave
    - narrowband signal
    - antenna aligned on x-axis
    """

    def __init__(self, num_antennas, d, wavelength):
        """
        Parameters
        ----------
        num_antennas : int
        d : element spacing (meters)
        wavelength : carrier wavelength (meters)
        """
        self.N = num_antennas
        self.d = d
        self.lam = wavelength

    def compute(self, angle_rad):
        """
        Compute steering vector for given angle.

        a(n) = exp(j * 2π * n * d * sin(theta) / λ)

        Returns
        -------
        ndarray shape (N,)
        """

        n = np.arange(self.N)
        phase = 2 * np.pi * n * self.d * np.sin(angle_rad) / self.lam
        return np.exp(1j * phase)

    def grid(self, angle_grid_rad):
        """
        Generate steering matrix for angle grid.

        Returns
        -------
        A : ndarray shape (num_angles, N)
        """
        return np.array([self.compute(a) for a in angle_grid_rad])
