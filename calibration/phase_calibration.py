import numpy as np


class PhaseCalibration:
    """
    Per-antenna phase calibration.

    Models phase mismatch between RF channels.
    """

    def __init__(self, phase_offsets_rad):
        """
        phase_offsets_rad : ndarray (num_antennas,)
        """
        self.phase_offsets = np.array(phase_offsets_rad)

    def apply(self, antenna_data):
        """
        Compensate phase mismatch.

        y_cal = y * exp(-j * phase_offset)
        """
        correction = np.exp(-1j * self.phase_offsets)
        return antenna_data * correction
