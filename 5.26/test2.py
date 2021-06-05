import wave

import scipy as sp
from thinkdsp import Spectrum, read_wave
import matplotlib.pyplot as plt

wave = read_wave("170255__dublie__trumpet.wav")
wave.normalize()
wave.make_audio()

plt.subplot(3,1,1)
wave.plot()

# 从1.1秒开始截取0.5秒的音频作为SinSignal
SinSignal = wave.segment(start=1.1, duration=0.5)
SinSignal.make_audio()
plt.subplot(3,1,2)
SinSignal.plot()

# 从2.1秒开始截取0.5秒的音频作为CosSignal
CosSignal = wave.segment(start=2.1, duration=0.5)
CosSignal.make_audio()
plt.subplot(3,1,3)
CosSignal.plot()

# 显示频谱
# spectrum = segment.make_spectrum()
# 频谱横坐标
# plt.subplot(2,1,1)
# spectrum.plot(high=7000)

# plt.subplot(2,1,2)

plt.show()