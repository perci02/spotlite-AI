

import cv2

img = cv2.imread( "cross.png")    #read an image
cv2.imshow('Show',img)          #display image
cv2.imwrite("victory.jpg",img)   #to save image 
cv2.waitKey(10000)
cv2.destroyAllWindows()
