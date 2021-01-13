# Open images
This dir using cv2 to open image and open as a dialog window

## Looking the code 

    cv.imread(cv.samples.findFile('images/space.png')
function that loads the image using the file path specified, the second argument is optional and specifies the format 
in which we want the image:
- IMREAD_COLOR loads the image in the BGR 8-bit format. This is the default that is used here.
- IMREAD_UNCHANGED loads the image as is (including the alpha channel if present)
- IMREAD_GRAYSCALE loads the image as an intensity one
    

    img = cv.imread(cv.samples.findFile('images/space.png'), cv.IMREAD_GRAYSCALE)

Afterwards, a check is executed, if the image ws loaded correctly

    if img is None:
        sys.exit("Could not read the image.")

We want our window to be displayed until the user presses a key

    cv.imshow("Display window", img)
    k = cv.waitKey(0)

in the end, the image is writen to a file if the pressed key was the s-key.