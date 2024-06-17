import numpy as np
import matplotlib.pyplot as plt

f_1 = 1.0   #Grundfrequenz
T = 10.0     #Zeitraum
N = 20000     #Anzahl der Summenglieder
sampling_rate = 1000   #Abtastrate
t = np.linspace(0, T, int(T * sampling_rate))   #Zeitvektor

def sawtooth_wave(t, f_1, N):      #Sägezahn
    signal = np.zeros_like(t)
    for n in range(1, N+1):
        signal += (1/n) * np.sin(np.pi * n * f_1 * t)
    return signal

signal = sawtooth_wave(t, f_1, N)   #Berechnung der Welle

plt.plot(t, signal)
plt.title("Sägezahnwelle")
plt.xlabel("Zeit (s)")
plt.ylabel("Amplitude")
plt.grid()
plt.show()