import cv2


image = cv2.imread('template.jpg', cv2.IMREAD_COLOR)


gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

sobel_image = cv2.Sobel(gray_image, cv2.CV_8U, 1, 0, 3)
canny_image = cv2.Canny(gray_image, 50, 150)

image_list_title = ['original', 'sobel', 'canny']
image_list = [image, sobel_image, canny_image]
cv2.imshow(sobel_image)