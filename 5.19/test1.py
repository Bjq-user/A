# 引入需要的库
import matplotlib.pyplot as plt
import numpy as np 
# linspace 第一个参数序列起始值, 第二个参数序列结束值,第三个参数为样本数默认50
# 即x范围在0到3π，分隔值总数为50
x = np.linspace(0, 3 * np.pi, 100)
# y轴范围是sin(x)
y = np.sin(x)

plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

# 图表绘图区域被分为一行两列的第一个图片
plt.subplot(1,2,1)
# 为第一个图片设置标题为f(x)=sin(x)
plt.title(r'$f(x)=sin(x)$')
# 以x,y作为该图像的横纵坐标
plt.plot(x, y)

# 为x1设定范围，从0到3π*(3/8)*π
x1 = [t*0.375*np.pi for t in x]
# 为y1设定范围，为sin(x1)
y1 = np.sin(x1)
# 图表绘图区域被分为一行两列的第二个图片
plt.subplot(1,2,2)
# 为图2设置标题为f(x)=sin(ωx),ω = 3/8π
plt.title(r'$f(x)=sin(\omega x), \omega = \frac{3}{8} \pi$')
# x，y1分别作为该图像的横纵坐标
plt.plot(x, y1)
# 显示图像
plt.show()
