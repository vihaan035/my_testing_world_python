from selenium import webdriver
import time
from tkinter import *
from gui import *
import urllib.request
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def thumbnail_extractor(query):
    PATH = "C:\webdrivers\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    a=1
    driver.get("https://www.youtube.com/results?search_query=" + query)
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
    task_gui(result)

def gaming_gui():
    root = Tk()
    root.geometry('700x700')
    b_gaming = Button(root, text="Gaming",command = thumbnail_extractor('gaming'))
    b_fashion = Button(root, text="Fashion",command = thumbnail_extractor('fashion'))
    b_cooking = Button(root, text="Cooking",command = thumbnail_extractor('cooking'))
    b_diy = Button(root, text="DIY",command = thumbnail_extractor('diy'))
    b_fitness = Button(root, text="Fitness",command = thumbnail_extractor('fitness'))
    b_music_dance = Button(root, text="Music&Dance",command = thumbnail_extractor('musicdance'))
    b_sports = Button(root, text="Sports",command = thumbnail_extractor('sports'))
    b_tech = Button(root, text="Tech",command = thumbnail_extractor('tech'))
    b_travel = Button(root, text="tech")
    b_comedy = Button(root, text="Comedy",command = thumbnail_extractor('comedy'))

    b_gaming.pack()
    b_fashion.pack()
    b_cooking.pack()
    b_diy.pack()
    b_fitness.pack()
    b_music_dance.pack()
    b_sports.pack()
    b_tech.pack()
    b_travel.pack() 
    b_comedy.pack()
    root.mainloop()