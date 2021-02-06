# Problem Set 01

### 1 - Load image and display to the screen
- To run the PS1-01 we need the OpenCv environment and to execute just run
  
``` python
python3 ps1-01/__init__.py -i images/<image>.<extension> 
```

To load image and display we need to use `cv.imread` and after I choose to create a class that fill the requirements
to display the image with the configs.

Function that shows the image and expect `esc button` to close files
``` python
    def show_img(self, desc):
        cv.imshow(desc, self.img)
        cv.waitKey(0)
```

Function that define mouse event and load the stats from the image
``` python
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
```

Important parts:
1. `event == cv.EVENT_MOUSEMOVE` definition of what kind of mouse event we are using, that is the mouse movement, and 
every time that the mouse move inside the image openCV capture and do something defined by the function.
   
2. Defining square window that be used to capture the pixel. 
``` python
 square_Window = self.img[(y - 5):(y + 5), (x - 5):(x + 5)]
 aux = np.zeros((140, 500, 3), np.uint8)
```
3. Creating the mean and stdDev from a squared window using `cv.mainStdDev(square_Window)`


### 2 - Analyzing image sequences 

- To run the PS1-02 we need the OpenCv environment and to execute just run
  
``` python
python3 ps1-02/__init__.py -i images/video.mov
```
1. Auto explicative code, while some frame exists and capturing the frame, and calculating main and standard deviation
from 3 different data measures.
``` python
    frameCount = 0
    while True:
        (grabbed, frame) = video.read()
    
        period = int(1000 * 1.0 / video.get(cv.CAP_PROP_FPS))
    
        if args.get("video") and not grabbed:
            break
    
        mean, stdDev = cv.meanStdDev(frame)
    
        median_color_per_row = np.median(frame, axis=0)
        median_color = np.median(median_color_per_row, axis=0)
    
        d1[frameCount, :] = [m[0] for m in mean]
        d2[frameCount, :] = [s[0] for s in stdDev]
        d3[frameCount, :] = median_color
    
        cv.imshow("images", frame)
    
        frameCount = frameCount + 1
        if cv.waitKey(period) & 0xFF == ord("q"):
            break
```

2.  Normalizing using slides formulas 
``` python
alpha1 = (std2/std1*mean1) - mean2
beta1 = std1/std2

alpha2 = (std3/std1*mean1) - mean3
beta2 = std1/std3

newD2 = np.multiply(beta1, d2+alpha1)
newD3 = np.multiply(beta2, d3+alpha2)
```

3. Comparing using L1 metric.
``` python
distance1 = 1 / frameCount * (np.sum(aux1))
distance2 = 1 / frameCount * (np.sum(aux2))
```

### 3 - DFT

- To run the PS1-03 we need the OpenCv environment and to execute just run
  
``` python
python3 ps1-03/__init__.py
```

1. Creating the first channel, that used the real part of image, and create the second channel that is the 
imaginary part
   
``` python
    def discrete_fourier_transform(image):
        return cv.dft(np.float32(image), flags=cv.DFT_COMPLEX_OUTPUT)
```

2. Creating magnitude using dft values

``` python
    def create_magnitude(f_transform):
        return cv.cartToPolar(f_transform[:, :, 0], f_transform[:, :, 1])
```

3. Using coordinates from magnitude to back to cartesian plan
``` python 
    def back_to_cartesian(p_1, p_2, modifier=1.0):
        return cv.polarToCart(p_1[:, :, 0], p_2[:, :, 1] * modifier)
```

4. Using cartesian coordinates to back to spacial domain
``` python
    def back_to_cartesian(p_1, p_2, modifier=1.0):
        return cv.polarToCart(p_1[:, :, 0], p_2[:, :, 1] * modifier)
```

### 3 - HSI HUE

- To run the PS1-04 we need the OpenCv environment and to execute just run
  
``` python
python3 ps1-04/__init__.py -U 230
```

1. Finding the HSI values, the hue as the angle between the point and predefined value
``` python
    hue = angle_between([i - 50, (j - 50) * -1], [0, -1])
```
2. Find the normalized saturation as the norm of the point till the center
``` python
    saturation = np.linalg.norm([i - 50, (j - 50) * -1]) / 50
```
3. Fill the saturation image
``` python
    img2[i, j] = 255 * saturation
```
4.  Normalized intensity
``` python
    intensity = u / 255
```
5. Process values and wrong boundary values 
``` python 
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
```
6. If the value is a defined color (all thanks by http://fourier.eng.hmc.edu/e161/lectures/ColorProcessing/node3.html)

``` python
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
```
7. Boundary treatment
``` python
    if r > 255:
        r = 255
    if g > 255:
        g = 255
    if b > 255:
        b = 255
```
7. Fill with BGR pattern
``` python
img[i, j] = (b, g, r)
```    
