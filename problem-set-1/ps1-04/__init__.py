# python problem4.py --u 230
# http://fourier.eng.hmc.edu/e161/lectures/ColorProcessing/node3.html
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-u", "--u", type=int, required=True,
                help="Value of U between 0 and 255")
args = vars(ap.parse_args())


def angle_between(p1, p2):
    ang1 = np.arctan2(*p1[::-1])
    ang2 = np.arctan2(*p2[::-1])
    return (ang1 - ang2) % (2 * np.pi)


u = args["u"]

if u > 255:
    u = 255
elif u < 0:
    u = 0

img = np.zeros((101, 101, 3))
pi = np.pi
img2 = np.zeros((101, 101))

# For each pixel in our image
for i in range(0, 101):
    for j in range(0, 101):

        # Finding the HSI values
        # Find the hue as the angle between the point and predefined value
        hue = angle_between([i - 50, (j - 50) * -1], [0, -1])

        # Find the normalized saturation as the norm of the point till the center
        saturation = np.linalg.norm([i - 50, (j - 50) * -1]) / 50

        # Fill the saturation image
        img2[i, j] = 255 * saturation

        # Normalized intensity
        intensity = u / 255

        # Default instantiation
        r = 0
        g = 0
        b = 0

        # If the intensity out of bounds
        if intensity > 1:
            intensity = 1
        # If grayscale
        if saturation == 0:
            r = g = b = u
        # out of bounds
        elif saturation > 1:
            # make RGB (0,0,0)
            r = g = b = 0
            # Bound the saturation back
            saturation = 1
            # Apply mask
            img2[i, j] = 0
        # If represents a color
        else:
            # If it is within the first 120 degrees
            if hue < 2 * pi / 3:
                b = (1 - saturation) / 3
                r = (1 + (saturation * np.cos(hue) / np.cos(pi / 3 - hue))) / 3
                g = 1 - r - b
            # If it is between 120 and 240
            elif hue < 4 * pi / 3:
                hue = hue - (2 * pi) / 3
                r = (1 - saturation) / 3
                g = (1 + (saturation * np.cos(hue) / np.cos(pi / 3 - hue))) / 3
                b = 1 - r - g
            # If it is between 240 and 360
            else:
                hue = hue - (4 * pi) / 3
                g = (1 - saturation) / 3
                b = (1 + (saturation * np.cos(hue) / np.cos(pi / 3 - hue))) / 3
                r = 1 - b - g

            r = 3 * intensity * r * 255
            g = 3 * intensity * g * 255
            b = 3 * intensity * b * 255

            # Treatment of ut of bounds
            if r > 255:
                r = 255
            if g > 255:
                g = 255
            if b > 255:
                b = 255
        # Fill with BGR pattern
        img[i, j] = (b, g, r)

# Show image after transform to standard
cv2.imshow('HSI circle', img.astype(np.uint8))
cv2.imshow('Saturation', img2.astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()
