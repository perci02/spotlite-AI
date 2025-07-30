
import cv2

image = cv2.imread("C:/Users/Perci Mahiba/Desktop/My Folder/AI/victory.jpg")
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('original',image)
cv2.imshow('gray',grayImage)
cv2.imwrite("graycross.png",grayImage)
print(image.size)
print(image.shape)

