import cv2

image = cv2.imread('07_Gaussian_Filter/input.jpeg')

if image is None:
    print("Image not found")
    exit()

result = cv2.GaussianBlur(image, (5, 5), 0)

cv2.imwrite('output.png', result)

cv2.waitKey(0)
cv2.destroyAllWindows()
