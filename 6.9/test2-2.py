from numpy.__config__ import show
from thinkdsp import decorate, Sinusoid, normalize,unbias
import numpy as np
import matplotlib.pyplot as plt

# 通过SawtoothSignal生成锯齿波信号
class SawtoothSignal(Sinusoid):
    # 频率默认为440,振幅是1
    def evaluate(self, ts):
        # ts是对信号求值的采样时间的序列
        # cycles自起始时间的周期数
        cycles = self.freq * ts + self.offset / np.pi / 2
        # np.modf是将周期的数量分解成小数部分和整数部分
        # 并将整数部分忽略,小数部份存储再frac中
        # frac序列在0-1范围内
        frac, _ = np.modf(cycles)
        # unbias将波形下移使得其中心位于0,然后normalize将波形归一化到指定的振幅
        ys = normalize(unbias(frac),self.amp)
        return ys

# 生成锯齿波波形,持续时间为0.5,采样率为40000
sawtooth = SawtoothSignal().make_wave(duration=0.5, framerate=40000
)
sawtooth.make_audio()
plt.subplot(2,1,1)
sawtooth.plot()
plt.xlim(0,0.01)
decorate(xlabel="Time(s)")
# plt.show()

# 绘制矩形波信号频谱
plt.subplot(2,1,2)
sawtooth.make_spectrum().plot(high=1500)
decorate(xlabel="Frequency(Hz)")
plt.show()