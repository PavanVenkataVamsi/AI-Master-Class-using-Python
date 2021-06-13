import cv2
img=cv2.imread("Dhoni.jpg")
print(img.size)
print(img.shape)
print(img.dtype)
grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)     #color image into gray image
cv2.imwrite("GrayImage.jpg",grayImg)            
cv2.imshow("Original",img)
cv2.imshow("GrayImage",grayImg)
cv2.waitKey(0)
cv2.destroyALLWindows()
