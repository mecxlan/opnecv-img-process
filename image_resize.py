
# Author: [Muhammad Arslan](https://www.linkedin.com/in/mecxlan/)

# 1. Read Image
# 2. Resize an Image
# 3. Blur Image 
# 4. Sharpen Image
# 5. Batch Process Image

# !pip install opencv-python
import cv2 as cv # for image processing
import numpy as np # for numerical processing
import sys # for command line arguments 
import os # for directory operations
import fnmatch # for pattern matching like *.jpg or *.png 

def sharpen(image):
    kernel = np.array([[0, -1, 0,], [-1, 5, -1], [0, -1, 0]]) # sharpening kernel 
    new_image = cv2.filter2D(image, -1, kernel) # applying the sharpening kernel to the input image & displaying it. -1 means destination image will have the same depth as the source. 
    cv2.imshow('Sharpened', new_image) # window title and image
    cv2.waitKey(0) # wait for any key press
    return new_image 

def blur(image):
    kernels = [3, 5, 9, 13] # different kernel sizes for blurring
    for idx, k in enumerate(kernels): # enumerate() returns an enumerate object. It contains the index and value of all the items in the list as pairs. This can be useful for iteration.
        image_bl = cv2.blur(image, ksize = (k, k)) # applying the blur filter
        cv2.imshow(str(k), image_bl) # window title and image
        cv2.waitKey(0) 
    return

def resize(fname, width, height): 
    image = cv2.imread(fname) # reading the image using OpenCV
    cv2.imshow('Original image', image) # displaying the image
    cv2.waitKey(0) 
    org_height, org_width = image.shape[0:2] # extracting height and width of the image
    print("width: ", org_width) # printing the height and width of the image
    print("height: ", org_height) # printing the height and width of the image

    if org_width >= org_height: # checking which dimension is greater
        new_image = cv2.resize(image, (width, height)) # resizing the image
    else: 
        new_image = cv2.resize(image, (height, width)) # resizing the image
        
    return fname, new_image 

listOfFiles = os.listdir('.') # list of files in the current directory
pattern = "*.jpg" # pattern to match for
n = len(sys.argv) # number of arguments passed to the script
if n == 3: # if the user has passed the width and height
    width = int(sys.argv[1]) # width
    height = int(sys.argv[2]) # height
else:
    width = 1280
    height = 960
if not os.path.exists('new_folder'): # if the output folder doesn't exist
    os.makedirs('new_folder') # create the folder

for filename in listOfFiles: # iterating over the list of files
    if fnmatch.fnmatch(filename, pattern): # checking if the file matches the pattern
        filename, new_image = resize(filename, width, height) # resizing the image
        cv2.imwrite("new_folder\\" + filename, new_image) # saving the image to the output folder

filename, new_image = resize('bird.jpg', 1280, 960) # resizing the image
#cv2.imshow('resized image', new_image) 
#cv2.waitKey(0)

# Average blurring technique # https://docs.opencv.org/master/d4/d13/tutorial_py_filtering.html

# Other usefull links for learning & practice
# https://www.geeksforgeeks.org/python-opencv-cv2-imread-method/

# blur(new_image)
# image = sharpen(new_image)
# https://docs.opencv.org/

