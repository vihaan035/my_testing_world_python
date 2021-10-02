from tkinter import *
import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys
import subprocess

def onclick1():
    import Nothing_more_than_assistant.py

root = Tk()
root.title("Button")

#First step: Create Element
btn1 = Button(root, text="Launch Jarvis",command=onclick1)

#Last step: Put element on the main window
btn1.pack()

root.mainloop()
