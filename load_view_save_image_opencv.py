#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 20:08:52 2018

@author: nilendra
"""
# import required libraries
import cv2
import numpy as np

# read the image using imread command as gray image.
img = cv2.imread('/home/nilendra/Documents/Opencv_logo.jpg',cv2.IMREAD_GRAYSCALE)

# read the image using imread command as color image.
#img = cv2.imread('/home/nilendra/Documents/Opencv_logo.jpg',cv2.IMREAD_COLOR)

# read the image using imread command as gray image as size redused by 8.
#img = cv2.imread('/home/nilendra/Documents/Opencv_logo.jpg',cv2.IMREAD_REDUCED_GRAYSCALE_8)

# show the image on image window
cv2.imshow('image',img)

# saving the newly created gray scale image
cv2.imwrite("/home/nilendra/Documents/gray_image.png",img)

# wait for key press for window exit
cv2.waitKey(0)

# distroy all the generated window
cv2.destroyAllWindows()

# this is patch. for reading image in spyder ide. otherwise
# image window will freeze.
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)