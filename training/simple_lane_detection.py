import cv2
import os
import requests
import PIL
from PIL import Image


import matplotlib.pyplot as plt #interfata pentru afisare de imagini
import matplotlib.image as mpimg #incarcare de imagini

import numpy as np # pentru lucrul cu arrays
import csv


#from matplotlib import pylab, mlab
###############################################################


#read a image from your computer
image_path = "D:\\Licenta 2018-2019\\Boch future mobility\\autobahn-wiki.jpg"
img = cv2.imread(image_path,0)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # converts from BGR to RGB
cv2.imshow('STREET', img)
cv2.waitKey(0)
from IPython.display import set_matplotlib_formats
set_matplotlib_formats('png', 'jpg')


imageDir = "D:\\GIT\\Training_image_procesing\\tests image"
imageFiles = os.listdir(imageDir)
imageList = [] #this list will contain all the test images

for i in range(0, len(imageFiles)):
    imageList.append(mpimg.imread(imageDir + "\\" + imageFiles[i]))

def display_images(images, cmap=None):
    plt.figure(figsize=(40,40))
    for i, image in enumerate(images):
        plt.subplot(3,2,i+1)
        plt.imshow(image, cmap)
        plt.autoscale(tight=True)
    plt.show()

display_images(imageList)

hls = cv2.cvtColor(image, cv2.COLOR_RGB2HLS)
def color_filter(image):
    #convert to HLS to mask based on HLS
    hls = cv2.cvtColor(image, cv2.COLOR_RGB2HLS)
    lower = np.array([0,190,0])
    upper = np.array([255,255,255])
    yellower = np.array([10,0,90])
    yelupper = np.array([50,255,255])
    yellowmask = cv2.inRange(hls, yellower, yelupper)
    whitemask = cv2.inRange(hls, lower, upper)
    mask = cv2.bitwise_or(yellowmask, whitemask)
    masked = cv2.bitwise_and(image, image, mask = mask)
    return masked
filtered_img = list(map(color_filter, imageList))
display_images(filtered_img)