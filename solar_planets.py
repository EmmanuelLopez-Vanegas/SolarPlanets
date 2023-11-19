import cv2
import numpy as np
poster=cv2.imread("thing.png")
rocket=poster[120:360, 400:500]
cv2.imshow("thing", poster)
cv2.waitKey(0)