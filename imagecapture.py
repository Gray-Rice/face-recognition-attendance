import cv2


def imageCapture():
    cam = cv2.VideoCapture(0)
    face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    while True:
        check, frame = cam.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        face = face_detector.detectMultiScale(
            gray, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40)
    )
        vid_frame = cv2.flip(frame, 1)

        for (x, y, w, h) in face:
            cv2.rectangle(vid_frame, (x,y), (x+w,y+h), (255,0,0), 2)  

        cv2.imshow("Press ESC to take photo", vid_frame)
        cv2.imwrite("Image.png", gray)
        key = cv2.waitKey(1)

        if key == 27:
            img = cv2.imread("Image.png")
            cam.release()
            cv2.destroyAllWindows()
            # cv2.imshow("Your Image",img)
            # key = cv2.waitKey(1)
            # cv2.destroyAllWindows()
            return img    
