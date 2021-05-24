# 创建人：郭雨龙
# 创建时间：2021/5/15 9:26
"""画图相关的功能文件"""
from matplotlib import pyplot as plt
from matplotlib import animation
# 引入多进程库
import multiprocessing
# 将matplotlib调整为交互式窗口显示，不添加此行无法显示动图
plt.switch_backend('TkAgg')

# tkinter与matplotlib不能显示在同一个画布上，所以需要设计一个多进程编程
class Plot(multiprocessing.Process):
    def __init__(self):
        # 设置主进程结束，子进程会被同步销毁
        super().__init__(daemon=True)
        # matplotlib组件的基本使用
        # 在哪个画布上进行作画
        self.fig = plt.figure()
        # 得到坐标轴
        self.ax = plt.axes()
        # 进行作画，这里使用line,进行赋值，使得其值为单值元组中的第一部分
        self.line, = self.ax.plot([], [])
        self.data = []

    def update(self,frame):
        self.data.append(frame ** 2)
        y = self.data
        # 将x轴变为与y轴等长
        # x = [i for i in range(data)]，下一行与此行等价将range返回的可迭代对象转化为数组
        x = list(range(len(self.data)))
        # 调整坐标轴的显示
        self.ax.relim()
        self.ax.autoscale_view()
        self.line.set_data(x, y)
        return self.line,


    def anima_init(self):
        self.line.set_data([],[])
        # 要求返回一个元组，当只返回line的时候，需要构造一个只有line的元组
        return self.line,

    def run(self):
    # run函数是每次新建进程时会自动call的一个函数
    # 画出动态图像，参数含义：
    # 1.画布，2下一帧函数，3.帧数范围，4.画图初始化函数，5.时间间隔ms，6.优化
        _ = animation.FuncAnimation(self.fig,
                                    self.update,
                                    frames=range(1, 100),
                                    init_func=self.anima_init,
                                    interval=100,
                                    blit=False)
        plt.show()



if __name__ == "__main__":
    p = Plot()
    p.run()