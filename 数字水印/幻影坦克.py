# 创建人：郭雨龙
# 创建时间：2021/5/6 14:20
# 在这里实现幻影坦克相关的代码
from PIL import Image
# 将读入的图像取灰度
whiteimage=Image.open("1顶.png").convert("L")
blackimage=Image.open("2顶.png").convert("L")
# new类，第一个参数传入mode图像类型，第二个参数传入一个元组表示图像大小
imgTank = Image.new("RGBA",(whiteimage.width,whiteimage.height))
pixel=[]
# 计算合成每个像素点的透明度
for wid in range(1,whiteimage.width):
    for high in range(1,whiteimage.height):
        pA = whiteimage.getpixel((wid,high))
        pB = blackimage.getpixel((wid,high))
        alpha = 255 - (pA - pB)
        gray = int(255*pB/alpha)
        imgTank.putpixel((wid,high),(gray,gray,gray,alpha))
        pixel.append(gray)
        pixel.append(alpha)
print(pixel)
imgTank.save("幻影坦克.png")
