from PIL import Image
im=Image.open("out3.png")
im = im.resize((192, 108), Image.NEAREST)
im.save("out4.png")
# #
# import sys
# from PIL import Image
#
# img=Image.open(sys.argv[1])
#
# img = img.resize((192, 108), Image.NEAREST)
# img.save(sys.argv[2])