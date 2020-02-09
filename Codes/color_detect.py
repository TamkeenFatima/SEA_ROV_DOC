import cv2
import numpy as np
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

boundaries = [
    ([17, 15, 100], [50, 56, 200]), #detecting red color
    ([86, 31, 4], [220, 88, 50]), #detecting blue color
    ([25, 146, 190], [62, 174, 250]), #detecting yellow color
    ([103, 86, 65], [145, 133, 128]), #detecting gray color
]

for (lower, upper) in boundaries:
    lower = np.array(lower, dtype = "uint8")
    upper = np.array(upper, dtype = "uint8")

    mask = cv2.inRange(image, lower, upper)
    output = cv2.bitwise_and(image, image, mask = mask)

    cv2.imshow("images", np.hstack([image, output]))
    cv2.waitKey(0)
