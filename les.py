import numpy as np
import matplotlib.pyplot as plt
import math

# ---------------------------------------------------------
# Frequency Axis
# From 0 to 720 Hz
# ---------------------------------------------------------
f = 60                      # Fundamental frequency (Hz)
fs = 720                    # Sampling frequency (Hz)
freq = np.linspace(0, fs, 1000)
omega = 2 * np.pi * freq       # Angular frequency
# Convert frequency to digital frequency
Omega = omega / fs

'''
                    # ---------------------------------------------------------
                  Z-TRANSFER FUNCTIONS OF LEAST ERROR SQUARE ALGORITHM (LES) FILTERS
                    # ---------------------------------------------------------
'''

# ---------------------------------------------------------
# REAL PART Z TRANSFER FUNCTION
# Ipsin⁡θ = (0.674972152*[cos(4Ω)−jsin(4Ω)])+(-0.364346074*[cos(3Ω)−jsin(3Ω)])+(-0.621244916*[cos(2Ω)−jsin(2Ω)])+(-0.364360555*[cos(Ω)−jsin(Ω)])+(0.364360555*[cos(Ω)+jsin(Ω)])+(0.621244916*[cos(2Ω)+jsin(2Ω)])+(0.364346074*[cos(3Ω)+jsin(3Ω)])+(-0.674972150*[cos(4Ω)+jsin(4Ω)])
# Ipsin⁡3θ = (-0.100263157*[cos(4Ω)−jsin(4Ω)])+(0.229849810*[cos(3Ω)−jsin(3Ω)])+(-0.009174009*[cos(2Ω)−jsin(2Ω)])+(-0.270148784*[cos(Ω)−jsin(Ω)])+(0.270148784*[cos(Ω)+jsin(Ω)])+(0.009174009*[cos(2Ω)+jsin(2Ω)])+(-0.229849810*[cos(3Ω)+jsin(3Ω)])+(0.100263157*[cos(4Ω)+jsin(4Ω)])
# IMAGINARY PART Z TRANSFER FUNCTION
# Ipcos⁡θ = (-0.243878245*[cos(4Ω)−jsin(4Ω)])+(-0.143424235*[cos(3Ω)−jsin(3Ω)])+(-0.042972332*[cos(2Ω)−jsin(2Ω)])+(0.229366476*[cos(Ω)−jsin(Ω)])+(0.401816673)+(0.229366476*[cos(Ω)+jsin(Ω)])+(-0.042972330*[cos(2Ω)+jsin(2Ω)])+(-0.143424235*[cos(3Ω)+jsin(3Ω)])+(-0.243878250*[cos(4Ω)+jsin(4Ω)])
# Ipcos⁡3θ = (0.116790202*[cos(4Ω)−jsin(4Ω)])+(-0.060968048*[cos(3Ω)−jsin(3Ω)])+(-0.238731368*[cos(2Ω)−jsin(2Ω)])+(0.038429971*[cos(Ω)−jsin(Ω)])+(0.288958485)+(0.038429971*[cos(Ω)+jsin(Ω)])+(-0.238731370*[cos(2Ω)+jsin(2Ω)])+(-0.060968048*[cos(3Ω)+jsin(3Ω)])+(0.116790202*[cos(4Ω)+jsin(4Ω)])
# ---------------------------------------------------------

Hr = (0.674972152 * (np.cos(4 * Omega) - 1j * np.sin(4 * Omega))) + (-0.364346074 * (np.cos(3 * Omega) - 1j * np.sin(3 * Omega))) + (-0.621244916 * (np.cos(2 * Omega) - 1j * np.sin(2 * Omega))) + (-0.364360555 * (np.cos(Omega) - 1j * np.sin(Omega))) + (0.364360555 * (np.cos(Omega) + 1j * np.sin(Omega))) + (0.621244916 * (np.cos(2 * Omega) + 1j * np.sin(2 * Omega))) + (0.364346074 * (np.cos(3 * Omega) + 1j * np.sin(3 * Omega))) + (-0.674972150 * (np.cos(4 * Omega) + 1j * np.sin(4 * Omega)))
Hr3 = (-0.100263157 * (np.cos(4 * Omega) - 1j * np.sin(4 * Omega))) + (0.229849810 * (np.cos(3 * Omega) - 1j * np.sin(3 * Omega))) + (-0.009174009 * (np.cos(2 * Omega) - 1j * np.sin(2 * Omega))) + (-0.270148784 * (np.cos(Omega) - 1j * np.sin(Omega))) + (0.270148784 * (np.cos(Omega) + 1j * np.sin(Omega))) + (0.009174009 * (np.cos(2 * Omega) + 1j * np.sin(2 * Omega))) + (-0.229849810 * (np.cos(3 * Omega) + 1j * np.sin(3 * Omega))) + (0.100263157 * (np.cos(4 * Omega) + 1j * np.sin(4 * Omega)))
# Magnitude and Phase for Real Part
Hr_mag = np.abs(Hr)
Hr_mag3 = np.abs(Hr3)
Hr_phase = np.angle(Hr, deg=True)
Hr_phase3 = np.angle(Hr3, deg=True)

Hi = (-0.243878245 * (np.cos(4 * Omega) - 1j * np.sin(4 * Omega))) + (-0.143424235 * (np.cos(3 * Omega) - 1j * np.sin(3 * Omega))) + (-0.042972332 * (np.cos(2 * Omega) - 1j * np.sin(2 * Omega))) + (0.229366476 * (np.cos(Omega) - 1j * np.sin(Omega))) + (0.401816673 * (np.cos(Omega) + 1j * np.sin(Omega))) + (0.229366476 * (np.cos(Omega) + 1j * np.sin(Omega))) + (-0.042972330 * (np.cos(2 * Omega) + 1j * np.sin(2 * Omega))) + (-0.143424235 * (np.cos(3 * Omega) + 1j * np.sin(3 * Omega))) + (-0.243878250 * (np.cos(4 * Omega) + 1j * np.sin(4 * Omega)))
Hi3 = (0.116790202 * (np.cos(4 * Omega) - 1j * np.sin(4 * Omega))) + (-0.060968048 * (np.cos(3 * Omega) - 1j * np.sin(3 * Omega))) + (-0.238731368 * (np.cos(2 * Omega) - 1j * np.sin(2 * Omega))) + (0.038429971 * (np.cos(Omega) - 1j * np.sin(Omega))) + (0.288958485 * (np.cos(Omega) + 1j * np.sin(Omega))) + (0.038429971 * (np.cos(Omega) + 1j * np.sin(Omega))) + (-0.238731370 * (np.cos(2 * Omega) + 1j * np.sin(2 * Omega))) + (-0.060968048 * (np.cos(3 * Omega) + 1j * np.sin(3 * Omega))) + (0.116790202 * (np.cos(4 * Omega) + 1j * np.sin(4 * Omega)))
# Magnitude and Phase for Imaginary Part
Hi_mag = np.abs(Hi)
Hi_mag3 = np.abs(Hi3)
Hi_phase = np.angle(Hi, deg=True)
Hi_phase3 = np.angle(Hi3, deg=True)

'''
                    # ---------------------------------------------------------
                                  PLOTTING FREQUENCY RESPONSES
                    # ---------------------------------------------------------
''' 

plt.figure(figsize=(12, 8))

plt.subplot(2,2,1)
plt.plot(freq, Hr_mag)
plt.title('Real Filter Magnitude Response 60Hz')             # Real Magnitude Response
plt.xlabel('Frequency (Hz)')
plt.ylabel('|Hr(f)|')
plt.grid(True)

plt.subplot(2,2,2)
plt.plot(freq, Hi_mag)
plt.title('Imaginary Filter Magnitude Response 60Hz')        # Imaginary Magnitude Response
plt.xlabel('Frequency (Hz)')
plt.ylabel('|Hi(f)|')
plt.grid(True)

plt.subplot(2,2,3)
plt.plot(freq, Hr_mag3)
plt.title('Real Filter Magnitude Response 180Hz')             # Real Magnitude Response
plt.xlabel('Frequency (Hz)')
plt.ylabel('|Hr(f)|')
plt.grid(True)

plt.subplot(2,2,4)
plt.plot(freq, Hi_mag3)
plt.title('Imaginary Filter Magnitude Response 180Hz')        # Imaginary Magnitude Response
plt.xlabel('Frequency (Hz)')
plt.ylabel('|Hi(f)|')
plt.grid(True)

plt.tight_layout()
plt.show()
