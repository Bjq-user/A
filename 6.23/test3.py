import wave
import numpy as np
import matplotlib.pyplot as plt
from thinkdsp import Chirp, PI2, play_wave, read_wave
from thinkdsp import normalize, unbias, decorate, SawtoothSignal

wave = read_wave('72475__rockwehrmann__glissup02.wav')
wave.make_audio()

wave.make_spectrogram(512).plot(high=5000)
decorate(xlabel='Time (s)', ylabel='Frequency (Hz)')

plt.show()