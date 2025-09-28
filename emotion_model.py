import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Emotion labels (as per FER-2013 dataset)
emotion_labels = ['Angry','Disgust','Fear','Happy','Sad','Surprise','Neutral']

# --- Load model function (for Streamlit and others) ---
def load_emotion_model():
    return load_model("emotion_model.h5")

# --- Detect emotion from frame/image ---
def detect_emotion(frame, model=None):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    emotion = None
    for (x,y,w,h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_gray = cv2.resize(roi_gray, (48,48))
        roi_gray = roi_gray.astype("float")/255.0
        roi_gray = np.expand_dims(roi_gray, axis=0)
        roi_gray = np.expand_dims(roi_gray, -1)

        # Use provided model if passed, else load default
        if model is None:
            model = load_model("emotion_model.h5")

        prediction = model.predict(roi_gray, verbose=0)[0]
        emotion = emotion_labels[np.argmax(prediction)]
        break  # take the first detected face only

    return emotion if emotion else "Neutral"
