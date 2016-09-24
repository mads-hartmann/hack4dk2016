
import cv2
import sys
import argparse
import math


def extract(image_path, cascade_path, output_dir, output_prefix):
    # Create the haar cascade
    face_cascade = cv2.CascadeClassifier(cascade_path)

    # Read the image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    print "Found {} faces".format(len(faces))

    # Finding only the faces closest to the center
    img_x0, img_y0, channels = image.shape
    dist_min = 100000
    for (x, y, w, h) in faces:
        dist = math.sqrt((x-img_x0/2)**2+(y-img_y0/2)**2)
        #print(dist)
        if dist<dist_min:
            dist_min = dist
            y_min = y
            x_min = x
        #print(y_min)

    # Looping over the faces
    face_index = 0
    y_top_margin = 40
    y_bottom_margin = 15
    for (x, y, w, h) in faces:
        # Writing code that take the centermost rectangles
        dist = math.sqrt((x-img_x0)**2 + (y-img_y0)**2)
        #print('y diff is:'+str(abs(y-y_min)))
        #print('x diff is:'+str(abs(x-x_min)))
        if (abs(y-y_min)<80) and (abs(x-x_min)<400):
            # Setting up the cropping
            x1 = x-50
            x2 = x+w+50
            y1 = y-50
            y2 = y+h+30
            crop_img = image[y1:y2,x1:x2]

            face_file_path = '{}/{}-{}.jpg'.format(
                output_dir,
                output_prefix,
                face_index)

            cv2.imwrite(face_file_path, crop_img)
            face_index = face_index+1


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--image', help='', type=str)
    parser.add_argument('--cascade', help='', type=str)
    parser.add_argument('--output-dir', help='', type=str)
    parser.add_argument('--output-prefix', help='', type=str)
    args = parser.parse_args()
    extract(args.image, args.cascade, args.output_dir, args.output_prefix)
