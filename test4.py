import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import sympy as sp
print(cv2.__version__)
'''----------------------------------先取得一个roi-----------------------------------------------'''
img0 = cv2.imread("C:/Users/lenovo/Desktop/wgz/pic/img1.bmp")
img1 = img0[170:300, 520:660]
print(img1.shape)
imgCopy1 = img1.copy()
imgCopy2 = img1.copy()
imgCopy3 = img1.copy()
'''------------------------------------变成灰度图------------------------------------------------'''
imgGray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
imgGray2 = imgGray1.copy()
print("imgGray1", imgGray1.shape)
'''------------------------------------阈值分割------------------------------------------------'''

ret, imgbinary = cv2.threshold(imgGray1, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)#(src,阈值,最大值,阈值类型)

'''------------------------------------matplotlib------------------------------------------------'''
imgarr0 = np.sum(imgGray1, axis=1)/140#每个点255是满值
# print(np.sum(imgGray1, axis=1))
# plt.plot(np.sum(imgGray1, axis=1))
# plt.show()
#print(a)#得到一个一维数组
print(imgarr0)#得到一个一维数组
# imgarr1 = imgarr0.reshape(130, 1)#转成一个（130，1）的矩阵
# print(imgarr1.shape)
x = np.arange(0, 130, 1)
plt.plot(x, imgarr0)
x_major_locator = MultipleLocator(10)#把x轴的刻度间隔设置为1，并存在变量里
y_major_locator = MultipleLocator(10)#把y轴的刻度间隔设置为10，并存在变量里
ax = plt.gca()#ax为两条坐标轴的实例
ax.xaxis.set_major_locator(x_major_locator)#把x轴的主刻度设置为1的倍数
ax.yaxis.set_major_locator(y_major_locator)#把y轴的主刻度设置为10的倍数
#plt.show()
'''--------------------------------------求导--------------------------------------------------'''
differentLine = np.array([])
'''--------------------------------------求导——求差值------------------------------------------'''
for i in range(130):
    diffabs = np.abs(imgarr0[i+1]-imgarr0[i])
    differentLine = np.append(differentLine, diffabs)
    if i+1 == 129:
        break
print(differentLine)
print(i)
print(differentLine.shape)
plt.plot(differentLine)
# plt.show()
'''--------------------------------------求导——求梯度------------------------------------------'''
gradientLine = np.gradient(imgarr0)
print(gradientLine.shape)
plt.plot(gradientLine)
plt.show()
'''----------------------------------------找膜儿---------------------------------------------'''
'''----------------------------------------低通滤波-------------------------------------------'''
''''''
imgarr0Copy0 = np.array([])
for j in range(130):
    a = imgarr0[j]
    if a > 140:#/140对应这的140；/255对应这的75
        imgarr0Copy0 = np.append(imgarr0Copy0, [140])
    elif a < 40:#/140对应这的40；/255对应这的20
        imgarr0Copy0 = np.append(imgarr0Copy0, [0])
    else:
        imgarr0Copy0 = np.append(imgarr0Copy0, [a])
print(imgarr0Copy0.shape)
plt.plot(imgarr0Copy0)
plt.show()
'''-----------------------------------------找极值--------------------------------------------'''
'''---------------------------------------找大极值--------------------------------------------'''
def findMaxPeak(arrays):
    peakList = []
    for i in range(1, 129):
        if arrays[i-1] < arrays[i] > arrays[i+1]:
            print("i=", i)
            peakList.append(i)
            # return i
        if arrays[0] > arrays[1]:
            print("i=", 0)
            peakList.append(0)
            # return 89
        elif arrays[-1] > arrays[-2]:
            print("i=", 129)
            peakList.append(129)
            # return 129
        while(i == 128):
            return peakList
MaxPeakList = findMaxPeak(imgarr0Copy0)
print(MaxPeakList)
'''---------------------------------------找小极值--------------------------------------------'''
def findMinPeak(arrays):
    peakList = []
    for i in range(1, 129):
        if arrays[i-1] > arrays[i] < arrays[i+1]:
            print("i=", i)
            peakList.append(i)
            # return i
        # if arrays[0] < arrays[1]:
        #     print("i=", 0)
        #     peakList.append(0)
        #     # return 89
        # elif arrays[-1] < arrays[-2]:
        #     print("i=", 129)
        #     peakList.append(129)
            # return 129
        while(i == 128):
            return peakList
MinPeakList = findMinPeak(imgarr0Copy0)
print(MinPeakList)
'''----------------------------------识别出来的区域进行上色-------------------------------------'''
for i in range(len(MaxPeakList)):
    a = MaxPeakList[i]
    for j in range(a-2, a+3):
        for k in range(140):
            if 90 < imgGray1[j][k] :#/140对应这的90，130；/255对应这的50，80
                imgCopy1[j][k] = (0, 255, 0)
for i in range(len(MinPeakList)):
    a = MinPeakList[i]
    for j in range(a-2, a+3):
        for k in range(140):
            if 50 < imgGray1[j][k] < 80:#/140对应这的50，80；/255对应这的 ...忘了
                imgCopy1[j][k] = (255, 0, 255)
'''------------------------------------展示图片------------------------------------------------'''
cv2.imshow("img1", img1)
cv2.resizeWindow("img1", 300, 300)
cv2.imshow("imgbinary", imgbinary)
cv2.resizeWindow("imgbinary", 300, 300)
cv2.imshow("imgCopy1", imgCopy1)
cv2.resizeWindow("imgCopy1", 300, 300)
cv2.waitKey(0)

