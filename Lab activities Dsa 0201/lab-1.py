import cv2
image = cv2.imread('C:/Users/karan/OneDrive/Desktop/OPEN CV/question 1.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Orig3inal Image", image)
cv2.imshow("Grayscale Image", gray)
cv2.imwrite("gray_image.jpg", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
