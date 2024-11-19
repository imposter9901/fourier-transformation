import matplotlib.pyplot as plt
import numpy as np

sampleRate = 50

def waveGenerater(amplitude, vinkelfrekvens, faseforskydning, k, t):
    f = (amplitude * np.sin(vinkelfrekvens * t + faseforskydning) + k)
    return f

def timeGenerator(sample_rate):
    t = np.linspace(0, 2 * np.pi, sample_rate)
    return t

print(timeGenerator(sampleRate))
print(waveGenerater(1,2,0,0, timeGenerator(sampleRate)))

plt.plot(timeGenerator(sampleRate), waveGenerater(1,1,0,0, timeGenerator(sampleRate)), label='combindeWave')
plt.show()