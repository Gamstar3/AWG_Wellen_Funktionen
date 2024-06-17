import numpy as np

T = 10.0     
sampling_rate = 1000   
t = np.linspace(0, T, int(T * sampling_rate))   

def sawtooth_wave(t, f_1, N):
    signal = np.zeros_like(t)
    for n in range(1, N+1):
        signal += (1/n) * np.sin(np.pi * n * f_1 * t)
    return signal
