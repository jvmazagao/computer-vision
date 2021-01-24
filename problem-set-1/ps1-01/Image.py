import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


def set_callback(desc, cb):
    cv.namedWindow(desc)
    cv.setMouseCallback(desc, cb)


class Image:
    def __init__(self, image):
        self.img = image

    def show_img(self, desc):
        cv.imshow(desc, self.img)
        cv.waitKey(0)

    def on_mouse_move(self, event, x, y, flags, param):

        font = cv.FONT_HERSHEY_SIMPLEX
        if event == cv.EVENT_MOUSEMOVE:
            square_Window = self.img[(y - 5):(y + 5), (x - 5):(x + 5)]
            aux = np.zeros((140, 500, 3), np.uint8)

            aux[5:15, 5:15] = self.img[(y - 5):(y + 5), (x - 5):(x + 5)]
            cv.putText(aux, ' <--- 11x11 window:', (10, 13), font, 0.5, (255, 255, 255), 1)
            cv.putText(aux, 'The current pointer position is:', (0, 35), font, 0.5, (255, 255, 255), 1)
            cv.putText(aux, '( ' + str(x) + ' , ' + str(y) + ')', (0, 55), font, 0.5, (255, 255, 255), 1)
            cv.putText(aux, 'RGB = ' + str(np.flipud(self.img[y][x])), (0, 75), font, 0.5, (255, 255, 255), 1)
            cv.putText(aux, 'Intensity = ' + str(np.average(self.img[y][x])), (0, 95), font, 0.5, (255, 255, 255), 1)
            mean, stdDev = cv.meanStdDev(square_Window)
            mean = [m[0] for m in mean]
            stdDev = [s[0] for s in stdDev]
            cv.putText(aux, 'Window Mean = ' + str(np.flipud(np.around(mean, 2))), (0, 115), font, 0.5, (255, 255, 255),
                       1)
            cv.putText(aux, 'Window StdDvt = ' + str(np.flipud(np.around(stdDev, 2))), (0, 135), font, 0.5,
                       (255, 255, 255), 1)
            cv.imshow('Stats', aux)

    def create_histogram(self):
        color = ('b', 'g', 'r')
        for i, col in enumerate(color):
            hist = cv.calcHist([self.img], [i], None, [256], [0, 256])
            cv.normalize(hist, hist, 0, 255, cv.NORM_MINMAX)
            plt.plot(hist, color=col)
            plt.xlim([0, 256])
        plt.show()
