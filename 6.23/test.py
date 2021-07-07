import wave
import numpy as np
import matplotlib.pyplot as plt
from thinkdsp import Chirp
from thinkdsp import decorate

# 从A3到A5做一个线性啁啾
# 扫过的频率为220-880Hz，相当于从A3到A5
signal = Chirp(start=220, end=880)
# 持续时间为2s，返回一个Wave对象
wave1 = signal.make_wave(duration=2)
wave1.make_audio()

plt.show()
