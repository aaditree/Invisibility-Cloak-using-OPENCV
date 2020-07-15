# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 21:57:04 2020

@author: Aaditree Jaisswal
"""

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
back = cv2.imread(r'C:\Users\Aaditree Jaisswal\Desktop\Guided Projects\imgs1.jpg')

while cap.isOpened():
    
    ret,frame = cap.read()
    
    if ret:
        hsv =cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
        red = np.uint8([[[0,0,255]]])
        hsv_red =cv2.cvtColor(red,cv2.COLOR_BGR2HSV)
            
        l_red = np.array([0,100, 100])
        u_red = np.array([10,255,255])
            
        mask1 = cv2.inRange(hsv,l_red , u_red)
        mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3, 3), 
                                         np.uint8), iterations = 2) 
        mask1 = cv2.dilate(mask1, np.ones((3, 3), np.uint8), iterations = 1) 
        
        part1 = cv2.bitwise_and(back, back, mask=mask1)
        mask2 = cv2.bitwise_not(mask1)
        part2 =cv2.bitwise_and(frame, frame, mask=mask2)
            
        cv2.imshow("mask" , (part1+part2))
        if cv2.waitKey(5)==ord('q'):
            break
            

            
cap.release()

cv2.destroyAllWindows()
