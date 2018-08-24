#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 15:57:19 2018

@author: nilendra
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 23:02:40 2018

@author: nilendra
@Description : loading, view and save video in opencv is not much diffrent
               than images. other than initial few lines of code, mostly it is
               same. here we will read the video feed from primary camera
               .in my case it will be video from my webcam and will store it.
               this program is tested on ubuntu
"""

# importing the required library
import cv2



# this fiunction will create a capture object for primary camera
capture = cv2.VideoCapture("/home/nilendra/Documents/small.avi")

# if object is created than pass otherwise generate an error message
if (capture.isOpened()):
    pass
else:
    print ("fail to open")
    
# creating codec information to write camera video file. this codec will 
#work on ubuntu. i found it after so many trail and error ahhhhhhhh
forcecc = cv2.VideoWriter_fourcc(*'MJPG')

# here we are creating a video writer object to save the video file later.
# 1st argument is file name with path, 2nd is codec information, last argument
# is video size. it is good idea to save a camera video in it same size and
# later alter it, otherwise some time it will create save file and dont show 
# any error also
out = cv2.VideoWriter('/home/nilendra/Documents/small2.avi',
                     forcecc,20.0, (int(capture.get(3)), int(capture.get(4))))

# going to loop if video capture object is open
while (capture.isOpened()):
    
    # it will read the video feed in infinite loop, which will later break in
    # if condition
    ret,frame = capture.read()
    
    # cvtColor function is for changing the video, to rgb ycbcr or lab or gray.
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2Lab)
    
    #saving the video frame in  disk, we can save gray also.
    out.write(frame)
    
    # display the video, here we can display the "frame " video also or both,
    # gray and frame by writing 2 imshow statement.
    cv2.imshow("frame2",gray)
    
    # waitkey is for waiting for the time in bitween the image frames. in casd
    # of image we provide "0" because we need to wait indefnite amount of time
    # but in case of video small time is okay to provide. basically it depends
    # on application. here i am using 1ms. if "Q" is pressed than break the loop
    # means stop playing and saving video.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release the video capture object.
capture.release()
# relese the video saving object.
out.release()

# distroy all the created window.
cv2.destroyAllWindows()

# this is not necessary in windows os but in ubuntu without these statements 
# it dont close the created windows.
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)
#cv2.waitKey(1)
