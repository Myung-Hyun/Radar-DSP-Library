# 📡 Radar DSP Library

## 1. Overview

This repository provides reusable digital signal processing (DSP) modules for FMCW radar systems.

The library focuses on transforming complex baseband radar signals into physically meaningful measurements such as:

- range
- velocity
- angle (extension-ready)
- detection candidates

The design goal is to provide **sensor-agnostic, reusable DSP components** that can be integrated into:

- radar simulators
- perception pipelines
- real radar data processing stacks

---

## 2. Design Philosophy

- Pure algorithmic implementation
- No dependency on specific radar hardware
- Modular processing blocks
- Reproducible numerical behavior
- Extensible to MIMO and real sensor calibration

This library operates strictly in the **complex baseband domain**.

---

## 3. Processing Pipeline

Typical FMCW DSP flow supported by this library:

```
Complex Baseband IQ
        ↓
Windowing
        ↓
Range FFT
        ↓
Doppler FFT
        ↓
Range-Doppler Map
        ↓
Detection (CFAR)
```

---

## 4. Modules

### 4.1 Window Functions

Applies windowing to reduce spectral leakage.

Supported windows:

- Hanning
- Hamming
- Blackman
- Rectangular

---

### 4.2 Range FFT

Transforms fast-time signal into range domain.

Input:
- complex IQ samples (per chirp)

Output:
- range profile

Physical meaning:
- beat frequency → target range

---

### 4.3 Doppler FFT

Transforms slow-time phase change into velocity domain.

Input:
- stacked range profiles across chirps

Output:
- Range-Doppler Map (RDM)

Physical meaning:
- phase progression → radial velocity

---

### 4.4 CFAR Detection

Detects peaks from Range-Doppler Map.

Supported strategies:

- Cell-Averaging CFAR (CA-CFAR)
- Ordered Statistics CFAR (extension-ready)

Output:
- detection indices
- detection power
- estimated SNR

---

### 4.5 Utility Functions

Common radar DSP utilities:

- power conversion
- noise estimation
- magnitude normalization
- peak extraction

---

## 5. Example Usage

```python
import numpy as np
from radar_dsp.range import range_fft
from radar_dsp.doppler import doppler_fft
from radar_dsp.cfar import ca_cfar_2d

# iq_data: complex baseband samples
range_profile = range_fft(iq_data)

rdm = doppler_fft(range_profile)

detections = ca_cfar_2d(rdm, guard_cells=2, ref_cells=8)
```

---

## 6. Data Conventions

### IQ Data Shape

```
[num_chirps, num_samples]
```

- axis 0 → slow-time
- axis 1 → fast-time

All processing assumes row-major layout.

---

### Range-Doppler Map Shape

```
[num_range_bins, num_doppler_bins]
```

Magnitude or power domain depending on configuration.

---

## 7. Numerical Assumptions

- Linear FMCW chirp
- Ideal mixing
- Uniform sampling
- Additive white Gaussian noise environment

Noise model:

$$
n \sim \mathcal{CN}(0, \sigma^2)
$$

---

## 8. Project Structure

```
radar-dsp-library/
│
├── radar_dsp/
│   ├── window.py
│   ├── range.py
│   ├── doppler.py
│   ├── cfar.py
│   └── utils.py
│
├── tests/
│   └── test_pipeline.py
│
└── README.md
```

---

## 9. Integration

This library is intended to be used as:

- a submodule of FMCW radar simulators
- a processing backend for perception pipelines
- a standalone DSP toolkit for radar research

---

## 10. Future Extensions

Planned features:

- MIMO virtual array processing
- Angle estimation (DOA)
- TDM-MIMO compensation
- Clutter suppression filters
- Calibration utilities
- GPU acceleration support

---

## 11. Requirements

- Python 3.9+
- NumPy
- SciPy

---

## 12. License

MIT License
