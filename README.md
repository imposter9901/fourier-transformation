# Fourier Transform Signal Generator

This project generates a signal with a given number of sine waves and plots the signal in the time domain and its Discrete Fourier Transform (DFT) in the frequency domain.

## Setup

1. Clone the repository.
2. Navigate to the `FourieTransform` directory.
3. Activate the virtual environment:
    - On Windows:
        ```sh
        .\Scripts\activate
        ```
    - On Unix or MacOS:
        ```sh
        source Scripts/activate
        ```
## Usage 

Run the `Fouir_transformation.py` script to generate and plot the signal and its DFT:
```sh
python Fouir_transformation.py
```

### Changing Signal Parameters
To customize the signal parameters, you need to modify the `signalProperties` variable in the `Fouir_transformation.py` file. This variable is a list of tuples, where each tuple represents a sine wave with the following parameters:

* Amplitude (a)
* Frequency (f)
* Phase (phi)
* Offset (k)

For example:

```sh
#Input signal properties
signalProperties = [[a, f, phi, k]], # Amplitude, frequency, phase, off-set                        
```