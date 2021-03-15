#!/usr/bin/env python
# coding: utf-8

import pafy
import vlc
from time import sleep
import random

import pyttsx3
import sys
from selenium import webdriver
from getpass import getpass
from selenium.webdriver.common.keys import Keys

import speech_recognition as sr
import os

import os 
sys.path.append(os.path.abspath(os.path.join('..', 'dir')))
from dir.user_details import *

import time
import win32com.client

engine = pyttsx3.init()
engine.setProperty('rate', 150)
r = sr.Recognizer()

def connect_to_meet():
    driver = webdriver.Chrome("./chromedriver.exe")
    driver.get(myurl)
    driver.implicitly_wait(5)
    meeting_pass=driver.find_element_by_xpath('//*[@id="ipt-joinmeeting"]')
    meeting_pass.send_keys(meet_pass)
    submit_btn = driver.find_element_by_xpath('//*[@id="join_btn"]').click()
    time.sleep(5)
    user_pass = driver.find_element_by_xpath('//*[@id="meetingInfoPassword"]')
    user_pass.send_keys(user_password)
    driver.implicitly_wait(5)
    login_form = driver.find_element_by_xpath("//button[@type='submit']").click()
    driver.implicitly_wait(5)
    join_btn = driver.find_element_by_xpath('//*[@id="smartJoinButton-trigger"]/div/button[1]')
    join_btn.click()
    driver.implicitly_wait(3)
    shell = win32com.client.Dispatch("WScript.Shell")
    time.sleep(2)
    shell.Sendkeys("{LEFT}")
    time.sleep(2)
    shell.Sendkeys("{ENTER}")
    engine.say("We are now connected and still have time,what do you want to do?")
    print("We are now connected and still have time,what do you want to do?")
    engine.runAndWait()
    with sr.Microphone() as source:
        print("Speak into the microphone")
        audio = r.listen(source)
        rec=r.recognize_google(audio)
        print("You said "+rec)
        if(rec=='play some music'):

            engine.say("Choosing a random melody to hear..")
            print("Choosing a random melody to hear..")
            engine.runAndWait()

            urls = [
            "https://www.youtube.com/watch?v=YL6gjL3w1vM&list=PLxGoKot5tMj1odQCmoHzCN1_xka8aWqQe",
            "https://www.youtube.com/watch?v=XkAtVnS9-FA&list=PLxGoKot5tMj1odQCmoHzCN1_xka8aWqQe&index=2",
            "https://www.youtube.com/watch?v=Yykd5087Vzc&list=PLxGoKot5tMj1odQCmoHzCN1_xka8aWqQe&index=3",
            "https://www.youtube.com/watch?v=jHEJvdqR3RU&list=PLxGoKot5tMj1odQCmoHzCN1_xka8aWqQe&index=5",
            "https://www.youtube.com/watch?v=fdTA2lL-27s&list=PLxGoKot5tMj1odQCmoHzCN1_xka8aWqQe&index=6"]

            url=random.choice(urls)
            video = pafy.new(url)
            best = video.getbest()
            playurl = best.url

            Instance = vlc.Instance()
            player = Instance.media_player_new()
            Media = Instance.media_new(playurl)
            Media.get_mrl()
            player.set_media(Media)
            player.play()

            sleep(60)

        else:
            pass


x='You\'ve got ten minutes for the meeting to start. Do you want to connect? Say YES or NO'
engine.say(x)
print(x)
engine.runAndWait()


with sr.Microphone() as source:
	print("Speak into the microphone")
	audio = r.listen(source)
rec=r.recognize_google(audio)
print("You said "+rec)
if(rec=='yes'):
    try:
    	connect_to_meet()
    except:
    	engine.say("some error occured")
    	engine.runAndWait()
    	sys.exit(0)
else:
	n="Okay fine! I will be on my way"
	engine.say(n)
	print(n)
	engine.runAndWait()
	sys.exit(0)


# c=input().lower()
# if(c=="yes"):
# 	try:
# 		connect_to_meet()
# 	except:
# 		engine.say("some error occured")
# 		engine.runAndWait()
# 		sys.exit(0)
# else:
# 	y="Okay fine! I will be on my way"
# 	engine.say(y)
# 	print(y)
# 	engine.runAndWait()
# 	sys.exit(0)
	
	







