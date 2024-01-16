import mindwave, time
import pygame
from pygame import mixer
from tkinter import *
from pydub import AudioSegment
from pydub.playback import play
import os

n=10
headset = mindwave.Headset('/dev/rfcomm0')

time.sleep(2)
# developed by anmol.code
while True:
    time.sleep(.5)
    x=int(headset.attention)
    print(x)
    for i in range(n):


        if x>=0 and x<=25:
             while True:
                 

                 
                 root = Tk()
                 root.title(' Music Mind')

                 root.geometry("500x400")

                 pygame.mixer.init()


                 def playsong():
                     pygame.mixer.music.load("madirfan-both-of-us-14037.mp3")
                     pygame.mixer.music.play()
                     mixer.music.set_volume(1)

                 title=Label(root,text="Music Mind",bd=9,relief=GROOVE,
                             font=("times new roman",50,"bold"),bg="white",fg="green")
                 title.pack(side=TOP,fill=X)


                 x=playsong()

                 root.after(10000, lambda: root.destroy())
                 time.sleep(2)
                 root.mainloop()
                 break

             break

        if x>=26 and x<=50:
             while True:
                  

                 
                  root = Tk()
                  root.title('Music Mind')

                  root.geometry("500x400")

                  pygame.mixer.init()
                  def playsong():
                     pygame.mixer.music.load("madirfan-both-of-us-14037.mp3")
                     pygame.mixer.music.play()
                     mixer.music.set_volume(.75)

                  title=Label(root,text="Music Mind",bd=9,relief=GROOVE,
                             font=("times new roman",50,"bold"),bg="white",fg="green")
                  title.pack(side=TOP,fill=X)


                  x=playsong()
                  root.after(10000, lambda: root.destroy())
                  time.sleep(2)

                  root.mainloop()

                  break

             break

        if x>=51 and x<=75:
             while True:
                  

                 
                  root = Tk()
                  root.title('Music Mind')

                  root.geometry("500x400")

                  pygame.mixer.init()
                  def playsong():
                     pygame.mixer.music.load("madirfan-both-of-us-14037.mp3")
                     pygame.mixer.music.play()
                     mixer.music.set_volume(.50)

                  title=Label(root,text="Music Mind",bd=9,relief=GROOVE,
                             font=("times new roman",50,"bold"),bg="white",fg="green")
                  title.pack(side=TOP,fill=X)


                  x=playsong()
                  root.after(10000, lambda: root.destroy())
                  time.sleep(2)
                  root.mainloop()

                  break
             break

        if x>=76 and x<=100:
             while True:
                 

                 
                 root = Tk()
                 root.title('Music Mind')

                 root.geometry("500x400")

                 pygame.mixer.init()
                 def playsong():
                     pygame.mixer.music.load("madirfan-both-of-us-14037.mp3")
                     pygame.mixer.music.play()
                     mixer.music.set_volume(.25)

                 title=Label(root,text="Music Mind",bd=9,relief=GROOVE,
                             font=("times new roman",50,"bold"),bg="white",fg="green")
                 title.pack(side=TOP,fill=X)


                 x=playsong()
                 root.after(10000, lambda: root.destroy())
                 time.sleep(2)
                 root.mainloop()

                 break
             break



   