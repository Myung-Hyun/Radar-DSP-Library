import numpy as np


class CACFAR2D:
    """
    2D Cell-Averaging CFAR

    Applies adaptive thresholding on Range-Doppler Map.

    Parameters
    ----------
    guard_cells : (g_r, g_d)
        guard region size
    training_cells : (t_r, t_d)
        training region size
    pfa : float
        probability of false alarm
    """

    def __init__(self, guard_cells=(2, 2), training_cells=(8, 4), pfa=1e-5):
        self.g_r, self.g_d = guard_cells
        self.t_r, self.t_d = training_cells
        self.pfa = pfa

    def _threshold_scale(self, num_training):
        """
        CFAR threshold scaling factor.

        Derived from exponential noise assumption.
        """
        return num_training * (self.pfa ** (-1 / num_training) - 1)

    def detect(self, rdm_power):
        """
        Apply CFAR detection.

        Returns
        -------
        detection_map : binary ndarray
        threshold_map : ndarray
        """

        R, D = rdm_power.shape
        detection = np.zeros_like(rdm_power, dtype=np.uint8)
        threshold_map = np.zeros_like(rdm_power)

        tr, td = self.t_r, self.t_d
        gr, gd = self.g_r, self.g_d

        for r in range(tr + gr, R - tr - gr):
            for d in range(td + gd, D - td - gd):

                # training window bounds
                r_start = r - tr - gr
                r_end   = r + tr + gr + 1
                d_start = d - td - gd
                d_end   = d + td + gd + 1

                window = rdm_power[r_start:r_end, d_start:d_end]

                # remove guard + CUT region
                guard = rdm_power[
                    r-gr:r+gr+1,
                    d-gd:d+gd+1
                ]

                noise_cells = np.sum(window) - np.sum(guard)
                num_training = window.size - guard.size

                noise_mean = noise_cells / num_training
                alpha = self._threshold_scale(num_training)

                threshold = alpha * noise_mean
                threshold_map[r, d] = threshold

                if rdm_power[r, d] > threshold:
                    detection[r, d] = 1

        return detection, threshold_map
