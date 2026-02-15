import numpy as np


class PeakDetector:
    """
    Extract peak locations from detection map.
    """

    def __init__(self, min_distance=1):
        self.min_distance = min_distance

    def extract(self, detection_map, power_map):
        """
        Parameters
        ----------
        detection_map : binary ndarray
        power_map : ndarray

        Returns
        -------
        peaks : list of dict
            {range_bin, doppler_bin, power}
        """

        peaks = []
        R, D = detection_map.shape

        for r in range(R):
            for d in range(D):
                if detection_map[r, d] == 0:
                    continue

                # local maximum check
                r0 = max(0, r - self.min_distance)
                r1 = min(R, r + self.min_distance + 1)
                d0 = max(0, d - self.min_distance)
                d1 = min(D, d + self.min_distance + 1)

                local = power_map[r0:r1, d0:d1]

                if power_map[r, d] >= np.max(local):
                    peaks.append({
                        "range_bin": r,
                        "doppler_bin": d,
                        "power": power_map[r, d]
                    })

        return peaks
