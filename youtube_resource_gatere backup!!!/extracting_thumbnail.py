from selenium import webdriver
import time
from tkinter import *
from gui import *
import urllib.request
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def thumbnail_extractor():
    PATH = "C:\webdrivers\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    a=1
    # root = Tk()
    # root.geometry('700x700')
    # b_gaming = Button(root, text="Gaming")
    driver.get("https://www.youtube.com/results?search_query=Gaming")
    time.sleep(3)
    thumbnails = driver.find_elements_by_class_name('yt-img-shadow')
    for thumbnail in thumbnails:
        if (thumbnail.get_attribute('src') != None):
            if (int(thumbnail.get_attribute('width')) == 360):
                print(thumbnail.get_attribute('src'))
                src = thumbnail.get_attribute('src')
                urllib.request.urlretrieve(src, "captcha"+str(a)+".png")
                a+=1
    result=[] 
    video_links = driver.find_elements_by_id('video-title')
    for videolink in video_links:
        result.append((videolink.get_attribute('href'), videolink.get_attribute('title')))
    driver.close()
    return result
    root.mainloop()