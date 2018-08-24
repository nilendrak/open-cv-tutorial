#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 15:58:57 2018

@author: nilendra
@Description : This file is small tutorial on how to write and draw common 
               symbols and shape on image using opencv.
"""
# import the required library
import numpy as np
import cv2

# reading an image
img = cv2.imread("test_image.png",cv2.IMREAD_COLOR)

'''
img = image to be display
pt1 = point 1
pt2 = point 2
color = color of particular of shape
thickness = thickness of line
tiplength = length of tip of arrow
text = text to write in the specified image
fontFace = diffrent type of text fonts
fontscale = scale need to be multiply with each alphabet
linetype = line type of font

there are so many diffrent type of attribute ex (cv2.LINE_AA) is prsent which
can be explored as needed
also there are othere shapes and drawing elements are there which can be
find in opencv documentation
----------cv2.polylines can be used to draw a shape of own
'''

# drawing line
cv2.line(img=img,pt1=(50,0),pt2=(100,100),color=(255,255,255),thickness=10)

# drawing a ractangle
cv2.rectangle(img=img,pt1=(0,0),pt2=(50,50),color=(100,100,100),thickness=10)

# drawing a circle
cv2.circle(img=img,center=(100,100),radius=50,color=(100,100,100),thickness=1)

# drawing arroed line
cv2.arrowedLine(img=img,pt1=(100,100),pt2=(200,200),
                color=(200,200,200),thickness=2,tipLength=.1)

# draw marker on the image
cv2.drawMarker(img=img,position=(100,200),color=(200,200,200),thickness=5)

# font to write on the image, explore othere fonts for fun S
font=cv2.FONT_HERSHEY_COMPLEX_SMALL

# writing on the image
cv2.putText(img=img,text="here i am",org =(0,150),fontFace=font,fontScale=1,
            color=(255,255,255),thickness=2,lineType=cv2.LINE_AA)


# display the image 
cv2.imshow("image",img)

# saving the newly created image
cv2.imwrite("/home/nilendra/Documents/draw_image.png",img)

# wait for infinite time
cv2.waitKey(0)

# kill all the windows
cv2.destroyAllWindows()

# ahhhh, this is small patch for work in ubuntu
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)