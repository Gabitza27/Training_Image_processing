import cv2
import os
import requests
from PIL import Image
from matplotlib import pyplot as plt

import matplotlib.pyplot as plt #interfata pentru afisare de imagini
import matplotlib.image as mpimg #incarcare de imagini
import numpy as np # pentru lucrul cu arrays

from IPython.display import set_matplotlib_formats
set_matplotlib_formats('png', 'jpg')
import csv
###############################################################


#read a image from your computer
image_path = "D:\\Licenta 2018-2019\\Boch future mobility\\autobahn-wiki.jpg"
img = cv2.imread(image_path,0)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # converts from BGR to RGB
cv2.imshow('STREET', img)
cv2.waitKey(0)



imageDir = "D:\\GIT\\Training_image_procesing\\tests image\\"
imageFiles = os.listdir(imageDir)
imageList = [] #this list will contain all the test images
for i in range(0, len(imageFiles)):
    imageList.append(mpimg.imread(imageDir+ imageFiles[i]))

def display_images(images, cmap=None):
    plt.figure(figsize=(40,40))
    for i, image in enumerate(images):
        plt.subplot(3,2,i+1)
        plt.imshow(image, cmap)
        plt.autoscale(tight=True)
    plt.show()

display_images(imageList)