#!/usr/bin/env python
# coding: utf-8

import pyttsx3
from selenium import webdriver
from getpass import getpass
from selenium.webdriver.common.keys import Keys

import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'dir1')))
from dir1.user_details import *

import time
import win32com.client

engine = pyttsx3.init()
engine.setProperty('rate', 150)

def connect_using_webex():
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
    time.sleep(6)
    shell.Sendkeys("{TAB}")
    time.sleep(2)
    shell.Sendkeys("{TAB}")
    time.sleep(2)
    shell.Sendkeys("{TAB}")
    time.sleep(2)
    shell.Sendkeys("{TAB}")
    time.sleep(2)
    shell.Sendkeys("{TAB}")
    time.sleep(2)
    shell.Sendkeys("{TAB}")
    time.sleep(2)
    shell.Sendkeys("{TAB}")
    time.sleep(2)
    shell.Sendkeys("{TAB}")
    time.sleep(2)
    shell.Sendkeys("{ENTER}")
    time.sleep(10)
    engine.say("You are now connected to the meeting")
    print("You are now connected to the meeting")
    engine.runAndWait()
    driver.quit()

def connect_using_chrome():
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
    openDropDown = driver.find_element_by_class_name('el-dropdown__caret-button').click()
    driver.implicitly_wait(5)
    shell = win32com.client.Dispatch("WScript.Shell")
    time.sleep(2)
    shell.Sendkeys("{DOWN}")
    time.sleep(2)
    shell.Sendkeys("{DOWN}")
    time.sleep(2)
    shell.Sendkeys("{DOWN}")
    time.sleep(2)
    shell.Sendkeys("{ENTER}")
    shell.SendKeys("{ENTER}")
    time.sleep(5)
    join_btn = driver.find_element_by_xpath('//*[@id="smartJoinButton-trigger"]/div/button[1]')
    join_btn.click()
    driver.implicitly_wait(3)
    iframe=driver.find_element_by_xpath('//*[@id="pbui_iframe"]')
    driver.switch_to.frame(iframe)
    full_name=driver.find_element_by_xpath('//*[@id="meetingSimpleContainer"]/div[2]/div[2]/input')
    full_name.send_keys(my_full_name)
    email_address=driver.find_element_by_xpath('//*[@id="meetingSimpleContainer"]/div[2]/div[3]/input')
    email_address.send_keys(email_id)
    next_btn = driver.find_element_by_id('guest_next-btn').click()
    driver.switch_to.default_content()
    iframe=driver.find_element_by_xpath('//*[@id="pbui_iframe"]')
    driver.switch_to.frame(iframe)
    time.sleep(1)
    driver.find_element_by_id('interstitial_join_btn').click()


x='Do you want to connect through Webex application or Google Chrome'
engine.say(x)
print(x)
print("Choose\na.Webex\nb.Chrome")
engine.runAndWait()
my_choice=input()

try:
	if(my_choice.lower()=='a'):
		connect_using_webex()
	else:
		connect_using_chrome()
except:
	engine.say("some error occured")
	engine.runAndWait()
	exit(0)





