#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 20:00:01 2018

@author: nilendra
Discription: This tutorial describe the morphological transformation, which is 
              basically noise reduction. the example is developed and tested
              on ububtu with anaconda spyder.
"""

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

if (cap.isOpened()):
    pass
else:
    print ("capture object didnot created")
    
while (cap.isOpened()):
    
    _,frame = cap.read()
    
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    
    
    # lower black value
    lower_black = (0,0,0)
    # upper black value
    higher_black = (50,50,50)
    
    
    # thresholding the image to get only the required color. here we are 
    # working for black color but it can be generalize for any color.
    # here basically we are taking the lower and higher range of required 
    # color and making those pixel to 255 and others are zero.
    # basically it is much easy to do in hsv color space but here i used 
    # original and gray also to compare the effectiveness. there are 100s  
    # more color space in opencv can be try.
    
    # creating mask usinf hsv image
    mask = cv2.inRange(hsv,lower_black,higher_black)
    # creatinng mask using original frame image
    mask2 = cv2.inRange(frame,lower_black,higher_black)
    
    # creation mask using gray image
    mask3 = cv2.inRange(gray,50,0)
    
    # here we are doing the experimentation using bitwise_and, bitwise_or
    # operation and diffrent combintion of images and with or without mask.
    res1 = cv2.bitwise_and(frame,frame,mask=mask)
    res2 = cv2.bitwise_or(frame,frame,mask=mask)
    res3 = cv2.bitwise_and(hsv,hsv,mask=mask)
    res4 = cv2.bitwise_or(hsv,hsv,mask=mask)
    res5 = cv2.bitwise_and(frame,hsv,mask=mask)
    res6 = cv2.bitwise_or(frame,hsv,mask=mask)
    res7 = cv2.bitwise_and(frame,frame)
    res8 = cv2.bitwise_or(frame,frame)
    res9 = cv2.bitwise_and(hsv,hsv)
    res10 = cv2.bitwise_or(hsv,hsv)
    res11 = cv2.bitwise_and(frame,hsv)
    
    
    
    # it is breaking the loop when key q is pressed.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    # if loop is experimental to find out the diffent combination of result
    # feel free to change the value of print_val to check for diffrent 
    # combination
    
    
    # here we are goint to talk about erosion and dilution operation
    # these work with a slider kernal. we give a slider a size for example
    # ( 5 X 5 ), we slide the slider around the image and if all the pixels
    # are white then we got white for erosion,otherwise black.
    # the other version of this is dilusion, which does the oposite. if the
    # entire area is not black then it is converted to white.
    
    # creating the kernal
    kernal = np.ones((3,3),dtype = np.uint8)
    
    # the parameters are input image, kernal = structuring element used for 
    # erosion and dilation, iteration = number of time kernal applied on image.
    erosion = cv2.erode(mask,kernal,iterations=1)
    dilation = cv2.dilate(mask,kernal,iterations=1)
    
    
    # The next pair is "opening" and "closing." The goal with opening is to
    # remove "false positives" so to speak. Sometimes, in the background, you
    # get some pixels here and there of "noise." The idea of "closing" is to
    # remove false negatives. Basically this is where you have your detected
    # shape, like our hat, and yet you still have some black pixels within the
    # object. Closing will attempt to clear that up.
    opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernal)
    closing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernal)
    
    
    # there are other options like tophat and blackhat. feel free to do the 
    # experimentation
    
    
    print_val = 8
    if (print_val == 0):
        cv2.imshow("mask_of_gray",mask3)
        cv2.imshow("mask_of_hsv",mask)
        cv2.imshow("mask_of_frame",mask2)
        
    elif (print_val == 1):
        cv2.imshow("bitwise_and_frame",res1)
        cv2.imshow("bitwise_or_frame",res2)
        
    elif (print_val == 2):
        cv2.imshow("bitwise_and_hsv",res3)
        cv2.imshow("bitwise_or_hsv",res4)
    
    elif (print_val == 3):
        cv2.imshow("bitwise_and_frame_hsv",res5)
        cv2.imshow("bitwise_or_frame_hsv",res6)
        
    elif (print_val == 4):
        cv2.imshow("bitwise_and_frame_without_mask",res7)
        cv2.imshow("bitwise_or_frame_without_mask",res8)
        
    elif (print_val == 5):
        cv2.imshow("bitwise_and_hsv_without_mask",res9)
        cv2.imshow("bitwise_or_hsv_without_mask",res10)
        
    elif (print_val == 6):
        cv2.imshow("bitwise_and_frame_hsv_without_mask",res11)
        
    elif (print_val == 7):
        cv2.imshow("masked",mask)
        cv2.imshow("erosition",erosion)
        cv2.imshow("dilation",dilation)
        
    elif (print_val == 8):
        cv2.imshow("opening",opening)
        cv2.imshow("closing",closing)
        
        
    else:    
        pass
    
    
    
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