# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 19:16:03 2020

@author: Aaditree Jaisswal
"""

import cv2

cap = cv2.VideoCapture(0)

while cap.isOpened():
    
    ret,back =cap.read()
    
    if ret:
        
        cv2.imshow("Image",back)
        if cv2.waitKey(5)==ord('q'):
            cv2.imwrite('imgs1.jpg',back)
            break

cap.release()

cv2.destroyAllWindows()

            