import wave

import scipy as sp
from thinkdsp import Spectrum, read_wave, decorate
import matplotlib.pyplot as plt
from IPython.display import display
from winsound import PlaySound

wave = read_wave("170255__dublie__trumpet.wav")
wave.normalize()
wave.make_audio()
# plt.subplot(2,1,1)
# plt.title("The original audio")
# wave.plot()

def play(file, flags):
    print('play audio'+file)
    PlaySound(file, flags)

# play('170255__dublie__trumpet.wav', flags=1)

# 从1.1秒开始截取0.5秒的音频
segment = wave.segment(start=1.1, duration=0.5)
# segment.make_audio()
# plt.subplot(2,1,2)
# plt.title("Capture snippets of audio")
# segment.plot()
segment.write("output.wav")
play("output.wav", flags=1)
# 显示 频谱
spectrum = segment.make_spectrum()
# 频谱横坐标频率
plt.subplot(2,1,1)
spectrum.plot(high=7000)

plt.subplot(2,1,2)
# spectrum.low_pass(2000)
# spectrum.high_pass(1000)
spectrum.band_stop(1000,2000)
spectrum.plot(high=3000)

spectrum.make_wave().make_audio()
def filter_wave(wave, start, duration, cutoff):
    """Selects a segment from the wave and filters it.
    
    Plots the spectrum and displays an Audio widget.
    
    wave: Wave object
    start: time in s
    duration: time in s
    cutoff: frequency in Hz
    """
    segment = wave.segment(start, duration)
    spectrum = segment.make_spectrum()

    spectrum.plot(high=5000, color='0.7')
    spectrum.low_pass(cutoff)
    spectrum.plot(high=5000, color='#045a8d')
    decorate(xlabel='Frequency (Hz)')
    
    audio = spectrum.make_wave().make_audio()
    display(audio)

plt.show()