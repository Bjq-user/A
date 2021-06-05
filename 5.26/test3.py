from thinkdsp import SinSignal, CosSignal , Spectrum, read_wave, decorate
import matplotlib.pyplot as plt
import wave

# 绘制一个频率400,振幅为1的正弦信号
sinSignal = SinSignal(freq=400, amp=1.0)
# plt.subplot(2,1,1)
# sinSignal.plot()
# 绘制一个频率600,振幅为0.5的余弦信号

cosSignal = CosSignal(freq=600, amp=0.5)
# plt.subplot(2,1,2)
# cosSignal.plot()

mix = sinSignal + cosSignal

# 产生一个长度为0.5秒,开始时间为0,每秒帧数为11025的信号
wave = mix.make_wave(duration=0.5, start=0, framerate=11025)
# wave.apodize()
# wave.make_audio()

# 得到其中一段波形
# period = mix.period
# segment = wave.segment(start=0, duration=period*6)
# segment.plot()

# 显示频谱
spectrum = wave.make_spectrum()
spectrum.plot(high=1000)
plt.show()