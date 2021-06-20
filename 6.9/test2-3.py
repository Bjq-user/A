from thinkdsp import decorate,SquareSignal,SinSignal,read_wave
import matplotlib.pyplot as plt
from winsound import PlaySound
from IPython.display import display
import wave

square = SquareSignal(1100).make_wave(duration=0.5, framerate=100000)
plt.subplot(2,1,1)
square.plot()
plt.xlim(0,0.01)
decorate(xlabel="Time(s)")

plt.subplot(2,1,2)
square.make_spectrum().plot()
decorate(ylabel="Frequency(Hz)")
decorate(xlabel="Time(s)")

square.make_audio()

wave = SinSignal(500).make_wave(duration=0.5,framerate=10000).make_audio()

plt.show()
