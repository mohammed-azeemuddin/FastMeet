# FastMeet

Before you start to judge me , this script is used for connecting to my meeting on time and entering the details of the meeting such as MeetingID,password,username and other credentials automatically.

This script also helps one to connect if they've been working hard on something and forget that they had to connect to some meeting that was scheduled. (NO REMINDERS NEEDED)

I've scheduled the program to run everyday 15 min before my meeting starts so that I am on time everyday.
Its built in the form of a simple chatbot (no ML/DL used). 

Just a simple chatbot that informs you that it's meeting time and connects you to the meeting without you even touching a key or clicking anything.

It also prompts if you want to hear any music as we've joined the meeting earlier and the meeting hasn't started yet.

There are two scripts I wrote for this project
1) Automated script : Connects you to the meeting on specified time everyday
2) Instant connect script: Connects you when you run the program (doesn't run automatically as the scheduled script) 

Both the scripts have one thing in common , they enter all the necessary details required to connect to the meeting without you having to do anything.

Python Libraries used : 
1) Selenium (for automation in web browser) 
2) win32com (for simulating key presses)
3) pyttsx3 (Python text to speech library)
4) pyaudio (for working with audio and voice)
5) SpeechRecognition (for identifying speech)
Also , Windows Task Scheduler (for running the script on a specified time daily/weekly etc.)


The video demo : https://www.youtube.com/watch?v=_WiJtKpCjKE
