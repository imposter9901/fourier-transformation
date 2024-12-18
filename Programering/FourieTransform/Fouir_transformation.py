# ---------------------------------------
# Description: This code generates a signal with a given number of sin waves and plots the signal in the time domain 
# and its Discrete Fourier Transform (DFT) in the frequency domain.
# ---------------------------------------

import numpy as np
import matplotlib.pyplot as plt
import datetime


# Functions ---------------------------------------

def timeGenerator(signalProperties):
    # Generate an array of time values
    # Generated to match two periods of the lowest frequency in the signal (longest duration in time)
    # Number of samples are calculated to fullfill Nyquist sampling criteria
    
    frequencyArray = [] # Temp array to store the frequencies in the signal

    for row in range(len(signalProperties)):
        frequencyArray.append(signalProperties[row][1]) # Add the frequency of each wave to the array

    lowestFrequency = min(frequencyArray) # Find the lowest frequency in the signal
    highestFrequency = max(frequencyArray) # Find the highest frequency in the signal
    minSamplingFrequency = 2 * highestFrequency # Sampling frequency must be at least twice the highest frequency in the signal
    numberOfSamples = 10*int(minSamplingFrequency / lowestFrequency) # Number of samples in the signal - The factor 10 is added to make smmoth plots

    print(f"Signal frequencies: {frequencyArray}")
    print(f"Lowest frequency: {lowestFrequency}")
    print(f"Highest frequency: {highestFrequency}")
    print(f"Minimum sampling frequency: {minSamplingFrequency}")
    print(f"Number of samples: {numberOfSamples}")

    t = np.linspace(0, 2* 1/lowestFrequency, numberOfSamples)

    return t

def frequencyGenerator(timeDomainAxis):
    # Generate an array of frequencies corresponding to the time domain
    
    sampleTime = timeDomainAxis[1] - timeDomainAxis[0]

    print(f"Actual sampling frequency: {int(1/sampleTime)}")
    
    f = np.fft.fftfreq(len(timeDomainAxis), d=(sampleTime)) # Compute the frequencies corresponding to the time values

    return f

def waveGenerator(a, f, phi, k, t):
    # API: a: amplitude, f: frequency, phi: phase, k: off-set, t: time array

    omega = 2 * np.pi * f # Angular frequency
    sineWave = (a * np.sin(omega * t + phi) + k) # Generate the f(t) values for each time value in the array

    # Return the array of the sine wave
    return sineWave

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
        F.append(X_k/(N/2))

    # Return the list of frequencies
    return np.array(F)

def combineWave(signalProperties, t):
    # Stores the combined wave
    signal = np.zeros_like(t)

    # Iterate through the number of waves
    for row in range(len(signalProperties)):
        signal = signal + waveGenerator(signalProperties[row][0], signalProperties[row][1], signalProperties[row][2], signalProperties[row][3], t)
       
    return signal

def plotWave(t, f, frequencies, F):
    # Plot the original signal and its DFT positive frequencies
     
    # Define the figure and the subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    
    # Plot the time domain signal
    ax1.plot(t, f)
    ax1.set_title('Time Domain Signal')
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Amplitude')
   

    # Only keep the positive frequencies
    positive_frequencies = frequencies[:len(frequencies) // 2]
    positive_F = F[:len(F) // 2]

    # Plot the DFT of the signal
    ax2.plot(positive_frequencies, np.abs(positive_F))
    ax2.set_title('Discrete Fourier Transform (DFT)')
    ax2.set_xlabel('Frequency')
    ax2.set_ylabel('Magnitude')

    # Display the plot
    plt.tight_layout()
    plt.show()



# Main code ---------------------------------------
print("-------------------------------------------------")
print(f"BEGIN:{__file__} @ {datetime.datetime.now()}")

#Input signal properties
signalProperties = [    [1, 200000, 0, 0], # Amplitude, frequency, phase, off-set
                        [1, 1000, 0, 0],
                        [1, 120000, 0, 0]]


# Time Domain Signal
t = timeGenerator(signalProperties)
signals = combineWave(signalProperties, t)

# Frequency Domain Signal
f = frequencyGenerator(t)
DFT_signals = DFT(signals)

# Plot the signals
plotWave(t, signals, f, DFT_signals)