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
# Ipsin⁡θ=(-0.111182*[cos(4Ω)−jsin(4Ω)])+(-0.278484*[cos(3Ω)−jsin(3Ω)])+(-0.047404*[cos(2Ω)−jsin(2Ω)])+(0.165802*[cos(Ω)−jsin(Ω)])+(0.294745)+(-0.389094*[cos(4Ω)−jsin(4Ω)])
# IMAGINARY PART Z TRANSFER FUNCTION
# Ipcos⁡θ=(0.364024*[cos(4Ω)−jsin(4Ω)])+(-0.316265*[cos(3Ω)−jsin(3Ω)])+(-0.232111*[cos(2Ω)−jsin(2Ω)])+(-0.085974*[cos(Ω)−jsin(Ω)])+(0.065169)+(-0.16925*[cos(4Ω)−jsin(4Ω)])
# ---------------------------------------------------------

Hr = (-0.111182 * (np.cos(4 * Omega) - 1j * np.sin(4 * Omega))) + (-0.278484 * (np.cos(3 * Omega) - 1j * np.sin(3 * Omega))) + (-0.047404 * (np.cos(2 * Omega) - 1j * np.sin(2 * Omega))) + (0.165802 * (np.cos(Omega) - 1j * np.sin(Omega))) + (0.294745) + (-0.389094 * (np.cos(4 * Omega) - 1j * np.sin(4 * Omega)))
# Magnitude and Phase for Real Part
Hr_mag = np.abs(Hr)
Hr_phase = np.angle(Hr, deg=True)

Hi = (0.364024 * (np.cos(4 * Omega) - 1j * np.sin(4 * Omega))) + (-0.316265 * (np.cos(3 * Omega) - 1j * np.sin(3 * Omega))) + (-0.232111 * (np.cos(2 * Omega) - 1j * np.sin(2 * Omega))) + (-0.085974 * (np.cos(Omega) - 1j * np.sin(Omega))) + (0.065169) + (-0.16925 * (np.cos(4 * Omega) - 1j * np.sin(4 * Omega)))
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

# ---------------------------------------------------------
# Frequency Axis
# From 0 to 720 Hz
# ---------------------------------------------------------
f = 180                     # Fundamental frequency (Hz)
fs = 720                    # Sampling frequency (Hz)
freq = np.linspace(0, fs, 1000)
omega = 2 * np.pi * freq       # Angular frequency
# Convert frequency to digital frequency
Omega = omega / fs

# ---------------------------------------------------------
# REAL PART Z TRANSFER FUNCTION
# Ipsin⁡θ=(0.181185*[cos(4Ω)−jsin(4Ω)])+(-0.011324*[cos(3Ω)−jsin(3Ω)])+(-0.229965*[cos(2Ω)−jsin(2Ω)])+(-0.038328*[cos(Ω)−jsin(Ω)])+(0.179443*i(0))+(-0.013066*i(1))+(-0.231707*i(2))+(-0.013937*i(3))+(0.177700*i(4))
# IMAGINARY PART Z TRANSFER FUNCTION
# Ipcos⁡θ=(-0.013937*[cos(4Ω)−jsin(4Ω)])+(0.250871*[cos(3Ω)−jsin(3Ω)])+(-0.059233*[cos(2Ω)−jsin(2Ω)])+(-0.343206*[cos(Ω)−jsin(Ω)])+(-0.052265*i(0))+(0.212544*i(1))+(-0.097561*i(2))+(0.193380*i(3))+(-0.090592*i(4))
# ---------------------------------------------------------

Hr = 0.181185*(np.cos(4*Omega)-1j * np.sin(4*Omega))
-0.011324*(np.cos(3*Omega)-1j * np.sin(3*Omega))
-0.229965*(np.cos(2*Omega)-1j * np.sin(2*Omega))
-0.038328*(np.cos(Omega)-1j * np.sin(Omega))
+0.179443
-0.013066*(np.cos(Omega)+1j * np.sin(Omega))
-0.231707*(np.cos(2*Omega)+1j * np.sin(2*Omega))
-0.013937*(np.cos(3*Omega)+1j * np.sin(3*Omega))
+0.177700*(np.cos(4*Omega)+1j * np.sin(4*Omega))
# Magnitude and Phase for Real Part
Hr_mag = np.abs(Hr)
Hr_phase = np.angle(Hr, deg=True)

Hi = -0.013937*(np.cos(4*Omega)-1j * np.sin(4*Omega))
+0.250871*(np.cos(3*Omega)-1j * np.sin(3*Omega))
-0.059233*(np.cos(2*Omega)-1j * np.sin(2*Omega))
-0.343206*(np.cos(Omega)-1j * np.sin(Omega))
-0.052265
+0.212544*(np.cos(Omega)+1j * np.sin(Omega))
-0.097561*(np.cos(2*Omega)+1j * np.sin(2*Omega))
+0.193380*(np.cos(3*Omega)+1j * np.sin(3*Omega))
-0.090592*(np.cos(4*Omega)+1j * np.sin(4*Omega))
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
plt.show()
