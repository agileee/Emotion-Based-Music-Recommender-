# Python Project emotion based music recommender 

## Solo Project

----------------------------------------------

## Description

Real-time, personalized music recommendation system that uses computer vision and deep learning to determine a user's current emotional state and recommends music from Spotify to match or influence that mood.

## Features

-> Real-Time Emotion Detection: Uses a Deep Learning CNN to instantly detect a user's emotion from a live webcam feed.

-> Personalized Recommendations: Fetches music from Spotify tailored to the detected mood, using the user's Top Artists/Tracks as seeds for personalization.

## How to run

● Create a Virtual Environment (recommended)
python -m venv venv

Activate it:
Windows (Command Prompt):
venv\Scripts\activate
You’ll see (venv) before your prompt.

pip install opencv-python tensorflow keras spotipy numpy pandas streamlit

● Open in VS Code
From the same folder:
code .

● Go to Kaggle website and create an api token which will download Kaggle.json file
move this into a folder named .Kaggle (which you should create in c:/users/<your_user_name>
then type this command:
(venv) PS C:\Users\your_user_name\EmotionMusicApp> kaggle datasets download -d msambare/fer2013 -p .
This will download a zipped file named fer2013.zip.

● You need to extract the fer2013.zip file from the downloaded zip file.
Using File Explorer (Recommended for Windows):
Open File Explorer and go to C:\Users\your_user_name\EmotionMusicApp.
Find the file fer2013.zip.
Right-click on it, select "Extract All...", and follow the prompts to extract the contents right into the EmotionMusicApp folder.
Ensure the file fer2013>test and fer2013>train ends up directly inside EmotionMusicApp.

● Once fer2013-> test and train folders are present in your EmotionMusicApp folder, run your training script:
Run the following command in your terminal, which is already in your virtual environment ((venv)):
pip install scipy

● Then run python main.py to test it 
opens webcam and q for quit and s for songs

● Now for dashboard approach:
pip install streamlit
run streamlit:
streamlit run app.py

## Future fixes to be made

-Better visualization
Launch a browser tab to directly play the Spotify tracks.

-Save playlist
Extend spotify_recommender.py so pressing s automatically creates a Spotify playlist and adds those 5 songs for you.

## Author

Akhil 
(github.com/agileee)
