from thinkdsp import decorate, TriangleSignal
import numpy as np
import matplotlib.pyplot as plt

# 创建一个频率为440Hz的三角波，持续时间为0.01s，绘制波形
triangle = TriangleSignal().make_wave(duration=0.01)
plt.subplot(2,1,1)
triangle.plot()
decorate(xlabel="Time(s)")

spectrum = triangle.make_spectrum()
print(spectrum.hs[0])

spectrum.hs[0] = 100
plt.subplot(2,1,2)
triangle.plot()
spectrum.make_wave().plot(color="gray")
decorate(xlabel="Time(s)")

plt.show()