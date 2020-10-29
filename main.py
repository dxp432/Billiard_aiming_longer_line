import cv2
import numpy as np
import time
import numpy as np
from PIL import ImageGrab
from win32con import NULL
from auto import *


while True:
    # time.sleep(1)
    computer_prtsc('Screencap.png')
    if computer_if_matchImg('Screencap.png', 'oo.png'):
    # if 1 == 1:
        print('继续播放')
        # computer_matchImgClick('Screencap.png', 'oo.png')
        myx, myy = computer_matchImg_return_x_y('Screencap.png', 'oo.png')
        print(myx, myy)
        # myx, myy = 429.0, 562.0
         # time.sleep(0.2)
        img_full = ImageGrab.grab(bbox=(0, 0, 1920, 1080)) 
        img_full = np.array(img_full.getdata(), np.uint8).reshape(img_full.size[1], img_full.size[0], 3)
        img = ImageGrab.grab(bbox=(float(myx) - 110.0, float(myy) - 110.0, float(myx) + 110.0, float(myy) + 110.0))
        img = np.array(img.getdata(), np.uint8).reshape(img.size[1], img.size[0], 3)

        # img = cv2.imread('pr4.jpg')
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        edges = cv2.Canny(gray,100,200,apertureSize = 3)
        # cv2.imshow('edges',edges)
        # cv2.waitKey(0)

        # 表示能组成一条直线的最少点的数量，点数量不足的直线将被抛弃
        # minLineLength = 57
        # 表示能被认为在一条直线上的亮点的最大距离。
        # maxLineGap = 2
        with open("minLineLength.txt", "r") as f:
            data = f.readline()
            print(data)
        minLineLength = int(data)
        maxLineGap = 1
        lines = cv2.HoughLinesP(edges,1,np.pi/180,15,minLineLength=minLineLength,maxLineGap=maxLineGap)
        if lines is None:
            print('没有找到直线--------------------')
        else:
            for x in range(0, len(lines)):
                for x1,y1,x2,y2 in lines[x]:
                    # 根据两点算出斜率，把线段延长成直线
                    p1 = (x1, y1)
                    p2 = (x2, y2)

                    theta = np.arctan2(p1[1]-p2[1], p1[0]-p2[0])
                    endpt_x = int(p1[0] - 1000*np.cos(theta))
                    endpt_y = int(p1[1] - 1000*np.sin(theta))

                    start_x = int(p1[0] + 1000*np.cos(theta)) 
                    start_y = int(p1[1] + 1000*np.sin(theta))

                    # img = np.zeros_like(img)

                    cv2.line(img_full, 
                    (start_x + int(float(myx)) - 110, start_y + int(float(myy)) - 110), 
                    (endpt_x + int(float(myx)) - 110, endpt_y + int(float(myy)) - 110), 
                    (0,255,0),
                    2)
                    # cv2.line(img, (start_x,start_y), (endpt_x, endpt_y), (0,255,0),2)
                    # cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
    # 
            filepath="1.png"
            cv2.imwrite(filepath, img)
            filepath="11.png"
            cv2.imwrite(filepath, img_full)
    else:
        print('no')



while True:
    # time.sleep(0.2)
    img = ImageGrab.grab(bbox=(280, 404, 1305, 925))
    img = np.array(img.getdata(), np.uint8).reshape(img.size[1], img.size[0], 3)

    # img = cv2.imread('pr4.jpg')
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray,100,200,apertureSize = 3)
    # cv2.imshow('edges',edges)
    # cv2.waitKey(0)

    # 表示能组成一条直线的最少点的数量，点数量不足的直线将被抛弃
    # minLineLength = 57
    # 表示能被认为在一条直线上的亮点的最大距离。
    # maxLineGap = 2
    with open("minLineLength.txt", "r") as f:
        data = f.readline()
        print(data)
    minLineLength = int(data)
    maxLineGap = 2
    lines = cv2.HoughLinesP(edges,1,np.pi/180,15,minLineLength=minLineLength,maxLineGap=maxLineGap)
    for x in range(0, len(lines)):
        for x1,y1,x2,y2 in lines[x]:
            # 根据两点算出斜率，把线段延长成直线
            p1 = (x1, y1)
            p2 = (x2, y2)

            theta = np.arctan2(p1[1]-p2[1], p1[0]-p2[0])
            endpt_x = int(p1[0] - 1000*np.cos(theta))
            endpt_y = int(p1[1] - 1000*np.sin(theta))

            start_x = int(p1[0] + 1000*np.cos(theta)) 
            start_y = int(p1[1] + 1000*np.sin(theta))

            # img = np.zeros_like(img)
            cv2.line(img, (start_x,start_y), (endpt_x, endpt_y), (0,255,0),2)
            # cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

    filepath="1.png"

    cv2.imwrite(filepath, img)
    # cv2.imshow('hough',img)
    # cv2.waitKey(0)






# #coding=utf-8
# import cv2
# import numpy as np  
 
# img = cv2.imread("pr1.jpg", 0)
 
# img = cv2.GaussianBlur(img,(3,3),0)
# edges = cv2.Canny(img, 50, 300, apertureSize = 3)
# lines = cv2.HoughLines(edges,0.9,np.pi/80,118) #这里对最后一个参数使用了经验型的值
# result = img.copy()
# for line in lines[0]:
# 	rho = line[0] #第一个元素是距离rho
# 	theta= line[1] #第二个元素是角度theta
# 	print(rho)
# 	print(theta)
# 	if  (theta < (np.pi/4. )) or (theta > (3.*np.pi/4.0)): #垂直直线
#                 #该直线与第一行的交点
# 		pt1 = (int(rho/np.cos(theta)),0)
# 		#该直线与最后一行的焦点
# 		pt2 = (int((rho-result.shape[0]*np.sin(theta))/np.cos(theta)),result.shape[0])
# 		#绘制一条白线
# 		cv2.line( result, pt1, pt2, (255))
# 	else: #水平直线
# 		# 该直线与第一列的交点
# 		pt1 = (0,int(rho/np.sin(theta)))
# 		#该直线与最后一列的交点
# 		pt2 = (result.shape[1], int((rho-result.shape[1]*np.cos(theta))/np.sin(theta)))
# 		#绘制一条直线
# 		cv2.line(result, pt1, pt2, (255), 1)
 
# cv2.imshow('Canny', edges )
# cv2.imshow('Result', result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()




# #coding=utf-8
# import cv2
# import numpy as np  
 
# img = cv2.imread("pr.jpg")
 
# img = cv2.GaussianBlur(img,(3,3),0)
# edges = cv2.Canny(img, 50, 150, apertureSize = 3)
# lines = cv2.HoughLines(edges,1,np.pi/180,118)
# result = img.copy()
 
# #经验参数
# minLineLength = 200
# maxLineGap = 15
# lines = cv2.HoughLinesP(edges,1,np.pi/180,80,minLineLength,maxLineGap)
# for x1,y1,x2,y2 in lines[0]:
# 	cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
 
# cv2.imshow('Result', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

