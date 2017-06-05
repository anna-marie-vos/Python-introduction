import cv2

img = cv2.imread('galaxy.jpg',0)# for color pass 1 for black&white pass 0, -1 = transparency capabilities

print(type(img))
print(img) # it is a an array
print(img.shape) # shape is the amount of arrays in arrays
print(img.ndim) # how many dimensions

cv2.imshow('galaxy.jpg',img)
cv2.waitKey(2000)
cv2.destroyAllWindows()
