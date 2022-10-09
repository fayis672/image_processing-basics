import cv2

#function to convert to negative image
def negative(img):
    return 255-img
#function to convert to negative image using open cv
def negative_using_openCV(img):
    return cv2.bitwise_not(img)