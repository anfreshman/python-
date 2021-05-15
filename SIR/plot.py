# 创建人：郭雨龙
# 创建时间：2021/5/15 9:26
"""画图相关的功能文件"""
from matplotlib import pyplot as plt
from matplotlib import animation

# matplotlib组件的基本使用
# 在哪个画布上进行作画
fig = plt.figure()
# 得到坐标轴
ax = plt.axes()
# 进行作画
ax.plot([1,2,3],[1,2,3])
fig.show()

def update(frame):
    pass

def anima_init():
    pass
# 画出动态图像，参数含义：
# 1.画布，2下一帧函数，3.帧数范围，4.画图初始化函数，5.时间间隔ms，6.优化
_ = animation.FuncAnimation(fig=fig,
                            update = update,
                            frames=range(1,100),
                            init_func=anima_init(),
                            interval = 100,
                            blit = False)