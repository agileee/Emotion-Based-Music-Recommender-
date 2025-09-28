import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "your_client_id"
CLIENT_SECRET = "your_client_secret"
REDIRECT_URI = "http://127.0.0.1:4301/callback"
SCOPE = "user-read-playback-state,user-modify-playback-state,user-read-currently-playing,user-top-read,playlist-modify-public"
# ---------------------------------------------------------

# Setup your Spotify app credentials
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=SCOPE
))

# Map emotions to Spotify Audio Features (Range 0.0 to 1.0)
emotion_to_features = {
    "Happy": {"target_valence": 0.9, "target_energy": 0.8, "target_danceability": 0.7},
    "Sad": {"target_valence": 0.1, "target_energy": 0.2, "target_acousticness": 0.7},
    "Angry": {"target_valence": 0.3, "target_energy": 0.9, "target_tempo": 120},
    "Neutral": {"target_valence": 0.5, "target_energy": 0.4, "target_instrumentalness": 0.6},
    "Surprise": {"target_valence": 0.7, "target_energy": 0.7, "target_loudness": 0.8},
    "Fear": {"target_valence": 0.2, "target_energy": 0.4, "target_acousticness": 0.9},
    "Disgust": {"target_valence": 0.3, "target_energy": 0.6}
}

emotion_to_search_genre = {
    "Happy": "pop",
    "Sad": "ambient",
    "Angry": "rock",
    "Neutral": "chill",
    "Surprise": "party",
    "Fear": "classical",
    "Disgust": "metal"
}

# --- MAIN FUNCTION USED IN app.py ---
def get_recommendations(emotion, limit=5):
    """
    Get recommended songs from Spotify based on detected emotion.
    Uses the SEARCH endpoint with genre as a reliable workaround.
    """
    genre = emotion_to_search_genre.get(emotion, "pop")

    results = sp.search(q=f'genre:"{genre}"', limit=limit, type='track', market='US')

    songs = []
    if not results['tracks']['items']:
        return [{"name": "No tracks found via search", "artist": "Try a different emotion", "url": ""}]

    for track in results['tracks']['items']:
        songs.append({
            "name": track['name'],
            "artist": track['artists'][0]['name'],
            "url": track['external_urls']['spotify']
        })
    return songs


