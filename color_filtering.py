#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 23:20:34 2018

@author: nilendra
@Description: 
"""
# import the required library
import numpy as np
import cv2

# create capture object to capture the camera feed.
cap = cv2.VideoCapture(0)

# checking if object is created or not.
if (cap.isOpened):
    pass
else:
    print ("failed to open")

'''
# this is one of the method to detect the hsv value. here we are trying to 
# detect the hsv of green color.
green = np.uint8([[[0,255,0 ]]])
hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
print hsv_green
'''

while(1):
    # open the feed to read
    _,frame = cap.read()
    
    # convet the bgr image to hsv
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    # lower black value
    lower_black = (0,0,0)
    # upper black value
    higher_black = (50,50,50)
    
    # creating the mask of the image in color range.
    mask = cv2.inRange(hsv,lower_black,higher_black)
    
    # bit wise and to create the fimal image.
    res = cv2.bitwise_and(frame,frame, mask=mask)
    
    # As in one-dimensional signals, images also can be filtered with various
    # low-pass filters(LPF), high-pass filters(HPF) etc. LPF helps in removing
    # noises, blurring the images etc. HPF filters helps in finding edges in
    # the images.
    
    # Operation is like this: keep this kernel above a pixel, add all the 25
    # pixels below this kernel, take its average and replace the central pixel
    # with the new average value. It continues this operation for all the
    # pixels in the image
    kernal = np.random.randn(15,15)
    
    # example kernal for edge detection
    
    kernal3 = np.array([[-1,0,1],
                       [-1,0,1],
                       [-1,0,1]])
    kernal2 = np.ones(shape=(30,30),dtype=np.float32)/255
    
    
    smoothed = cv2.filter2D(res,-1,kernal)
    smoothed1 = cv2.filter2D(res,-1,kernal2)
    smoothed2 = cv2.filter2D(frame,-1,kernal3)
    
    
    
    
    
    
    
    
    
    
    # In this, instead of box filter, gaussian kernel is used. It is done
    # with the function, cv2.GaussianBlur(). We should specify the width and
    # height of kernel which should be positive and odd. We also should
    # specify the standard deviation in X and Y direction, sigmaX and sigmaY
    # respectively. If only sigmaX is specified, sigmaY is taken as same as
    # sigmaX. If both are given as zeros, they are calculated from kernel
    # size. Gaussian blurring is highly effective in removing gaussian noise
    # from the image.
    # if the size of kernal is smaller, example (5,5) in gausian blur,than 
    # image would be that much smooth. always the weidth and hight of kernal
    # should be odd like 3,5,7 ....
    blur = cv2.GaussianBlur(res,(55,55),0)
    blur1 = cv2.GaussianBlur(res,(15,15),0)
    blur2 = cv2.GaussianBlur(res,(5,5),0)
    
    
    
    # Here, the function cv2.medianBlur() takes median of all the pixels under
    # kernel area and central element is replaced with this median value. This
    # is highly effective against salt-and-pepper noise in the images.
    # Interesting thing is that, in the above filters, central element is a
    # newly calculated value which may be a pixel value in the image or a new
    # value. But in median blurring, central element is always replaced by
    # some pixel value in the image. It reduces the noise effectively. Its
    #kernel size should be a positive odd integer.
    median = cv2.medianBlur(res,15)
    
    
    # cv2.bilateralFilter() is highly effective in noise removal while keeping
    # edges sharp. But the operation is slower compared to other filters. We
    # already saw that gaussian filter takes the a neighbourhood around the
    # pixel and find its gaussian weighted average. This gaussian filter is a
    # function of space alone, that is, nearby pixels are considered while
    # filtering. It doesn't consider whether pixels have almost same intensity.
    # It doesn't consider whether pixel is an edge pixel or not. So it blurs
    # the edges also, which we don't want to do.

    # Bilateral filter also takes a gaussian filter in space, but one more
    # gaussian filter which is a function of pixel difference. Gaussian
    # function of space make sure only nearby pixels are considered for
    # blurring while gaussian function of intensity difference make sure only
    #those pixels with similar intensity to central pixel is considered for
    # blurring. So it preserves the edges since pixels at edges will have
    #large intensity variation.
    bilateral = cv2.bilateralFilter(res,15,75,75)
    
    
    
    
    # displaying the image
    #cv2.imshow("frame",hsv)
    #cv2.imshow("mask",mask)
    #cv2.imshow("res",res)
    cv2.imshow("smoothed2",smoothed)
    cv2.imshow("smothed2",smoothed1)
    cv2.imshow("smothed3",smoothed2)
    
    #cv2.imshow("original",frame)
    #cv2.imshow("averaged",smoothed)
    #cv2.imshow("gausian_blur",blur)
    #cv2.imshow("gausian_blur1",blur1)
    #cv2.imshow("gausian_blur2",blur2)
    #cv2.imshow("median_blur",median)
    #cv2.imshow("bilateral",bilateral)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
       
    
    
# release the video capture object.
cap.release()
# relese the video saving object.
#out.release()

# distroy all the created window.
cv2.destroyAllWindows()

# this is not necessary in windows os but in ubuntu without these statements 
# it dont close the created windows.
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)
