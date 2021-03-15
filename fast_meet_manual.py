#!/usr/bin/env python
# coding: utf-8

# In[48]:

import pyttsx3
import sys
from selenium import webdriver
from getpass import getpass
from selenium.webdriver.common.keys import Keys

# In[49]:


import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'dir')))
from dir.user_details import *


# In[50]:


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

engine = pyttsx3.init()
engine.setProperty('rate', 150)
x='Connecting to the meeting....'
engine.say(x)
print(x)
engine.runAndWait()
try:
	connect_to_meet()
except:
	engine.say("some error occured")
	engine.runAndWait()
	exit(0)





