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

![p1](https://user-images.githubusercontent.com/48662097/111827132-8c856800-890f-11eb-8fcd-4f2745d7eaf6.jpg)

*Now exit form the command prompt or close python shell*

**If your version is 64 bit**
*Open cmd and type in the below command from the same directory*

`pip install PyAudio-0.2.11-cp38-cp38-win_amd64.whl`

**If your version is 32 bit**
*Open cmd and type in the below command from the same directory*

`pip install PyAudio-0.2.11-cp39-cp39-win32.whl`

### Enter your details

Navigate to the directory FastMeet/dir1 and open `user_details.py`

**Enter the required details**

myurl  *(link to webex site)*

meet_pass  *[webex meeting id (without quotes)]*

user_password  *(webex meeting password)*

my_full_name *(your name in the meeting)*

email_id *(your email id in the meeting)*

![p1](https://user-images.githubusercontent.com/48662097/111855952-87470e00-894d-11eb-9124-7f64df0ec2cc.jpg)

## Testing your program 

We're halfway there!

Run `fast_meet_auto.py` and `fast_meet_manual.py` to test the scripts. 




