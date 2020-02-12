import cv2

title = 'Face Detection'
cv2.namedWindow(title)
video = cv2.VideoCapture(0)#'VID-20190329-WA0142.mp4')

if video.isOpened():
    rval, frame = video.read()
else:
    rval = False

# Paths to haarcascade_frontalface_alt.xml and haarcascade_eye.xml files which are available in OpenCV dist
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#"C:\\Users\\YV\\venv3.6\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_alt.xml")
eye_cascade = cv2.CascadeClassifier('C:\\Users\\YV\\venv3.6\\Lib\\site-packages\\cv2\\data\\haarcascade_eye.xml')

while rval:

# if rval:

    # frame = cv2.flip(frame, 1)
    cv2.imshow(title, frame)
    rval, frame = video.read()

    faces = faceCascade.detectMultiScale(frame)
    # print(faces)
    if faces != ():
        headcount = faces.shape[0]
    else:
        headcount = 0

    font = cv2.FONT_HERSHEY_SIMPLEX
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, 'Face', (x+w-w//5,y+h), font, .5, (0, 0, 255), 2, cv2.LINE_AA)

        eyes = eye_cascade.detectMultiScale(frame)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(frame, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)


    cv2.putText(frame, str(headcount), (10, 25), font, .5, (255, 255, 255), 2, cv2.LINE_AA)

    key = cv2.waitKey(20)
    if key == 27:  # exit on ESC
        break

video.release()
cv2.destroyWindow(title)
