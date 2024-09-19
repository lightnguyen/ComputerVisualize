import cv2
import numpy as np

def nothing(x):
    pass
img = cv2.imread(r'c:\Users\pc\Downloads\messi.jpg', cv2.IMREAD_GRAYSCALE)
cv2.namedWindow('Canny Edge Detection')
cv2.createTrackbar('Lower Threshold', 'Canny Edge Detection', 0, 255, nothing)
cv2.createTrackbar('Upper Threshold', 'Canny Edge Detection', 0, 255, nothing)
cv2.setTrackbarPos('Lower Threshold', 'Canny Edge Detection', 100)
cv2.setTrackbarPos('Upper Threshold', 'Canny Edge Detection', 200)
while True:
    lower = cv2.getTrackbarPos('Lower Threshold', 'Canny Edge Detection')
    upper = cv2.getTrackbarPos('Upper Threshold', 'Canny Edge Detection')
    edges = cv2.Canny(img, lower, upper)
    cv2.imshow('Canny Edge Detection', edges)
    if cv2.waitKey(1) & 0xFF == ord(' '):
        break
cv2.destroyAllWindows()