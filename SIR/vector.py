# 创建人：郭雨龙
# 创建时间：2021/5/3 15:42
# 简单的向量加减法
# 这里用到了Python的运算符重载 __add__ __sub__ __eq__
class Vector:
    """定义一个简单的二维向量类"""
    def __init__(self,x,y):
        self.x = x
        self.y = y

    # 自定义一个复制函数
    def copy(self):
        return Vector(self.x,self.y)

    # 重定义Vector的加法
    def __add__(self, other):
        # v1 + v2 = v3
        return Vector(self.x+other.x,self.y+other.y)

    # 重定义Vector的减法
    def __sub__(self, other):
        return Vector(self.x-other.x,self.y-other.y)

    # 重定义vector的==
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # 调用length属性，向量的length就是x^2+y^2开根号，这里使用函数加@property实现类似属性的调用
    @property
    def length(self):
        return (self.x*self.x + self.y*self.y) ** 0.5

    # 编写标准化uniform函数
    def uniform(self,length):
        return Vector(self.x/self.length *length,self.y/self.length*length)
