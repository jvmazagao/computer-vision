import numpy as np
import cv2 as cv

img = cv.imread('images/messi-5.jpeg')
px = img[100, 100]
print(px)

blue = img[100, 100, 0]
print(blue)
img[100, 100] = [255, 255, 255]
print(img[100, 100])

# Warning
#
# Numpy is an optimized library for fast array calculations. So simply accessing each and every pixel value and
# modifying it will be very slow and it is discouraged.
#
# Note The above method is normally used for selecting a region of an array, say the first 5 rows and last 3 columns.
# For individual pixel access, the Numpy array methods, array.item() and array.itemset() are considered better. They
# always return a scalar, however, so if you want to access all the B,G,R values, you will need to call array.item()
# separately for each value. Better pixel accessing and editing method :

print(img.item(10, 10, 2))
img.itemset((10, 10, 2), 100)
print(img.item(10, 10, 2))

print("Print image properties")
print(img.shape)
print(img.size)
print(img.dtype)

ball = img[135:170, 12:52]
img[47:82, 0:40] = ball

while 1:
    cv.imshow('image', img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()
