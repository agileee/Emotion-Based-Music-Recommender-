import cv2
from emotion_model import detect_emotion
from spotify_recommender import get_playlist

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    emotion = detect_emotion(frame)
    cv2.putText(frame, f"Emotion: {emotion}", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
    cv2.imshow("Emotion Detector", frame)

    key = cv2.waitKey(1)
    if key == ord('q'):  # Press 'q' to quit
        break
    elif key == ord('s'):  # Press 's' to get songs
        songs = get_playlist(emotion)
        print(f"Recommended songs for {emotion}:")
        for s in songs:
            print(f"{s['name']} - {s['artist']} ({s['url']})")

cap.release()
cv2.destroyAllWindows()
