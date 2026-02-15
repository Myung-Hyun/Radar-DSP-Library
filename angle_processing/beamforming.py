import numpy as np


class Beamformer:
    """
    Conventional (Bartlett) Beamforming

    입력:
        data: shape (num_rx, num_snapshots) or (num_rx,)
        angle_grid: radian array (e.g., np.linspace(-np.pi/2, np.pi/2, 181))
        steering_vector_fn: callable(angle) -> (num_rx,) complex

    출력:
        beam power spectrum: shape (num_angles,)
    """

    def __init__(self, steering_vector_fn, angle_grid):
        self.steering_vector_fn = steering_vector_fn
        self.angle_grid = angle_grid

    def process(self, data):
        """
        Beamforming power spectrum 계산
        """

        if data.ndim == 1:
            data = data[:, np.newaxis]

        R = self._covariance_matrix(data)

        power_spectrum = np.zeros(len(self.angle_grid), dtype=float)

        for i, angle in enumerate(self.angle_grid):
            a = self.steering_vector_fn(angle)
            a = a[:, np.newaxis]

            numerator = np.conj(a.T) @ R @ a
            denominator = np.conj(a.T) @ a

            power_spectrum[i] = np.real(numerator / denominator).squeeze()

        return power_spectrum

    @staticmethod
    def _covariance_matrix(data):
        """
        Spatial covariance matrix
        data shape: (num_rx, num_snapshots)
        """
        return (data @ np.conj(data.T)) / data.shape[1]
