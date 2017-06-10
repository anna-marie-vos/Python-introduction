import cv2
import os

images = os.listdir('./images')

def resize(filePath, image):
    img = cv2.imread(filePath,1)
    length = 100
    width = 100
    resizedImage = cv2.resize(img, (width,length))
    newFilePath = './resized/'+image
    cv2.imwrite(newFilePath,resizedImage)

for image in images:
    fileName = './images/'+image
    resize(fileName, image)
