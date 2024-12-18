import numpy as np
import matplotlib.pyplot as plt
import random

sample_rate = 50

numberOfWaves = 3
frequencyArray = [random.randint(1, 100) for _ in range(numberOfWaves)]

print(frequencyArray)

def timeGenerator(sample_rate):
    # Generate an array of time values from 0 to 2*pi, the sample rate is the number of samples in the array
    
    t = np.linspace(0, 2 * np.pi, sample_rate)

    return t

def waveGenerator(amplitude, vinkelfrekvens, faseforskydning, k, t):

    # Generate the f(t) values for each time value in the array
    f = (amplitude * np.sin(vinkelfrekvens * t + faseforskydning) + k)

    # Return the array of t, and f(t)
    return f

def DFT(f):
    
    # Compute the lenght of the signal
    N = len(f)

    # Saves the frequency information
    F = []

    # Iterate through the signals frequencys
    for k in range(N):
        
        # Stores the current frequency
        X_k = 0

        # Iterate through the samples in the signal
        for n in range(N):
            
            # Compute the complex number for the current frequency
            e = np.exp(2j * np.pi * k * n / N)

            # Find the frequency for the current sample
            X_k += f[n] * e

        # Append the frequency to the list of frequencies
        F.append(X_k)

    # Return the list of frequencies
    return np.array(F)

def combindeWave(numberOfWaves, frequencyArray, t):
    # Stores the combined wave
    signal = []

    # Iterate through the number of waves
    for i in range(numberOfWaves):
        
        # Generate the wave
        signal.append(waveGenerator(1, frequencyArray[i], 0, 0, t))

    # Combine the waves
    combindeWave = np.sum(signal, axis=0)

    # Return the combined wave
    return combindeWave




# Generate the time so all the waves are in the same time frame
t = timeGenerator(sample_rate)

f = combindeWave(numberOfWaves, frequencyArray, t)


# Compute the DFT of the signal
F = DFT(f)

#print(F)

# Compute the frequencies corresponding to the DFT values
frequencies = np.fft.fftfreq(len(f), d=(t[1] - t[0]) / (2 * np.pi))


# Only keep the positive frequencies
positive_frequencies = frequencies[:len(frequencies) // 2]
positive_F = F[:len(F) // 2]


# Plot the original signal and its DFT
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# Plot the original signal
ax1.plot(t, f)
ax1.set_title('Original Signal')
ax1.set_xlabel('Time')
ax1.set_ylabel('Amplitude')

# Plot the DFT of the signal
ax2.plot(positive_frequencies, np.abs(positive_F))
ax2.set_title('Discrete Fourier Transform (DFT)')
ax2.set_xlabel('Frequency')
ax2.set_ylabel('Magnitude')


plt.tight_layout()
plt.show()