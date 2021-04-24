# 创建人：郭雨龙
# 创建时间：2021/4/19 21:29

import sys
from PIL import Image

#将small_img中的像素用近邻法嵌入到big_img中，每(big_w/small_w)*(big_h/small_h)
#个big_img的图像中嵌入一个small_img的像素

# 读入图像
def my_nearest_resize(big_img, small_img):
    #得到图像的大小
    big_w, big_h = big_img.size
    small_w, small_h = small_img.size
    #复制一份图像矩阵
    dst_im = big_img.copy()
    #得到大图像上相对于小图像的点
    stepx = big_w/small_w
    stepy = big_h/small_h
    #
    for i in range(0, small_w):
        for j in range(0, small_h):
            map_x = int( i*stepx + stepx*0.5 )
            map_y = int( j*stepy + stepy*0.5 )
            if map_x < big_w and map_y < big_h :
                dst_im.putpixel( (map_x, map_y), small_img.getpixel( (i, j) ) )

    return dst_im



if __name__ == '__main__':
    big_img=Image.open(sys.argv[1])     # 大图
    small_img=Image.open(sys.argv[2])   # 小图

    dst_im = my_nearest_resize(big_img, small_img)
    dst_im.save(sys.argv[3])            # 嵌入小图像素的大图