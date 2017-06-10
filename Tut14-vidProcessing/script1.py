import cv2

img = cv2.imread('galaxy.jpg',0)# for color pass 1 for black&white pass 0, -1 = transparency capabilities

print(type(img))
print(img) # it is a an array
print(img.shape) # shape is the amount of arrays in arrays
print(img.ndim) # how many dimensions

# resizedImage = cv2.resize(img,(500,1000))
length = int(img.shape[0]/2)
width = int(img.shape[1]/2)
print(length, width)

resizedImage = cv2.resize(img, (width, length))

cv2.imshow('galaxy.jpg',resizedImage)

cv2.imwrite('galaxy_resized.jpg',resizedImage)
cv2.waitKey(3000) #0 will keep the image until you press a button
cv2.destroyAllWindows()
