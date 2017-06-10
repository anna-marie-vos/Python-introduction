import cv2

fce_cascade = cv2.CascadeClassifier('./files/haarcascade_frontalface_default.xml')

# img = cv2.imread('./files/photo.jpg')
img = cv2.imread('./files/news.jpg')
grayIm = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = fce_cascade.detectMultiScale(grayIm,
scaleFactor = 1.1,
minNeighbors = 5)

for x,y,w,h in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

resized = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))

cv2.imshow("gray",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
