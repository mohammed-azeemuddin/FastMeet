FastMeet
This script is used for connecting to my meeting on time and entering the details of the meeting such as MeetingID,password,username and other credentials automatically.

This script also helps one to automatically connect to a meeting without them needing to remember about it once scheduled. (NO REMINDERS NEEDED) 🤠✌️

I've scheduled the program to run everyday 15 min before my meeting starts (using Windows Task Scheduler). Its built in the form of a simple chatbot (no ML/DL used). ✨ It also prompts if you want to hear any music as we've joined the meeting earlier than expected. 🎶

A simple chatbot that informs you that it's meeting time and connects you to the meeting without you even touching a key or clicking anything. It also prompts if you want to hear any music as we've joined the meeting earlier and the meeting hasn't started yet.

There are two scripts in this project

Automated script : Connects you to the meeting on specified time everyday
Instant connect script: Connects you when you run the program (doesn't run automatically as the scheduled script)
Both the scripts have one thing in common , they enter all the necessary details required to connect to the meeting without you having to do anything.

Python Libraries used :

1. Selenium (for automation in web browser)
2. win32com (for simulating key presses)
3. pyttsx3 (Python text to speech library)
4. pyaudio (for working with audio and voice)
5. SpeechRecognition (for identifying speech) Also , Windows Task Scheduler (for running the script on a specified time daily/weekly etc.)

The video demo : https://www.youtube.com/watch?v=_WiJtKpCjKE

## Steps for installation
**Python version - 3.8.5 used**

Use cmd prompt and enter the given code below for installing all the required libararies. Make sure you are working in project directory itself.

`pip install -r requirements.txt`

Check if your python version is 32 bit or 64 bit version
Go to cmd and type

`python`

You will see something similar to this picture

