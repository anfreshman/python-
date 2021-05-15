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
        """初始化，得到tkinter的TK，并得到后端引擎，前端画布"""
        # 创建一个tkinter窗口
        self.root = tkinter.Tk()
        # 将引擎传入前端
        self.engine = Engine(CANVAS_SIZE,POPULATION)
        # 编写用户可输入选项，数据与逻辑相分离
        self.user_input = {
            "population":500,
            "move_range":50
        }
        # 将strvar定义为空字典，方便循环
        self.strvars = {}
        # 创建画布
        self.create_widget()


    def create_widget(self):
        """该方法创建一个画布以及在画布上创建一个其他小组件，如按钮"""
        for var in self.user_input:
            # 在canvas上面建立一个文本输入框,将输入内容保存到varstr中，输入框与varstr都属于一个frame
            frame = tkinter.Frame(self.root)
            # 创建strvar保存用户的输入
            strvar = tkinter.StringVar(frame)
            # 设置label
            label = tkinter.Label(frame,text=var)
            # 创建文本输入框
            entry = tkinter.Entry(frame,textvariable = strvar)
            # 设置文本框默认值
            strvar.set(self.user_input[var])
            # frame与entry是需要显示的，strvar不用显示，先pack先显示,使用side设置向左对齐，放在同一行
            label.pack(side=tkinter.LEFT)
            entry.pack(side=tkinter.LEFT)
            frame.pack()
            # 将读入的值返回给类属性
            self.strvars[var] = strvar
        # 创建一块画布，画布属于self.root
        self.canvas = tkinter.Canvas(self.root,bg="white",width=CANVAS_SIZE,height=CANVAS_SIZE)
        # 将数据装载如(画入)tkinter中
        self.canvas.pack()
        # 画出一个button，并且将其与self.restart方法/事件关联上
        self.restart_button = tkinter.Button(self.root,text="restart",command=self.restart)
        self.restart_button.pack()

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
        # 使用引擎创建人
        self.engine.create(self.user_input)
        # 在人群中插入一批感染者
        self.engine.infect(10)
        self.root.after(30, self.next_frame)
        """运行窗口"""
        self.root.mainloop()

    def restart(self):
        # 用strvar获取用户输入，这里直接使用int()进行强制类型转换会导致无法使用其他的数值类型
        # 例如小数，所以我们可以先使用type内置函数获得本身应有的type，得到typeobject
        for key in self.user_input:
            print(self.user_input[key])
            val_type = type(self.user_input[key])
            self.user_input[key] = val_type(self.strvars[key].get())
        # 将用户输入输入进create，并重载create函数，使得两种模式都可以用
        self.engine.create(self.user_input)
        self.engine.infect(10)
        # 这里不可以添加next_frame()，否则两个单独的next_frame()同时执行，会导致帧数滑动过快
        # self.next_frame(int(self.strvars["活动范围"].get()))

# 当直接运行的时候会调用，import则不会运行
if __name__ == "__main__":
    # 实例化
    interface = Interface()
    # 调用
    interface.start()