import cv2
import numpy as np
import matplotlib.pyplot as plt

def displat_lines(image, lines):
      line_image = np.zeros_like(image)
      if lines:
            for line in lines:
                  x1,y1,x2,y2 = line
                  cv2.line(line_image , (x1,y1),(x2,y2),(255,0,0),10)
      return line_image


def roi(image):
      height = image.shape[0]
      triangle = np.array([(200,height),(1100,height),(550,250)])
      polygons = np.array(triangle)
      mask = np.zeros_like(image)
      cv2.fillPoly(mask, polygons, 255)
      masked_image = cv2.bitwise_and(canny, mask)
      return masked_image
      

def canny(image):
      nimg = np.copy(image)
      gray = cv2.cvtColor(nimg , cv2.COLOR_BGR2GRAY)
      blur = cv2.GaussianBlur(gray , (5,5), 0)
      canny = cv2.Canny(blur, 50 ,150)






image = cv2.imread("road.jpeg")
lane_image  = np.copy(image)
canny = canny(lane_image)
cropped_image = roi(canny)
lines = cv2.HoughLinesP(cropped_image , 2, np.pi/180, 100 , np.array([]), minLineLength==40 , maxLineGap=5)
line_image  = displat_lines(lane_image , lines)
combo_image = cv2.addWeighted(lane_image , 0.8 , line_image , 1)
cv2.imshow("result", line_image)
cv2.waitKey(0)