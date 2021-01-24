import argparse
import cv2 as cv
from Image import Image, set_callback

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Path to the image to be scanned")
    args = vars(ap.parse_args())

    img = Image(cv.imread(args["image"]))
    desc = "Image {}".format(str(args["image"]))
    set_callback(desc, img.on_mouse_move)
    while 1:
        img.show_img(desc)
        img.create_histogram()
        k = cv.waitKey(0)
        if k:
            break

    cv.destroyAllWindows()
