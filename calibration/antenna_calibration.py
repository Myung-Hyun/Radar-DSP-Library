import numpy as np


class AntennaGainCalibration:
    """
    Gain calibration for antenna array.
    """

    def __init__(self, gain_factors):
        """
        gain_factors : ndarray (num_antennas,)
        """
        self.gain = np.array(gain_factors)

    def apply(self, antenna_data):
        """
        Normalize antenna responses.
        """
        return antenna_data / self.gain
