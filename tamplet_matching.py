#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 22:28:25 2018

@author: nilendra
Description : This is basic object detection. here we are taking a sample
              and templet is the object of the image. This work good where 
              the tamplet match exactly in the image, for example button, in
              computer GUI.
"""
#import important packages
import cv2
import numpy as np

# read image.
img = cv2.imread("/home/nilendra/Documents/main_image.jpg")

# convert the image into gray image
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# read  the templete whech need to mach in the original image.
template = cv2.imread("/home/nilendra/Documents/tamplet_image.jpg",0)

# extract weidth and height of the tamplete to dtraw in the original image.
w,h = template.shape[::-1]

#print(w)
#print(h)
'''
templete maching is a simple  2d convolution method. It simply slides the
 template image over the input image (as in 2D convolution) and compares the
 template and patch of input image under the template image. Several
 comparison methods are implemented in OpenCV. (You can check docs for more
 details). It returns a grayscale image, where each pixel denotes how much
 does the neighbourhood of that pixel match with template.
 following six method can be applied for tamplet matching
 'cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED'
'''

res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)

# creating a threshold value to select max number of images.
threshold = 0.7

# only draw at those locations where the value of 2d convolution with image 
# is more than threhold value.
loc = np.where(res >= threshold)

# draw ractangle in main image on all the matching locations.
for pt in zip(*loc[::-1]):
    cv2.rectangle(img,pt,(pt[0] + w,pt[1] + h),(0,255,255),2)
    


#cv2.imshow("original image",img)
#cv2.imshow("gray image",img_gray)
#cv2.imshow("tamplet",template)
#cv2.imshow("res",res)
cv2.imshow("detected",img)
cv2.waitKey(0)

# distroy all the created window.
cv2.destroyAllWindows()

# this is not necessary in windows os but in ubuntu without these statements 
# it dont close the created windows.
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)
