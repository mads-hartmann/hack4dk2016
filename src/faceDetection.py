
import cv2
import sys
import argparse


def analyze(image_file, cascade_file):
    print image_file
    print cascade_file

    # imagePath = 'testImg.jpg'
    # image = cv2.imread(imagePath)
    # #cv2.imshow('ImageWindow',image)
    # #cv2.waitKey()
    #
    # # Create the haar cascade
    # faceCascade = cv2.CascadeClassifier(cascPath)
    #
    #
    # faces = faceCascade.detectMultiScale(
    #     gray,
    #     scaleFactor=1.1,
    #     minNeighbors=5,
    #     minSize=(30, 30),
    #     flags = cv2.cv.CV_HAAR_SCALE_IMAGE
    # )
    #
    # #imagePath = sys.argv[1]
    # #cascPath = sys.argv[2]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='CSV file to read from', type=str)
    parser.add_argument('--cascade', help='JSON file to write to', type=str)
    args = parser.parse_args()
    analyze(args.input, args.cascade)
