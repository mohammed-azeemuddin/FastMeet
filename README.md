# FastMeet

## Introduction

This script is used for connecting to meeting on time and entering the details of the meeting such as MeetingID,password,username and other credentials automatically.

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

## Testing the scripts 

We're halfway there!

Run `fast_meet_auto.py` and `fast_meet_manual.py` to test the scripts. 

## Scheduling the script using Windows task scheduler

Go to Search -> Task Scheduler

You will be able to see something like this.

![image](https://user-images.githubusercontent.com/48662097/111857361-f6753000-8956-11eb-9ba7-249256118058.png)


1) Go to the Actions (on the right) and click Create Task

![image](https://user-images.githubusercontent.com/48662097/111857421-57046d00-8957-11eb-97f4-ec167c7ef796.png)

2) In Create task enter the details as given below in the picture . Tick **run with highest priviliges** and select Configure for **Windows 10** from *dropdown*

![image](https://user-images.githubusercontent.com/48662097/111857457-87e4a200-8957-11eb-8df6-5dcfc2cf7599.png)

3) Go to triggers tab from the same create task menu and click on New..

![image](https://user-images.githubusercontent.com/48662097/111857534-2e30a780-8958-11eb-91b1-6caf0b84d530.png)

4) Enter your required time settings and click OK . 

![image](https://user-images.githubusercontent.com/48662097/111857611-b44cee00-8958-11eb-89d3-23ec2f0b78ac.png)






