import cv2
import sys
import math

# Get user supplied values
imagePath = sys.argv[1]
cascPath = sys.argv[2]

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
)

print "Found {0} faces!".format(len(faces))

# Finding only the faces closest to the center
img_x0, img_y0, channels = image.shape
dist_min = 1000
for (x, y, w, h) in faces:
    dist = math.sqrt( (x-img_x0)^2+(y-img_y0)^2)
    if dist<dist_min:
        dist_min = dist
        y_min = y

# Looping over the faces
nameInt = 0
y_top_margin = 40
y_bottom_margin = 15
for (x, y, w, h) in faces:
    # Writing code that take the centermost rectangles
    dist = math.sqrt( (x-img_x0)^2+(y-img_y0)^2 )
    if (y>y_min-y_top_margin) and (y<y_min+y_bottom_margin):
        # Setting up the cropping
        x1 = x-50
        x2 = x+w+50
        y1 = y-50
        y2 = y+h+30
        crop_img = image[y1:y2,x1:x2]

        # Saving the cropped image
        name = str(str(nameInt)+'.png')
        cv2.imwrite(name,crop_img)
        nameInt = nameInt+1
