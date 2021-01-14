import numpy as np
import cv2 as cv

if __name__ == "__main__":
    img = np.zeros((512, 512, 3), np.uint8)
    cv.circle(img, (200, 200), 70, (0, 0, 255), -1)
    cv.circle(img, (200, 200), 35, (0, 0, 0), -1)
    poly = np.array([[200, 200], [256, 284], [154, 284]])
    poly_new = poly.reshape((-1, 1, 2))
    cv.drawContours(img, [poly_new], 0, (0, 0, 0), -1)

    cv.circle(img, (120, 350), 70, (0, 255, 0), -1)
    cv.circle(img, (120, 350), 35, (0, 0, 0), -1)
    poly = np.array([[120, 350], [154, 274], [236, 350]])
    poly_new = poly.reshape((-1, 1, 2))
    cv.drawContours(img, [poly_new], 0, (0, 0, 0), -1)

    cv.circle(img, (300, 350), 70, (255, 0, 0), -1)
    cv.circle(img, (300, 350), 35, (0, 0, 0), -1)
    poly = np.array([[300, 350], [256, 284], [356, 270]])
    poly_new = poly.reshape((-1, 1, 2))
    cv.drawContours(img, [poly_new], 0, (0, 0, 0), -1)
    while 1:
        if cv.waitKey(1) == ord('q'):
            break
        cv.imshow('Render opencv', img)
