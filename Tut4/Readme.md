# Numpy
* Numpy is a library specifically for multi-dimentional arrays
* Import the following:`import os`, `import pandag`, `import numpy`

## OpenCV
* to install openCV: `sudo pip3 install opencv-python`
* import it with: `import os`, `import pandas`, `import numpy`, `import cv2`
* to import image: `image = cv2.imread("smallgray.png",0)` with 0 = gray, 1 = color
* `image_list = [[0, 255, 0, 255, 0],[0, 125, 255, 255, 0],[255, 134, 255,  97, 0]]`
* to change a list to an array: `image_array = numpy.asarray(image_list)`
* to make a new image using the array: `cv2.imwrite("newimage.png", image_array)`
* to select various items use: `image[0:2]` or `image[:, 2:4]` or `image[2]`
* to iterate through an array: `for i in image: print(i)`
* to iterate through all the array numbers one by one: `for i in image.flat: print(i)`
* to concatonate arrays: `concatImage = numpy.hstack((image1, image2))` or `concatImage = numpy.vstack((image1, image2))`
* to split arrays horisontally: `splitArr = numpy.hsplit(concatImage,5)`, with the number 5 being the amount of new arrays.
* to split arrays vertically: `splitArr = numpy.vsplit(concatImage,2)`
