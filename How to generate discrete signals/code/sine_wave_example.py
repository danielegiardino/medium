import numpy as np
import matplotlib.pyplot as plt

# Sampling Frequency Fs=1 MHz
Fs = 1e6  # I can also write 1000000
Ts = 1/Fs

# Frequency of the sine wave 100 kHz
Fc = 125e3

# Normalized Frequency
F_N = Fc/Fs

# Number of samples
len = 32

# n variable
n = np.linspace(0, len-1, len);

# Discrete Time vector
t = n*Ts   # seconds
t = t*1e6  # scaling to obtain micro seconds

# Sine wave
x = np.sin(2*np.pi*F_N*n)

# Figure
plt.figure()

plt.subplot(2,1,1)
plt.plot(n, x, 's-', label='Sine Wave')
plt.title('Sine Wave')          # Title
plt.xlabel('Samples')           # x Label
plt.ylabel('Amplitude')         # y Label
plt.legend(loc='upper right')   # Legend
plt.grid()                      # Grid

plt.subplot(2,1,2)
plt.plot(t, x, 'x-', label='Sine Wave')   # Function to perform the plot
plt.xlabel('Time [$\mu$s]')               # x Label
plt.ylabel('Amplitude')                   # y Label
plt.legend()                              # Legend
plt.grid()                                # Grid

# Display the sine wave
plt.show() 
