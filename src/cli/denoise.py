import cv2
import sys
import argparse
import math
import numpy as np

image_path = '/Volumes/Storage/Documents/hack4dk2016/_processed/0002-1.jpg'
output_dir = '/Volumes/Storage/Documents/hack4dk2016/_denoised/test.jpg'

image = cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imwrite('/Volumes/Storage/Documents/hack4dk2016/_denoised/original.jpg', image)

# Denoising
denoised = cv2.fastNlMeansDenoising(image,50000)

cv2.imwrite('/Volumes/Storage/Documents/hack4dk2016/_denoised/denoised.jpg', denoised)

# Creating the mask to be used
height,width = image.shape
mask = np.zeros((height,width), np.uint8)

a = np.where(image<100)

mask[a[0],a[1]] = 255

cv2.imwrite('/Volumes/Storage/Documents/hack4dk2016/_denoised/mask.jpg', mask)

#outside = np.ma.masked_where(mask, image)
average_color = denoised.mean()
simpleAverage = image

for i in range(0,np.shape(a)[1]):
    simpleAverage[a[0][i],a[1][i]]= simpleAverage[a[0][i],a[1][i]-10]

cv2.imwrite('/Volumes/Storage/Documents/hack4dk2016/_denoised/simpleAverage.jpg', simpleAverage)

# Using inpainting
bytemask = np.asarray(mask, dtype=np.uint8)
cv2.imwrite('/Volumes/Storage/Documents/hack4dk2016/_denoised/bytemask.jpg', bytemask)

dst = cv2.inpaint(image,bytemask,inpaintRadius=10, flags=cv2.INPAINT_TELEA)

cv2.imwrite('/Volumes/Storage/Documents/hack4dk2016/_denoised/inpaint.jpg', dst)

dst2 = cv2.inpaint(dst,bytemask,inpaintRadius=10, flags=cv2.INPAINT_TELEA)

cv2.imwrite('/Volumes/Storage/Documents/hack4dk2016/_denoised/inpaint2.jpg', dst2)
