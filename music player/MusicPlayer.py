from tkinter import *
import pygame
from tkinter.filedialog import askdirectory
import os
from tkinter import messagebox

key = Tk()
key.resizable(0, 0)
key.title("Music Player UNIcompiler")
img=PhotoImage(file="image_mp3\—Pngtree—vector music notes icon_4184656.png")
key.iconphoto(False,img)
key.geometry("500x500+500+150")
key.config(bg='#116562')

pygame.mixer.init()

playlist = []
current = StringVar()
cb1 = IntVar()
vol = DoubleVar()
index = 0
p = 0
flag = 0

lbl1 = Label(key, bg="#116562", fg="Black", text="MY MUSIC",font=("Minion Pro Med",10,"bold")).place(x=50, y=15)


musiclist = Listbox(key, fg="black", bg="white", selectbackground="black",
                    selectmode=SINGLE, width=55, height=10, font=("SegoePrint", 10))
musiclist.place(x=50, y=40)

lblcursong = Label(key, bg="white", fg="black", textvariable=current, width=55, relief=RIDGE).place(x=50, y=225)



def set_vol(_=None):
    pygame.mixer.music.set_volume(vol.get() / 100)


v = Scale(key, bg="#116562", activebackground="black", fg="black",
          variable=vol, from_=0, to=100,
          tickinterval=20, orient="vertical",
          cursor="hand2", command=set_vol)
v.place(x=50, y=380)
v.set(50)


def load():
    global flag, length
    directory = askdirectory()
    if directory == '' and musiclist.curselection() == ():
        messagebox.showwarning("Attention", "No Directory Selected")
    else:
        os.chdir(directory)
        playlist.clear()
        for i in os.listdir(directory):
            if i.endswith(".mp3"):
                flag = 1
                playlist.append(i)
        if flag == 1:
            length = len(playlist)
            musiclist.delete(0, END)
            if musiclist.size() == 0:
                for i in range(0, length):
                    musiclist.insert(i, "%s" % playlist[i])
            else:
                pass
        else:
            messagebox.showerror("Error", "No MP3 files in the chosen Directory")


def play():
    global index,p
    sel = musiclist.curselection()
    if playlist == []:
        messagebox.showerror("Error", "No song in Playlist")
    elif sel == ():
        pygame.mixer.music.load(playlist[0])
        pygame.mixer.music.play()
        index = 0
        current.set(playlist[index])
    else:
        pygame.mixer.music.load(musiclist.selection_get())
        pygame.mixer.music.play()
        current.set(playlist[sel[0]])
        musiclist.selection_clear(0, END)
        index = sel[0]


def nextm():
    global index
    index += 1
    if index <= (length-1):
        pygame.mixer.music.load(playlist[index])
        update()
        pygame.mixer.music.play()
    else:
        index = 0
        pygame.mixer.music.load(playlist[index])
        update()
        pygame.mixer.music.play()


def prev():
    global index
    index -= 1
    if index >= 0:
        pygame.mixer.music.load(playlist[index])
        update()
        pygame.mixer.music.play()
    elif index < 0:
        index = len(playlist)-1
        pygame.mixer.music.load(playlist[index])
        update()
        pygame.mixer.music.play()


def update():
    current.set(playlist[index])
    musiclist.activate(index)


def pause():
    global p
    if p == 0:
        pygame.mixer.music.pause()
        current.set("Music Paused")
        p = 1
    else:
        pygame.mixer.music.unpause()
        p = 0
        current.set(playlist[index])


def stop():
    pygame.mixer.music.fadeout(500)
    current.set("Music Stopped")


def clear():
    musiclist.delete(0, END)
    pygame.mixer.music.stop()
    current.set("Playlist Cleared")


def close():
    key.destroy()


btnload = Button(key, bg="black", fg="#116562", width=11, text="Add Songs",font=("Minion Pro Med",10,"bold") ,command=load).place(x=50, y=280)
btnplay = Button(key, bg="green", fg="black", width=6, text=u"\u25B6",font=("Minion Pro Med",10,"bold"), command=play).place(x=265, y=330)
btnpause = Button(key, bg="red", fg="black", width=6, text=u"\u23F8",font=("Minion Pro Med",10,"bold"), command=pause).place(x=200, y=330)
btnnext = Button(key, bg="grey", fg="black", width=8, text=u"\u23ED",font=("arial",10,"bold"), command=nextm).place(x=330, y=330)
btnprev = Button(key, bg="grey", fg="black", width=8, text=u"\u23EE",font=("Minion Pro Med",10,"bold"), command=prev).place(x=120, y=330)
btnclear = Button(key, bg="black", fg="#116562", width=11, text="Clear Playlist", font=("Minion Pro Med",10,"bold"), command=clear).place(x=360, y=280)
btnclose = Button(key, bg="black", fg="#116562", width=10, text="Close", font=("Minion Pro Med",10,"bold"),command=close).place(x=360, y=450)


key.mainloop()
 