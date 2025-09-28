import cv2
import numpy as np
import streamlit as st
from emotion_model import load_emotion_model, detect_emotion
from spotify_recommender import get_recommendations

st.set_page_config(page_title="Emotion Music App", layout="wide")

st.title("🎵 Emotion-Based Music Recommender")
st.write("Your face → Emotion → Spotify recommendations")

# Load model once
model = load_emotion_model()

# Streamlit camera input
img_file_buffer = st.camera_input("Take a picture")

emotion_emojis = {
    "Happy": "😃",
    "Sad": "😢",
    "Angry": "😡",
    "Neutral": "😐",
    "Surprise": "😲",
    "Fear": "😨",
    "Disgust": "🤢"
}

if img_file_buffer is not None:
    # Convert to OpenCV image
    file_bytes = np.asarray(bytearray(img_file_buffer.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)

    # Detect emotion
    emotion = detect_emotion(img, model)

    if emotion:
        st.write(f"Detected Emotion: {emotion} {emotion_emojis.get(emotion, '😶')}")

        # Get song recommendations
        songs = get_recommendations(emotion)

        st.markdown("### 🎶 Recommended Songs:")
        for song in songs:
            name = song["name"]
            artist = song["artist"]
            url = song["url"]
            st.markdown(f"- [{name} - {artist}]({url})")
        else:
            st.warning("No face detected. Try again!")
