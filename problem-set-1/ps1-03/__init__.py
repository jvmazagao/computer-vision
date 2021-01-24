# python problem3.py
# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_transforms/py_fourier_transform/py_fourier_transform.html
import numpy as np
from matplotlib import pyplot as plt
import cv2 as cv

img1 = cv.imread('images/400v400-1.png', 0)
img2 = cv.imread('images/400v400-2.png', 0)


def discrete_fourier_transform(image):
    return cv.dft(np.float32(image), flags=cv.DFT_COMPLEX_OUTPUT)


# pre
def allocate_memory():
    return np.zeros((400, 400, 2))


# and angle
def create_magnitude(f_transform):
    return cv.cartToPolar(f_transform[:, :, 0], f_transform[:, :, 1])


def back_to_cartesian(p_1, p_2, modifier=1.0):
    return cv.polarToCart(p_1[:, :, 0], p_2[:, :, 1] * modifier)


def back_to_spacial_domain(phase):
    domain = cv.idft(phase)
    return cv.magnitude(domain[:, :, 0], domain[:, :, 1])


dft1 = discrete_fourier_transform(img1)
dft2 = discrete_fourier_transform(img2)

amp1Phase2 = allocate_memory()
amp2Phase1 = allocate_memory()
polar1 = allocate_memory()
polar2 = allocate_memory()

polar1[:, :, 0], polar1[:, :, 1] = create_magnitude(dft1)
polar2[:, :, 0], polar2[:, :, 1] = create_magnitude(dft2)

amp1Phase2[:, :, 0], amp1Phase2[:, :, 1] = back_to_cartesian(polar1, polar2)
amp2Phase1[:, :, 0], amp2Phase1[:, :, 1] = back_to_cartesian(polar2, polar1)


img_back1 = back_to_spacial_domain(amp1Phase2)
img_back2 = back_to_spacial_domain(amp2Phase1)

plt.subplot(221), plt.imshow(img1, cmap='gray')
plt.title('Input Image 1'), plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(img2, cmap='gray')
plt.title('Input Image 2'), plt.xticks([]), plt.yticks([])
plt.subplot(223), plt.imshow(img_back1, cmap='gray')
plt.title('Amp from 1 Phase from 2'), plt.xticks([]), plt.yticks([])
plt.subplot(224), plt.imshow(img_back2, cmap='gray')
plt.title('Amp from 2 Phase from 1'), plt.xticks([]), plt.yticks([])
plt.show()

# -------------------------------------------------------------
# Loading a uniform texture / human face
img = cv.imread('images/400v400-t-1.png', 0)

dft = discrete_fourier_transform(img)
ampModified = allocate_memory()
phaseModified = allocate_memory()
polar = allocate_memory()

polar[:, :, 0], polar[:, :, 1] = create_magnitude(dft)

ampModified[:, :, 0], ampModified[:, :, 1] = back_to_cartesian(np.log(polar), polar)
phaseModified[:, :, 0], phaseModified[:, :, 1] = back_to_cartesian(polar, polar, 1.1)

img_back3 = back_to_spacial_domain(ampModified)

img_back4 = back_to_spacial_domain(phaseModified)

plt.subplot(131), plt.imshow(img, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(img_back3, cmap='gray')
plt.title('Amp  modified'), plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(img_back4, cmap='gray')
plt.title('Phase modified'), plt.xticks([]), plt.yticks([])
plt.show()
