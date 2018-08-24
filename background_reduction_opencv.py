#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 21:49:32 2018

@author: nilendra
@ Description: 
"""
import cv2


'''
Background subtraction is a major preprocessing steps in many vision based
applications. For example, consider the cases like visitor counter where a
static camera takes the number of visitors entering or leaving the room, or a
traffic camera extracting information about the vehicles etc. In all these
cases, first you need to extract the person or vehicles alone. Technically,
you need to extract the moving foreground from static background.

If you have an image of background alone, like image of the room without
visitors, image of the road without vehicles etc, it is an easy job. Just
 subtract the new image from the background. You get the foreground objects
 alone. But in most of the cases, you may not have such an image, so we need
 to extract the background from whatever images we have. It become more
 complicated when there is shadow of the vehicles. Since shadow is also moving,
 simple subtraction will mark that also as foreground. It complicates things.
there are 3 algoritm in opencv for this.
1 : createBackgroundSubtractorMOG()
It is a Gaussian Mixture-based Background/Foreground Segmentation Algorithm.
It uses a method to model each background pixel by a mixture of K Gaussian
 distributions (K = 3 to 5). The weights of the mixture represent the time
 proportions that those colours stay in the scene. The probable background
 colours are the ones which stay longer and more static
 
2 : cv2.createBackgroundSubtractorMOG2()
It is also a Gaussian Mixture-based Background/Foreground Segmentation
 Algorithm.
 One important feature of this algorithm is that it selects the appropriate
 number of gaussian distribution for each pixel. (Remember, in last case,
 we took a K gaussian distributions throughout the algorithm). It provides
 better adaptibility to varying scenes due illumination changes etc.

3: BackgroundSubstracterGMG
This algorithm combines statistical background image estimation and per-pixel
 Bayesian segmentation
 It uses first few (120 by default) frames for background modelling.
 It employs probabilistic foreground segmentation algorithm that identifies
 possible foreground objects using Bayesian inference. The estimates are
 adaptive; newer observations are more heavily weighted than old observations
 to accommodate variable illumination. Several morphological filtering
 operations like closing and opening are done to remove unwanted noise.
 You will get a black window during first few frames.

It would be better to apply morphological opening to the result to remove the
 noises. 
'''


# this fiunction will create a capture object for primary camera
capture = cv2.VideoCapture(0)

# create background substracter object
fgbg = cv2.createBackgroundSubtractorMOG2()
#fgbg = cv2.createBackgroundSubtractorKNN()


# if object is created than pass otherwise generate an error message
if (capture.isOpened()):
    pass
else:
    print ("fail to open")
    


# going to loop if video capture object is open
while (capture.isOpened()):
    
    # it will read the video feed in infinite loop, which will later break in
    # if condition
    ret,frame = capture.read()
    
    # apply mask on detected motion foreground.
    fgmask = fgbg.apply(frame)
    
   
    
    # display the video, here we can display the "frame " video also or both,
    # gray and frame by writing 2 imshow statement.
    cv2.imshow("original",frame)
    cv2.imshow("detected",fgmask)
    
    # waitkey is for waiting for the time in bitween the image frames. in casd
    # of image we provide "0" because we need to wait indefnite amount of time
    # but in case of video small time is okay to provide. basically it depends
    # on application. here i am using 1ms. if "Q" is pressed than break the loop
    # means stop playing and saving video.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release the video capture object.
capture.release()

# distroy all the created window.
cv2.destroyAllWindows()

# this is not necessary in windows os but in ubuntu without these statements 
# it dont close the created windows.
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)
#cv2.waitKey(1)