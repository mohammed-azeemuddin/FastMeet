#!/usr/bin/env python
# coding: utf-8

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

engine = pyttsx3.init()
engine.setProperty('rate', 150)
x='You\'ve got ten minutes for the meeting to start. Do you want to connect? Say YES or NO'
engine.say(x)
print(x)
engine.runAndWait()

r = sr.Recognizer()
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
	
	







