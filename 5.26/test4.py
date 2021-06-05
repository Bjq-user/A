from thinkdsp import read_wave, play_wave
import matplotlib.pyplot as plt
import wave

wave = read_wave(filename="170255__dublie__trumpet.wav")
wave.normalize()
wave.make_audio()

def stretch(wave, factor):
    wave.ts *= factor
    wave.framerate /= factor

stretch(wave, 0.5)
wave.make_audio()
wave.plot()
plt.show()