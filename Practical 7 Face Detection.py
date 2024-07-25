import cv2

img = cv2.imread("11.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
haar_cascade_face = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
faces = haar_cascade_face.detectMultiScale(gray_img, scaleFactor=1.3, minNeighbors=5)

print("Number of faces detected:", len(faces))

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow('Detected faces', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
