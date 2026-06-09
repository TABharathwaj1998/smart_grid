import numpy as np
import matplotlib.pyplot as plt
import math


# ---------------------------------------------------------
# Frequency Axis
# From 0 to 240 Hz
# ---------------------------------------------------------
f = 60                      # Fundamental frequency (Hz)
fs = 480                    # Sampling frequency (Hz)
omega = 2 * np.pi * f       # Angular frequency
delta_T = 1 / fs            # Sampling interval
freq = np.linspace(0, 240, 1000)
# Convert frequency to digital frequency
Omega = 2 * np.pi * freq / fs
'''
                    # ---------------------------------------------------------
                        Z-TRANSFER FUNCTIONS OF ROCKFELLER & UDREN FILTERS
                    # ---------------------------------------------------------
'''
# ---------------------------------------------------------
# REAL PART Z TRANSFER FUNCTION
# Hr(e^jΩ) = j*sin(Ω)/(ωΔT)
# IMAGINARY PART Z TRANSFER FUNCTION
# Hi(e^jΩ) = -4*sin²(Ω/2)/(ωΔT)^2
# ---------------------------------------------------------

Hr = 1j * np.sin(Omega) / (omega * delta_T)
# Magnitude and Phase for Real Part
Hr_mag = np.abs(Hr)
Hr_phase = np.angle(Hr, deg=True)
# ----------------------------------------------------------
Hi = -4 * (np.sin(Omega / 2) ** 2) / ((omega * delta_T) ** 2)
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
#plt.show()

samples = np.array([
    714, 2218, 2314, 1233, -99, 
    -1195, -1699, -1029, 714, 2219,
    2314, 1233, -99, -1195, -1699])     # Digitized voltage samples from the problem statement

# Sample indices
n = np.arange(1, len(samples) + 1)

# ---------------------------------------------------------
# Rockefeller & Udren Real and Imaginary Coefficients
# ---------------------------------------------------------
real_coeff = []
imag_coeff = []
magnitude = []
phase = []

# Using:
# Real  = (V[n+1] - V[n-1]) / (2*w*delta_T)
# Imag  = (V[n+1] - 2V[n] + V[n-1]) / (w*delta_T)^2
for k in range(1, len(samples)-1):
    real = (samples[k+1] - samples[k-1]) / (2 * omega * delta_T)
    imag = (samples[k+1]
            - 2*samples[k]
            + samples[k-1]) / ((omega * delta_T) ** 2)
    
    magnitude.append(math.sqrt(real**2 + imag**2))
    phase.append(math.atan2(imag, real))
    real_coeff.append(real)
    imag_coeff.append(imag)

# X-axis for calculated points
k_axis = np.arange(2, len(samples))

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