#!/usr/bin/python3
from bs4 import BeautifulSoup
import sys
from selenium import webdriver
import os
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

links = []
for arg in sys.argv[1:]:
    s = Service(executable_path="./geckodriver")
    browser = webdriver.Firefox(service=s)
    browser.get(arg)
    chwd = browser.window_handles
    p = browser.current_window_handle
    for w in chwd:
        if(w != p):
            browser.switch_to.window(w)
            browser.close()
    browser.switch_to.window(p)
    browser.maximize_window()
    last_height = browser.execute_script("return document.body.scrollHeight")
    middle = browser.find_element(By.TAG_NAME, "html")
    middle.send_keys(Keys.PAGE_DOWN)
    soup1 = 0
    soup2 = 1
    while(soup1 != soup2):
        soup1 = BeautifulSoup(browser.page_source, 'html.parser')
        middle.send_keys(Keys.PAGE_DOWN)
        time.sleep(2) #need a better way to wait for page to load
        soup2 = BeautifulSoup(browser.page_source, 'html.parser')
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    browser.quit()
    htmlas = soup.find_all('a')
    for i in htmlas:
        link = i.get("href")
        if("/watch" in str(link) or "playlist" in str(link)):
            link = "https://www.youtube.com" + link
        links.append(link)
outf = open("links", "w")
for i in links:
    outf.write(str(i) + "\n")
outf.close()
