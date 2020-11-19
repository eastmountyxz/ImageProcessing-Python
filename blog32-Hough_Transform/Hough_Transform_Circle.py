import cv2
import numpy as np

img=cv2.imread("circles.png")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #convert to grayscale

blurr=cv2.blur(gray,(3,3)) #blur the image to reduce noice

detected_circles=cv2.HoughCircles(blurr,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=100)

circles = np.uint16(np.around(detected_circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow('detected circles',img)
cv2.imwrite("Circle detected.png",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
