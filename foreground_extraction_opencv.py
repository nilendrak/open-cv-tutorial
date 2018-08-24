#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 13:52:39 2018

@author: nilendra
Description: this simple example use opencv's grabcut algorithm to extract 
             the foreground from the image. the example is tested on ubutnu 
             with anaconda spyder.
"""
# import the required libarries
import cv2
import numpy as np

'''
following is the description of grabcut function we are going to use.
img = it is user defined supplied image
mask : it is mask image, where we define which areas are foreground,
        background or probable foreground/background, following are the mask.
rect : it is the rectange which incloses the foreground, format is (x,y,w,h)
bgdmodel, fgdmodel = these are the arrays used by the model internally, we 
just need to define two np.float64 type zero array of size (1,65).
iterCount : the number of iteration the algorithm should do.
mode : It should be cv2.GC_INIT_WITH_RECT or cv2.GC_INIT_WITH_MASK or combined
 which decides whether we are drawing rectangle or final touchup strokes.
'''

'''
first we are going to check the rectangle model
here the mode should be cv2.GC_INIT_WITH_RECT, because we are using rectangle 
method.we modify the mask such that all 0-pixels and 2-pixels are put to 0
 (ie background) and all 1-pixels and 3-pixels are put to 1
 (ie foreground pixels).
 '''

# read the image 
img = cv2.imread("/home/nilendra/Documents/messi.jpeg",1)
# for another image
img2 = cv2.imread("/home/nilendra/Documents/prince.jpg",1)
# create mask
mask = np.zeros(img.shape[:2],np.uint8)
mask2 = np.zeros(img2.shape[:2],np.uint8)

# background and forground model, it is (1,65 dimentional float64 array)
bgmodel = np.zeros((1,65),np.float64)
fgmodel = np.zeros((1,65),np.float64)

# create a rectange across image, which need to be extracted.
rectangle = (20,20,200,150)
rectangle2 = (50,0,280,460)

# cut the image, here we are doing 5 iteration and method is rectangle.
# here we can increse the iteration level to increse the effort to remove 
# background much better
cv2.grabCut(img,mask,rectangle,bgmodel,fgmodel,6,cv2.GC_INIT_WITH_RECT)
cv2.grabCut(img2,mask2,rectangle2,bgmodel,fgmodel,5,cv2.GC_INIT_WITH_RECT)
# create 2nd mask to make the foregroung pixel 1 and 3 to ones and 0 and 2 to
# zero.
# if you exchange 2nd and 3rd parameter than, grabed image will be black and
# background will be as it is.
#mask2 = (np.where((mask==2)| (mask==0),0,1).astype('uint8'))
mask22 = (np.where((mask2==2)| (mask2==0),0,1).astype('uint8'))
#create new image by multiplying the image by created mask2
#img  = img * mask2[:,:,np.newaxis]
img2  = img2 * mask22[:,:,np.newaxis]

# here if you observe messi hair is gone and some part of backgound also came
# in image. so we will give final touch up to pixel 1 for messi's hair and
# pixel 0 for image background.

# we can additional create a mask manually in some pait tool to remove the 
# unwanted part further, but here i am leaving that for experimentation.
 
# plot the image. 
#cv2.imshow("grabed",img)
cv2.imshow("prince",img2)
#cv2.imshow("mask",mask)
#cv2.imshow("mask2",mask2)
cv2.waitKey(0)

# distroy all the created window.
cv2.destroyAllWindows()

# this is not necessary in windows os but in ubuntu without these statements 
# it dont close the created windows.
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)
 