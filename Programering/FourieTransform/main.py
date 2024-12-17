import matplotlib.pyplot as plt
import numpy as np
import random

sample_rate = 10
signal = []
antalBølger = 5


def waveGenerater(amplitude, vinkelfrekvens, faseforskydning, k, t):
    f = (amplitude * np.sin(vinkelfrekvens * t + faseforskydning) + k)
    return f

def timeGenerator(sample_rate):
    t = np.linspace(0, 2 * np.pi, sample_rate)
    return t


for i in range(antalBølger):
    signal.append(waveGenerater(random.randint(1, 5), random.randint(1, 5), random.randint(1, 5), random.randint(1, 5), timeGenerator(sample_rate)))

    combindeWave = np.sum(signal, axis=0)

print(timeGenerator(sample_rate))
print(waveGenerater(1, 1, 1, 1, timeGenerator(sample_rate)))

plt.plot(timeGenerator(sample_rate), combindeWave, label='combindeWave')
plt.legend()
plt.grid()

plt.show()