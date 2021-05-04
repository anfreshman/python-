# 创建人：郭雨龙
# 创建时间：2021/5/2 21:09
# 所有后端的工作在这里完成(24:18)
import random
from vector import Vector
MOVE_RANGE = 50
MOVE_SPEED = 3
# 危险距离
UNSAFE_DISTANCE = 10
# 近距离感染可能性
INFECTIOUS_RATE = 0.7
# 恢复健康的时间(这里用帧数代替)
RECOVER_TIME = 300
class Person:
    """人类，即每个小方块，有大小和状态"""
    def __init__(self,engine):
        # 直接使用向量对当前点的坐标进行存储
        self.position = Vector(
            random.randrange(0,engine.size),
            random.randrange(0,engine.size)
        )
        # 存储初始点的位置，直接使用等号会导致引用传递，改一个后面也变了，所以要自己写复制函数
        self.home = self.position.copy()
        # 每一个人都有一个当前移动的目标点，到达之后即更换，设置初始目标点为home
        self.move_target = self.home.copy()
        # 活动范围(四方)
        self.move_range = MOVE_RANGE
        # 移动速度
        self.move_speed = MOVE_SPEED
        # 患病情况，默认为健康人
        self.status = "S"
        # 距离痊愈的时间
        self.recover_time_left = -1

    # 不设置成员变量，用函数实现动态调用，否则每一次修改position都需要修改一遍x
    @property
    def x(self):
        return self.position.x

    @property
    def y(self):
        return self.position.y

    def get_new_target(self):
        """获得新的目标点，目标点需要离家一定的距离内"""
        self.move_target = self.home + Vector(random.uniform(-self.move_range,self.move_range),random.uniform(-self.move_range,self.move_range))
        # 我们期望可以通过向量的加减，直接获取两点之间的方向与距离，并且进行一致话，使得每次移动的
        # 使用uniform()方法进行标准化，使得每次移动的距离的模都小于等于移动速度
        self.step = (self.move_target - self.position).uniform(self.move_speed)


    def move(self):
        """在person类中实现移动的功能(因为可以依靠一个人单独完成，不用交互)"""
        if self.position == self.move_target:
            # 如果已经到达目标点，则可以直接获取下一个目标地点
            self.get_new_target()
        # 如果还没有到达目标点，则根据算法进行一次位置的移动(距离的缩小),若当前距离小于一次移动的步长，那么直接使其移动到目标地点
        if(self.move_target-self.position).length < self.move_speed:
            self.position = self.move_target
        else:
            self.position = self.position + self.step

    def too_close(self,person):
        """判断两个人是否在危险距离之内"""
        return (self.position-person.position).length < UNSAFE_DISTANCE

    def try_infect(self,person):
        """尝试感染一个健康的人"""
        if(random.random() <= 0.3):
            person.status = "I"
            # 设置康复时间
            person.recover_time_left = RECOVER_TIME

class Engine:
    """引擎类，期望可以计算出每个人(正方形)的坐标与状态"""
    # 初始化方法，传入画布的大小与人数
    def __init__(self,size,population):
        self.size = size
        self.population = population

    def create(self,population = None):
        # 如果输入了population，将其赋值给self.population
        if population:
            self.population = population
        self.persons = []
        for i in range(self.population):
            self.persons.append(Person(self))

    def next_fream(self,move_range=None):
        """假定每个人都有一个出生地(person的第一次随机得到的点)，每一次运动都有一个目标点，
            以匀速向目标点前进，到达目标点后更换目标点，可以看出，向目标点的移动是一个简单的
            向量加减法的问题，目标点需要在出生点的范围之内"""
        for person in self.persons:
            # 如果前端传入了人群的移动范围，则更新每个人的移动范围
            if move_range:
               person.move_range = move_range
            person.move()
            # 患者尝试感染其他人
            if person.status == "I":
                for target in self.persons:
                    # 如果目标是未被感染过的健康人群，且距离足够近
                    if target.status == "S" and person.too_close(target):
                        # 尝试感染
                        person.try_infect(target)
                    #     判断是否即将康复
                    if target.recover_time_left == 0:
                        target.status = "R"
                    else:
                        target.recover_time_left -= 1

    def infect(self,number):
        """在已有的person列表中插入number个感染者"""
        # 使用random的sample函数从列表中随机抽取N个元素
        init_infect = random.sample(self.persons,number)
        for person in init_infect:
            person.status = "I"
            # 对于初始化的感染者，我们随机一个康复距离时间
            person.recover_time_left = random.uniform(1,RECOVER_TIME)