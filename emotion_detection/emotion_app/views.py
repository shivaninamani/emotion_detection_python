import cv2
from deepface import DeepFace
from django.http import HttpResponse
from django.shortcuts import render


def app(request):
    return render(request,'main.html')

'''def emotion_detection(request):
    detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = detector.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            face_img = frame[y:y+h, x:x+w]

            emotions = DeepFace.analyze(face_img, actions=['emotion'],enforce_detection=False)

            dominant_emotion = emotions[0]['dominant_emotion']

            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame, dominant_emotion, (x, y-10), font, 0.8, (0, 0, 255), 2, cv2.LINE_AA)

        cv2.imshow('Face Emotion Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    return render(request, 'emotion_detection.html')
    '''
def emotion_detection(request):
    detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)
    emotions_list = []

    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            face_img = frame[y:y+h, x:x+w]
            emotions = DeepFace.analyze(face_img, actions=['emotion'],enforce_detection=False)
            dominant_emotion = emotions[0]['dominant_emotion']
            emotions_list.append(dominant_emotion)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame, dominant_emotion, (x, y-10), font, 0.8, (0, 0, 255), 2, cv2.LINE_AA)

        cv2.imshow('Face Emotion Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    context = {'emotions': emotions_list}
    return render(request, 'emotion_detection.html', context)
