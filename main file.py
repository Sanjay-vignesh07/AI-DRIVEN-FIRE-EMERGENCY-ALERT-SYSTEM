import cv2
import time


fire_cascade = cv2.CascadeClassifier('C:/Users/admin/OneDrive/Desktop/sanjay vignesh/fire detection/fire_detection.xml') # add extension of xml file for Haar cascade model




cap = cv2.VideoCapture(0)
while 1:
    import pyttsx3

    ret, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    fire = fire_cascade.detectMultiScale(img, 1.2, 5)
    for (x, y, w, h) in fire:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

        engine = pyttsx3.init()
        engine.say('Fire')
        engine.runAndWait()
        time.sleep(0.2)


    winName = 'Fire detection system'
    cv2.namedWindow(winName, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(winName, 1000, 1000)
    cv2.imshow(winName, img)


    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()