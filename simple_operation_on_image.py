#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 22:34:16 2018

@author: nilendra
@Description: This tutorial is for working some simple operations on image.
               we will try to extract and modify a singe pixal or specific 
               region of interest.
               thing to note is same thing can be done on video also, as we 
               did in writing and drawing on video tutorial.
               the file is made using syder editor on ubuntu.
"""
# importing the required library
import cv2
import numpy as np

# reading the image , an old fashioned way.
img = cv2.imread("/home/nilendra/Documents/prince.jpg",cv2.IMREAD_COLOR)

# access a individual pixal and print it
pixal = img[100,100]
print (pixal)

# change a pixal on the image and verifing by printing its value.
img[100,100] = [255,255,255]

pixal = img[100,100]
print (pixal)

# reading pixal values from a region of image.
pixel = img[100:150,100:150]
print (pixel)

# modifying a region of image.
img[150:200,200:250] = [255,255,255]

# we can access some of the properties of image as well
print (img.shape)    # read the shape of image
print (img.size)     # reading the size of image
print (img.dtype)    # reading the data type of image.

prince_face = img [30:130,110:210]
img [0:100,0:100] = prince_face

# we can modify the part or complete color of image
# 1st entry is for row, 2nd is for coloumn and 3rd is for color channel
# blue = 0
# green =1 
# red = 2
# img [:,100:150:0] = 0    # here for all rows and coloun 100:150, blue channel
# is being zero

# here for complete image green is beeing 0
img[:,:,1] = 0

# here for complete image red is being zero
#img[:,:,2] = 0

# here for complete image blue channel is being zero.
#img[:,:,0] = 0



cv2.imshow("prince_img.jpg",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.waitKey(0)
cv2.waitKey(0)
cv2.waitKey(0)
cv2.waitKey(0)


