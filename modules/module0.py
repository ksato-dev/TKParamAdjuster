# refer to https://stackoverrun.com/ja/q/10777197

import vlc
import random
from tkinter import *
from tkinter import filedialog
import threading

song = ""
instance = vlc.Instance()

def get_songs():
       global song
       global x
       global songs
       songs = filedialog.askopenfilenames()
       x = 0
       song = songs[x]
       print(songs)
       commence(song)

def pause_resume():
       player.pause()

def commence(song):
       global player
       global x
       player = instance.media_player_new()
       media = instance.media_new(song)
       player.set_media(media)
       player.play()


def next_song():
       if x >= len(songs):
           print("Error: Can't go any further")
           x = 0
           return
       player.stop()
       song = songs[x]
       commence(song)

def set_volume(v):
       global vol
       global player
       # either get the new volume from given argument v (type: str):
       # value = int(v)
       # or get it directly from Scale widget (type: int)
       value = vol.get()
       player.audio_set_volume(value)

def show_value(self):
       global player
       i = vol.get()
       player.audio_set_volume(i)

window = Tk()

window.geometry("600x600")
window.title('JukeBox')

#pause_button = Button(window, text = "Next", command = next_song)
#pause_button.grid(row=1, column = 2)
Button(window, text="Start", command=get_songs).grid(column=1,row=1)
Button(window, text="Next", command=next_song).grid(column=1,row=2)
pause_button = Button(window, text = "Pause/Resume", command = pause_resume)
pause_button.grid(row=3, column = 1)
menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_separator()
filemenu.add_command(label="Open", command=get_songs())
filemenu.add_command(label="Exit", command=window.destroy)
menubar.add_cascade(label="File", menu=filemenu)
window.config(menu=menubar)
# vol = Scale(window,from_ = 0,to = 1,orient = HORIZONTAL ,resolution = .1, command=set_volume)
vol = Scale(window,from_ = 0,to = 1,orient = HORIZONTAL ,resolution = .1, command=show_value)
vol.grid(row = 1, column = 2)

window.mainloop()
