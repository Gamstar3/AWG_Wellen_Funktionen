import numpy as np

def sawtooth_wave(f_1, N, S_R, T):     
    t = np.linspace(0, T, int(T * S_R))
    signal = np.zeros_like(t)
    for n in range(1, N+1):
        signal += (1/n) * np.sin(np.pi * n * f_1 * t)
    return signal
