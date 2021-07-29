import cv2
import numpy as np
'''----------------------------------算法----------------------------------'''
def thresholdFunction(img):
    imgGray1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # print("imgGray1", imgGray1.shape)
    '''------------------------------------阈值分割------------------------------------------------'''
    ret, imgBinary = cv2.threshold(imgGray1, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)  # (src,阈值,最大值,阈值类型)
    x, y = imgBinary.shape  # x行y列
    '''-----------------------画中膜的上边的外膜的下边(进行上下对称处理)-------------------------------------'''
    for j in range(y):
        count = 0
        for i in range(int(x / 2), x):
            if i == x - 2:
                count = 0
                break
            if int(imgBinary[i + 1][j]) - int(imgBinary[i][j]) == 255:
                count += 1
                if count == 2:
                    img[i][j] = (0, 255, 0)
                    img[a][j] = (0, 255, 0)
                a = i
    return img

cap = cv2.VideoCapture("C:/Users/lenovo/Desktop/wgz/carotid/20210721000809789.mp4")
'''----------------------------------定义鼠标动作用来选框---------------------------------'''
drawing = False
point = (0, 0)
mode = False
tangleSize = 71
a1, b1, a2, b2 = 99, 99, 200, 200
def mouse_drawing(event, x, y, flags, params):
    global a1, b1, a2, b2, drawing, mode
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        mode = True
        a2, b2 = x, y
        cv2.rectangle(img, (a2-tangleSize, b2-tangleSize), (a2+tangleSize, b2+tangleSize), (0, 255, 0), -1)
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing is True:
            if mode == True:
                a2, b2 = x, y
                cv2.rectangle(img, (a2-tangleSize, b2-tangleSize), (a2+tangleSize, b2+tangleSize), (0, 255, 0), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        a2, b2 = x, y
        cv2.rectangle(img, (a2-tangleSize, b2-tangleSize), (a2+tangleSize, b2+tangleSize), (0, 255, 0), -1)


cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame", mouse_drawing)
count, count1 = 0, 0
while(True):
    success, img = cap.read()
    cv2.rectangle(img, (a2 - tangleSize, b2 - tangleSize), (a2 + tangleSize, b2 + tangleSize), (0, 0, 255), 0)
    img1 = img[b2 - (tangleSize - 1): b2 + (tangleSize - 1), a2 - (tangleSize - 1):a2 + (tangleSize - 1)].copy()
    img1 = thresholdFunction(img1)
    # print((a2-80, b2-80), (a2+80, b2+80))
    count += 1
    if count == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        print(count)
        count = 0
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    cv2.imshow("Frame", img)
    cv2.imshow("Frame1", img1)
    if cv2.waitKey(5) & 0xFF == ord(' '):
        break


