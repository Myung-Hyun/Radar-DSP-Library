import numpy as np


class TDMMIMOCompensation:
    """
    Compensation for TDM-MIMO phase error.

    Phase error arises due to:
        target motion during TX switching
    """

    def __init__(self, doppler_frequency, tx_time_offset):
        """
        Parameters
        ----------
        doppler_frequency : Hz
        tx_time_offset : seconds between TX switching
        """
        self.fd = doppler_frequency
        self.dt = tx_time_offset

    def apply(self, virtual_array_data):
        """
        Compensate phase rotation.

        phase = 2π * fd * dt
        """
        phase = 2 * np.pi * self.fd * self.dt
        correction = np.exp(-1j * phase)

        return virtual_array_data * correction
