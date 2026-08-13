import cv2
img = cv2.imread('C:/Users/karan/OneDrive/Desktop/OPEN CV/lab cv.jpg')
blur = cv2.GaussianBlur(img, (7,7), 0)
cv2.imshow("Original Image", img)
cv2.imshow("Blur Image", blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
