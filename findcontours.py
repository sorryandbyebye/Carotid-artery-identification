import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import sympy as sp
print(cv2.__version__)
'''----------------------------------先取得一个roi-----------------------------------------------'''
img0 = cv2.imread("C:/Users/lenovo/Desktop/wgz/pic/img1.bmp")
img1 = img0[170:300, 520:660]#img1是[170:300, 520:660]
print(img1.shape)
imgCopy1 = img1.copy()
imgCopy2 = img1.copy()
imgCopy3 = img1.copy()
'''------------------------------------变成灰度图------------------------------------------------'''
imgGray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
imgGray2 = imgGray1.copy()
print("imgGray1", imgGray1.shape)
'''------------------------------------阈值分割------------------------------------------------'''
ret, imgBinary = cv2.threshold(imgGray1, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)#(src,阈值,最大值,阈值类型)
x, y = imgBinary.shape#x行y列
# print(imgBinary)
# print(imgBinary.shape)
# a=imgBinary[2][3]
# b=imgBinary[2, 3]
# print(imgBinary[2][3])
# print(imgBinary[2, 3])
'''----------------------------------------腐蚀和画边框------------------------------------------------'''
# kernel = np.ones((1, 1), np.uint8)
# imgErode = cv2.erode(imgBinary, kernel)
#
# contour, hierarchy = cv2.findContours(imgBinary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
# imgDrawContours1 = cv2.drawContours(imgCopy1, contour, -1, (255, 0, 0), 1)
'''-----------------------画中膜的上边的外膜的下边(进行上下对称处理)-------------------------------------'''
for j in range(y):
    count = 0
    for i in range(int(x/2), x):
        if i == x-2:
            count = 0
            break
        if int(imgBinary[i+1][j])-int(imgBinary[i][j]) == 255:
            count += 1
            if count == 2:
                imgCopy1[i][j] = (0, 255, 0)
                imgCopy1[a][j] = (0, 255, 0)
            a = i
'''------------------------------------展示图片------------------------------------------------'''
cv2.imshow("img1", img1)
cv2.resizeWindow("img1", 300, 300)
cv2.imshow("imgbinary", imgBinary)
cv2.resizeWindow("imgbinary", 300, 300)
# cv2.imshow("imgErode", imgErode)
# cv2.resizeWindow("imgErode", 300, 300)
# cv2.imshow("imgDrawContours1", imgDrawContours1)
# cv2.resizeWindow("imgDrawContours1", 300, 300)
cv2.imshow("imgCopy1", imgCopy1)
cv2.resizeWindow("imgCopy1", 300, 300)

cv2.waitKey(0)