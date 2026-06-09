import numpy as np
import matplotlib.pyplot as plt
import math

# ---------------------------------------------------------
# Frequency Axis
# From 0 to 480 Hz
# ---------------------------------------------------------
f = 120                     # Fundamental frequency (Hz)
fs = 960                    # Sampling frequency (Hz)
freq = np.linspace(0, (fs/2), 1000)
omega = 2 * np.pi * freq       # Angular frequency
# Convert frequency to digital frequency
Omega = omega / fs

'''
                    # ---------------------------------------------------------
                  Z-TRANSFER FUNCTIONS OF DISCRETE FOURIER TRANSFORM (DFT) FILTERS
                    # ---------------------------------------------------------
'''
# ---------------------------------------------------------
# REAL PART Z TRANSFER FUNCTION
# HR(Ω) = 0.5[cos(4Ω)−jsin(4Ω)]+0.866[cos3Ω)−jsin(3Ω)]+1.0[cos(2Ω)−jsin(2Ω)]+0.866[cos(Ω)−jsin(Ω)]+0.5
# IMAGINARY PART Z TRANSFER FUNCTION
# Hi(Ω) = [cos(5Ω)−jsin(5Ω)]+0.866[cos(4Ω)−jsin(4Ω)]+0.5[cos(3Ω)−jsin(3Ω)]−0.5[cos(Ω)−jsin(Ω)]−0.866
# ---------------------------------------------------------

Hr = 0.5 * (np.cos(4 * Omega) - 1j * np.sin(4 * Omega)) + 0.866 * (np.cos(3 * Omega) - 1j * np.sin(3 * Omega)) + 1.0 * (np.cos(2 * Omega) - 1j * np.sin(2 * Omega)) + 0.866 * (np.cos(Omega) - 1j * np.sin(Omega)) + 0.5
# Magnitude and Phase for Real Part
Hr_mag = np.abs(Hr)
Hr_phase = np.angle(Hr, deg=True)
# ----------------------------------------------------------
Hi = 1.0 * (np.cos(5 * Omega) - 1j * np.sin(5 * Omega)) + 0.866 * (np.cos(4 * Omega) - 1j * np.sin(4 * Omega)) + 0.5 * (np.cos(3 * Omega) - 1j * np.sin(3 * Omega)) - 0.5 * (np.cos(Omega) - 1j * np.sin(Omega)) - 0.866
# Magnitude and Phase for Imaginary Part
Hi_mag = np.abs(Hi)
Hi_phase = np.angle(Hi, deg=True)
'''
                    # ---------------------------------------------------------
                                  PLOTTING FREQUENCY RESPONSES
                    # ---------------------------------------------------------
'''

plt.figure(figsize=(12, 8))

plt.subplot(2,2,1)
plt.plot(freq, Hr_mag)
plt.title('Real Filter Magnitude Response')             # Real Magnitude Response
plt.xlabel('Frequency (Hz)')
plt.ylabel('|Hr(f)|')
plt.grid(True)

plt.subplot(2,2,2)
plt.plot(freq, Hr_phase)
plt.title('Real Filter Phase Response')                 # Real Phase Response
plt.xlabel('Frequency (Hz)')
plt.ylabel('Phase (degrees)')
plt.grid(True)

plt.subplot(2,2,3)
plt.plot(freq, Hi_mag)
plt.title('Imaginary Filter Magnitude Response')        # Imaginary Magnitude Response
plt.xlabel('Frequency (Hz)')
plt.ylabel('|Hi(f)|')
plt.grid(True)

plt.subplot(2,2,4)
plt.plot(freq, Hi_phase)
plt.title('Imaginary Filter Phase Response')            # Imaginary Phase Response
plt.xlabel('Frequency (Hz)')
plt.ylabel('Phase (degrees)')
plt.grid(True)

plt.tight_layout()


samples = np.array([348,1870,2526,1956,
    508,-971,-1628,-1102,
    267,1641,2184,1554,
    106,-1311,-1854])     # Digitized voltage samples from the problem statement

# Sample indices
n = np.arange(1, len(samples) + 1)

# ---------------------------------------------------------
# REAL AND IMAGINARY COEFFICIENTS CALCULATION USING DFT FORMULAS
# ---------------------------------------------------------
real_coeff = []
imag_coeff = []
magnitude = []
phase = []

sin_reference = [0,0.5,0.866,1.0]
cos_reference = [1.0,0.866,0.5,0.0]

# Using:
# Real  = sum(x[n] * sin(2πkn/N)) for n=0 to N-1
# Imag  = sum(x[n] * cos(2πkn/N)) for n=0 to N-1
for k in range(3,len(samples)-1):
    real = (samples[k-3] * sin_reference[0]) + (samples[k-2] * sin_reference[1]) + (samples[k-1] * sin_reference[2]) + (samples[k] * sin_reference[3])
    imag = (samples[k-3] * cos_reference[0]) + (samples[k-2] * cos_reference[1]) + (samples[k-1] * cos_reference[2]) + (samples[k] * cos_reference[3])

    magnitude.append(math.sqrt(real**2 + imag**2))
    phase.append(math.atan2(imag, real))
    real_coeff.append(real)
    imag_coeff.append(imag)

# X-axis for calculated points
k_axis = np.arange(3, len(samples)-1)

# ---------------------------------------------------------
# Convert coefficients and magnitude/phase to NumPy Arrays
# ---------------------------------------------------------
real_coeff = np.array(real_coeff)
imag_coeff = np.array(imag_coeff)
magnitude = np.array(magnitude)
phase_angle = np.array(phase)

# ---------------------------------------------------------
# PLOTTING PEAK MAGNITUDE AND PHASE
# ---------------------------------------------------------
plt.figure(figsize=(12,8))

plt.subplot(3,1,1)
plt.plot(n, samples, marker='o')
plt.title('Digitized Voltage Samples')      # Sample vs Voltage
plt.xlabel('Sample Number')
plt.ylabel('Voltage')
plt.grid(True)

plt.subplot(3,1,2)
plt.plot(k_axis, magnitude, marker='o')
plt.title('Estimated Peak Magnitude')       # Sample vs Magnitude
plt.xlabel('Sample Number')
plt.ylabel('Magnitude')
plt.grid(True)

plt.subplot(3,1,3)
plt.plot(k_axis, phase_angle, marker='o')
plt.title('Estimated Peak Phase')            # Sample vs Phase
plt.xlabel('Sample Number')
plt.ylabel('Phase (degrees)')
plt.grid(True)

plt.tight_layout()
plt.show()
