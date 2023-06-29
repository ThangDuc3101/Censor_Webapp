# Censor_Webapp
## Description
> The CENSOR application is a web-based implementation of a video censoring tool. It utilizes the main tools such as Mediapipe and Flask. The application functions by taking input as a video (either a .mp4 file or real-time frames from a webcam), detecting faces or hands, and subsequently blurring or censoring them.
## Installation
1. Clone this repos
> git clone https://github.com/ThangDuc3101/Censor_Webapp.git
2. Activate Virtual Environment
> With Windows
- Open the terminal in my project after downloading it
- Then enter this content to the terminal: 'venv/Scripts/activate.bat'
> With Linux
- Open the terminal in my project after downloading it
- Enter this content to terminal: 'source NAMENEV/bin/activate.bat'
3. After activating the virtual environment, you should install all dependencies. I used a text file that names "requirements.txt", it contains all library that I used for this project. Enter the terminal: "pip install -r requirement.txt"
4. And now, you are ready to play with this app. Run the main.py file to start.
> Note: In this project, I used Python 3.11.4. If you can't install some libraries you can download this Python version and delete the folder that names "venv". After that create a new virtual environment by this command: "python -m venv venv". You will see a new folder created in your folder. Then, you must activate it and try to install all libraries in my requirements.txt file. 
## Demo
### Face Blur
![Face Blur](/static/images/face.jpg)
### Hands Blur
![Hands_Blur](/static/images/hands.jpg)
### Video 
https://github.com/ThangDuc3101/Censor_Webapp/assets/88826829/aa28e806-e24e-405d-898a-002f2312ce5d

