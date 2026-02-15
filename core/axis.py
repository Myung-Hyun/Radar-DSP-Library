class Axis:
    """
    Radar data axis definition

    표준 데이터 구조:
        (num_rx, num_chirp, num_sample)

    이후 단계:
        range FFT → (num_rx, num_chirp, num_range_bin)
        doppler FFT → (num_rx, num_doppler_bin, num_range_bin)
        angle → (num_angle, num_doppler_bin, num_range_bin)
    """

    RX = 0
    CHIRP = 1
    SAMPLE = 2

    RANGE = 2
    DOPPLER = 1
    ANGLE = 0
