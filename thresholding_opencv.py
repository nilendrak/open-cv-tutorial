#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 18:27:24 2018

@author: nilendra
@Description : 
"""
import cv2
import numpy as np

def thresholding (type):
    '''
    this function is implemented to chose a specific type of thresholding 
    # followinf is the description of threshold function
    # first argument is image source, which sould be grayscale image
    # 2nd argument is threshold value, which use to classify the pixel.
    # 3rd argument is pixal value which would be given to the pixel if it is 
    # greater than threshold value.
    #fourth is diffrent style of thresholding. possible values are cv2.THRESH_BINARY,
    # cv2.THRESH_MASK , cv2.THRESH_BINARY_INV, cv2.THRUSH_TRUNC, cv2.THRUSH_TOZERO,
    # etc.
    '''
    if (type == 0):
        retval,threshold = cv2.threshold(grayscale,10,255,cv2.THRESH_BINARY)
    elif (type == 1):
        retval,threshold = cv2.threshold(grayscale,10,255,cv2.THRESH_BINARY_INV)
        
    elif (type == 2):
        retval,threshold = cv2.threshold(grayscale,10,255,cv2.THRESH_TRUNC)
        
    elif (type == 3):   
        retval,threshold = cv2.threshold(grayscale,10,255,cv2.THRESH_TOZERO)
    else:
        retval,threshold = cv2.threshold(grayscale,10,255,cv2.THRESH_TOZERO_INV)
        
    return threshold
        

img = cv2.imread("/home/nilendra/Documents/bpage.jpg")

#for better result convert image into grayscale
grayscale = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


#retval,threshold = cv2.threshold(grayscale,10,255,cv2.THRESH_BINARY)
thres = thresholding(1)




# there is one more thresholding called adaptive tresholding
# In this, the algorithm calculate the threshold for a small regions of the
# image. So we get different thresholds for different regions of the same
# image and it gives us better results for images with varying illumination.

#cv.ADAPTIVE_THRESH_MEAN_C : threshold value is the mean of neighbourhood area.
 
#cv.ADAPTIVE_THRESH_GAUSSIAN_C : threshold value is the weighted sum of 
#      neighbourhood values where weights are a gaussian window.
# block size decides the size of neighbourhood area.
# next argument is just a constant which is substracted from from the mean of 
# weighted mean calculated
thr = cv2.adaptiveThreshold(grayscale,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                            cv2.THRESH_BINARY,115,1)

'''
there is one more varity of thresholding is Otsu's thresholding.
the details of this algorithm is avilable in opencv documentation.
'''



cv2.imshow("bookimage",thres)
cv2.imshow("bookimage2",thr)
cv2.waitKey(0)

# distroy all the created window.
cv2.destroyAllWindows()

# this is not necessary in windows os but in ubuntu without these statements 
# it dont close the created windows.
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)
#cv2.waitKey(1)
