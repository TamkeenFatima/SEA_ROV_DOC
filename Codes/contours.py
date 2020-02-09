import cv2
import numpy as np
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

boundaries = [
    ([17, 15, 100], [50, 56, 200]),
    ([86, 31, 4], [220, 88, 50]),
    ([25, 146, 190], [62, 174, 250]),
    ([103, 86, 65], [145, 133, 128]),
]

for (lower, upper) in boundaries:
    lower = np.array(lower, dtype = "uint8")
    upper = np.array(upper, dtype = "uint8")

    mask = cv2.inRange(image, lower, upper)
    output = cv2.bitwise_and(image, image, mask = mask)

    cv2.imshow("images", np.hstack([image, output]))
    cv2.waitKey(0)

    edged = cv2.Canny(output, 30, 200)

    contours, hierarchy = cv2.findContours(edged, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)

    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    final = cv2.drawContours(output, contours, contourIdx = -1, color = (0, 255, 0), thickness = 3)

    cv2.imshow('Canny Edges After Contouring', edged)
    cv2.waitKey(0)

    cv2.imshow('Contours', output)
    cv2.waitKey(0)

cv2.destroyAllWindows()
