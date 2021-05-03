# 创建人：郭雨龙
# 创建时间：2021/5/1 15:44
import tkinter
from engine import Engine
"""这里存储SIR项目的所有的前端代码"""
# 常量命名规范，全大写+下划线连接
CANVAS_SIZE = 800
POPULATION = 500
class Interface:
    def __init__(self):
        # 创建一个tkinter窗口
        self.root = tkinter.Tk()
        # 创建一块画布，画布属于self.root
        self.canvas = tkinter.Canvas(self.root,bg="white",width=CANVAS_SIZE,height=CANVAS_SIZE)
        # 将数据装载如(画入)tkinter中
        self.canvas.pack()
        # 将引擎传入前端
        self.engine = Engine(CANVAS_SIZE,POPULATION)
        # 使用引擎创建人
        self.engine.create()

    def draw_people(self):
        """画出每个人的位置"""
        # 根据患病情况确认颜色，使用字典，这里体现了数据与条件分离的编程思想
        color = {
            "S":"green",
            "I":"red",
            "R":"yellow"
        }
        # 更具person的status，获取其对应的颜色
        for person in self.engine.persons:
            self.canvas.create_rectangle(person.x-2,person.y-2,person.x+2,person.y+2,fill=color[person.status],outline=color[person.status])

    def next_frame(self):
        """确定下一帧动画中动点的位置"""
        # 更新person的位置
        self.engine.next_fream()
        # 擦除上一次遗留下来的点
        self.canvas.delete("all")
        # 画出当前时间段所有人
        self.draw_people()
        # 延时函数，延时30毫秒后执行next_frame函数
        self.root.after(30,self.next_frame)

    def start(self):
        # 在人群中插入一批感染者
        self.engine.infect(10)
        self.root.after(30, self.next_frame)
        """运行窗口"""
        self.root.mainloop()

# 当直接运行的时候会调用，import则不会运行
if __name__ == "__main__":
    # 实例化
    interface = Interface()
    # 调用
    interface.start()