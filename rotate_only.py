# import cv2
# from random import randint
#
# img = cv2.imread('e.jpg',0)
# rows,cols = img.shape
#
#
# for i in range(0,10, 1):
#     M = cv2.getRotationMatrix2D((cols/2,rows/2),randint(0,360),1)
#     dst = cv2.warpAffine(img,M,(cols,rows))
#
#
#     cv2.imshow('image1',dst)
#     cv2.waitKey(0)

from random import randint
from PIL import Image

img = Image.open('e.jpg')

for i in range(0,5, 1):
    img2 = img.rotate(randint(0,360))
    img2.show()