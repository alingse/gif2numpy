from __future__ import print_function
import gif2numpy
import cv2
import time

images = [
    "Images/orange.gif",
    "Images/sea.gif",
    "Images/walk.gif", 
    "Images/hopper.gif", 
    "Images/audrey.gif", 
    "Images/Rotating_earth.gif", 
    "Images/testcolors.gif",
]

for image in images:
    frames, exts, image_specs = gif2numpy.convert(image, BGR2RGB=True)
    print()
    print("Image:", image)
    print()
    print("len frames", len(frames))
    print("len exts", len(exts))
    print("exts:", exts)
    print("image_specs:", image_specs)
    for i in range(len(frames)):
        name = "{}_{}_.jpg".format(image, i)
        cv2.imwrite(name, frames[i])
