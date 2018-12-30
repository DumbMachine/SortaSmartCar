# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 18:23:34 2018

@author: ratin
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def draw_lines(img , lines):
    try:
        for line  in lines:
            coords = line[0]
            cv2.line(img, (coords[0],coords[1]), (coords[2],coords[3])  , [255,255,255] , 3)
    except:
        pass

def roi(image , vertices):
    mask  = np.zeros_like(image)
    cv2.fillPoly(mask, vertices , 255)
    masked = cv2.bitwise_and(image,mask)
    return masked

def process(image):
    pimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    pimage = auto_canny(pimage , threshold1 = 200 , threshold2 = 300)
    vertices =np.array([[0,800],[10,500],[400,300],[620,300],[1200,800]])
    g = roi(pimage , [vertices])
    
    lines = cv2.HoughLinesP(pimage , 1 , np.pi/180 , 180 ,np.array([]), 20 ,15 )
    draw_lines(g ,lines)
    return g



cap = cv2.VideoCapture("test2.mp4")
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        image = process(frame)  
        cv2.imshow("image", image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print("[INFO] End of Video Stream")
        break
cap.release()
cv2.destroyAllWindows()

def auto_canny(image, sigma=0.01):
	# compute the median of the single channel pixel intensities
	v = np.median(image)
 
	# apply automatic Canny edge detection using the computed median
	lower = int(max(0, (1.0 - sigma) * v))
	upper = int(min(255, (1.0 + sigma) * v))
	edged = cv2.Canny(image, lower, upper)
 
	# return the edged image
	return edged



 
 
