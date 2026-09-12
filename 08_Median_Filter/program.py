import cv2

image = cv2.imread('08_Median_Filter/input.jpeg')

if image is None:
    print("Image not found")
    exit()

result = cv2.medianBlur(image, 5)

cv2.imwrite('output.png', result)

cv2.waitKey(0)
cv2.destroyAllWindows()
