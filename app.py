import cv2

img = cv2.imread("files/galaxy.jpg", 0)


resized_image = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
cv2.imshow("Galaxy", resized_image)
cv2.imwrite("files/Galaxy_resized.jpg", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
