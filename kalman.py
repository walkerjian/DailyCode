'''
Kalman Filtering python test, with test cases
'''
import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, FloatLogSlider, IntSlider, Checkbox, Dropdown

# Constants
h = 6.62607015e-34  # Planck constant
c = 3e8  # speed of light
e = 1.602176634e-19  # electron charge

# Function for irradiance
def irradiance(theta, d, a, lam, n):
    return (2 * np.cos((np.pi * a * theta) / lam) ** 2 * np.sin((n * np.pi * d * theta) / lam) / (np.pi * d * theta / lam)) ** 2

# Function to convert frequency to wavelength
def freq_to_wavelength(freq):
    return c / freq

@interact
def plot_and_image(frequency=FloatLogSlider(value=5e14, base=10, min=14, max=15, step=0.01, description='Frequency (Hz):'),
                   a=FloatLogSlider(value=1e-6, base=10, min=-7, max=-5, step=0.01, description='Slit width (m):'),
                   d=FloatLogSlider(value=1e-6, base=10, min=-7, max=-5, step=0.01, description='Slit separation (m):'),
                   n=IntSlider(value=3, min=1, max=10, description='Number of slits:'),
                   log_scale=Checkbox(value=False, description='Log scale'),
                   color_map=Dropdown(options=['viridis', 'inferno', 'plasma', 'gray'], value='viridis', description='Color map')):
                   
    wavelength = freq_to_wavelength(frequency)
    theta = np.linspace(-np.pi, np.pi, 1000)
    irr = irradiance(theta, d, a, wavelength, n)

    if log_scale:
        irr = np.log(irr)

    fig, ax = plt.subplots(2, 1, figsize=(8, 10))
    
    ax[0].plot(theta, irr)
    ax[0].set_xlabel("Theta")
    ax[0].set_ylabel("log(Irradiance)" if log_scale else "Irradiance")
    
    ax[1].imshow(irr[np.newaxis, :], aspect='auto', cmap=color_map)
    ax[1].axis('off')

    plt.show()
