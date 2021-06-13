import cv2

haar_file = "E:\\patchtech\\day5\\haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(haar_file)
webcam = cv2.VideoCapture(0)

while True:
    (_,img) = webcam.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,4)
    text="NO person Detected"
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        text="Person Detected"
    Imgidenfied = cv2.putText(img,text,(10,20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.imshow("FaceDetection",img)
    key = cv2.waitKey(10)
    if key==27:
        break
webcam.release()
cv2.destroyAllWindows()
