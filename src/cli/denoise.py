import cv2
import sys
import argparse
import math
import numpy as np

image_path = '/Volumes/Storage/Documents/hack4dk2016/_processed/0009-1.jpg'
output_dir = '/Volumes/Storage/Documents/hack4dk2016/_denoised/test.jpg'

image = cv2.imread(image_path)

# Denoising
denoised = cv2.fastNlMeansDenoising(image,50000)

# Saving the denoised image
cv2.imwrite(output_dir, denoised)

# Creating the mask to be used
height,width,depth = image.shape
mask = np.zeros((height,width), np.uint8)

inverted = 255-image
a = np.where(inverted>220)

mask[a[0],a[1]] = 255

cv2.imshow('image',mask)
cv2.waitKey(0)

# Using inpainting
dst = cv2.inpaint(denoised,mask,10,cv2.INPAINT_TELEA)
cv2.imshow('dst',dst)
cv2.waitKey(0)
