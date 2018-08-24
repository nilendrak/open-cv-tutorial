#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 14:21:41 2018

@author: nilendra
@Description : this example code is for doing simple arithmatic operations
               on images.where ever necessary code is commented and program
               is tested om ubuntu with anaconda spyder.
"""
# import the required libraries
import cv2
import numpy as np

# read all the images
img = cv2.imread("/home/nilendra/Documents/image2.png",cv2.IMREAD_COLOR)
img2 = cv2.imread("/home/nilendra/Documents/image1.png",cv2.IMREAD_COLOR)
img3 = cv2.imread("/home/nilendra/Documents/Opencv_logo.jpg",cv2.IMREAD_COLOR)

# simple addition of two images.
add = img + img2

# addition of images using opencv addition function
# function for image addition is g(x) = (1 - alpha) * F0(x) + alpha * F1(x)
add2 = cv2.add(img,img2)

# adding the image using weighted sum. in this addition weight need to be 
# provided with the corresponding images. the value of addition of weight 
# should be 1.
# the parameter are image1, weight1, image2, weight2 and last parameter is
# gamma for (illuminance)
waight_img = cv2.addWeighted(img,0.6,img2,0.4,0)

# getting the parameter of images.
hight,width,col = img3.shape
print(hight)
print(width)
print(col)

# picking up the region of image from image as the size of image3.
roi = img[0:hight,0:width]

# converrt image3 in gray image.
img2gray = cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY)

# creating the binary mask of gray image using thresholding.
ret,mask = cv2.threshold(img2gray,220,255,cv2.THRESH_BINARY_INV)

# creating the inverse of mask.
mask_inv = cv2.bitwise_not(mask)

# creation background image. here src1 and src2 are input array or scaler.
# mask is optional operation mask, 8-bit singel channel array ,that specifies
# elements of the output array to be changed.
img1_bg = cv2.bitwise_and(src1=roi,src2=roi,mask=mask_inv)


img2_fg = cv2.bitwise_and(img3,img3,mask=mask)

# adding 2 generated images.
dst = cv2.add(img1_bg,img2_fg)

#img[0:hight,0:width] = dst


# cv2.imshow("image1",add2)
# cv2.imshow("image2",add)
cv2.imshow("image",dst)
#cv2.imshow("image2",img2_fg)
cv2.waitKey(0)


cv2.destroyAllWindows()




cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)
