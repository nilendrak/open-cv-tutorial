#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 21:30:18 2018

@author: nilendra
Description : this tutorial defines, how to detect the corners in the image
              example is tested in ubuntu, in spyder from anaconda.
"""

#import the required modules
import cv2
import numpy as np

# reading the image
img = cv2.imread("/home/nilendra/Documents/tutor.jpg",1)

# convert the image into gray image
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# convert into float32
gray = np.float32(gray)

# detect the corners using goodFeaturesToTrack function. here the parametera 
# are , inage , total number of corner to detect, quality, and distance
# between 2 detected corners 
corners = cv2.goodFeaturesToTrack(gray,50,0.01,10)

# convert into integer 64
corners = np.int64(corners)

#loop over the image and mark circle at deteted corners
for corner in corners:
    x,y = corner.ravel()
    cv2.circle(img,(x,y),3,255,-1)

# display the image
cv2.imshow("logo",img)

cv2.waitKey(0)

# distroy all the created window.
cv2.destroyAllWindows()

# this is not necessary in windows os but in ubuntu without these statements 
# it dont close the created windows.
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)