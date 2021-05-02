# 创建人：郭雨龙
# 创建时间：2021/5/1 15:44
import tkinter
"""这里存储SIR项目的所有的前端代码"""
# 常量命名规范，全大写+下划线连接
CANVAS_SIZE = 800
class Interface:
    def __init__(self):
        # 创建一个tkinter窗口
        self.root = tkinter.Tk()
        # 创建一块画布，画布属于self.root
        self.canvas = tkinter.Canvas(self.root,bg="green",width = CANVAS_SIZE,height = CANVAS_SIZE)
        # 将数据装载如(画入)tkinter中
        self.canvas.pack()

    def next_frame(self):
        """确定下一帧动画中动点的位置"""
        # 擦除上一次遗留下来的点
        self.canvas.delete("all")
        """画出一个长方形，给出左上角的x,y点与右下角的x,y点，还可以使用fill指定内部颜色，outline指定边框颜色"""
        self.canvas.create_rectangle(self.x-4, self.y-4, self.x+4, self.y+4, fill="red",outline="blue")
        # 移动视觉中心
        self.y += 2
        self.x += 2
        # 延时函数，延时30毫秒后执行next_frame函数
        self.root.after(30,self.next_frame)

    def start(self):
        # 设置视觉中心
        self.x = 4
        self.y = 4
        self.root.after(30, self.next_frame)
        """运行窗口"""
        self.root.mainloop()

# 当直接运行的时候会调用，import则不会运行
if __name__ == "__main__":
    # 实例化
    interface = Interface()
    # 调用
    interface.start()