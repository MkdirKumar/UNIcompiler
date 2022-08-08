from __future__ import unicode_literals
from asyncio.windows_events import NULL
from cgitb import text
from email.mime import image
from msilib.schema import Directory
import shutil
from tkinter import filedialog
from turtle import color, width
import pytube
import time
from tkinter.ttk import *
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube
from tkinter import *
from tkinter import messagebox
import os

import youtube_dl
from setuptools import Command

#screen+header
key = Tk()
key.geometry('500x600')
title=key.title('YouTube Video Downloader UNIcompiler')
img=PhotoImage(file="png\youtube-logo-png-2069.png")
key.iconphoto(False,img)
key.configure(bg="white")


#download function
def fun1():
    url=YouTube(str(link.get()))
    
    v=url.streams.get_highest_resolution()
    v.download()
    task=10 #download bar
    x=0
    while(x<task):
      time.sleep(1)
      bar['value']+=10
      x+=1
      key.update_idletasks()
    messagebox.showwarning("Attention", "successfully downloaded MP4")
bar= Progressbar(key, orient=HORIZONTAL, length=300)
bar.pack(pady=270)

   
 


def mp4_mp3():
  url=YouTube(str(link.get()))
  ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
  }
  with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link.get()])
    messagebox.showwarning("Attention", "successfully downloaded MP3")    
    
#GUI
canvas=Canvas(key,width=500, height=400)
canvas.pack()
key.resizable(0,0)


link=StringVar()
Label(key, text="Paste YouTube Link", font=("Minion Pro Med",15,"bold"),foreground="red").place(x=160, y=140)

    
EnterLink = Entry(key, width=40, font=31, textvariable=link,bd=2).place(x=10, y=200)
#Button(key,text='Select Path', font=("Minion Pro Med",14,"bold"), bg="red",foreground="white", command=downloadPath).place(x=185, y=300)
Button(key,text='Download MP4', font=("Minion Pro Med",12,"bold"), bg="red",foreground="white", command=fun1).place(x=300, y=350)
Button(key,text='Download mp3', font=("Minion Pro Med",12,"bold"), bg="red",foreground="white", command=mp4_mp3).place(x=50, y=350)

key.mainloop()
