""" This script allows sounds to be mapped to buttons to make a sound board """
import tkinter
import os
import glob
from playsound import playsound
from pathlib import Path

def load_sounds():
    """ Load sound files and ensure there are files in the sounds folder """
    WAV = "/*.wav"
    MP3 = "/*.mp3"
    OOG = "/*.ogg"
	
    sounds = glob.glob(SOUND_DIR+WAV) + glob.glob(SOUND_DIR+MP3) + glob.glob(SOUND_DIR+OOG)
    length = len(sounds)
	
    if length > 0 and length < MAX_SOUNDS:
        return sounds
    elif length >= MAX_SOUNDS:
	    raise Exception("Maximum number of files (" + MAX_SOUNDS + ") exceeded")
	
    raise Exception("No sound files loaded")

def play_sound(sound):
    """" Play a sound """
    playsound(sound)
	
def init_sound_buttons(SOUNDS_LST):
    """ lnitialises sound buttons """
    USE_GRID = 6
    SLASH_CHAR = '\\'
    DOT_CHAR = '.'
    names_ext = []
    names = []
	
    for path in SOUNDS_LST:
        (folder, sep, file) = path.rpartition(SLASH_CHAR)
        names_ext.append(file)

    for file in names_ext:
        (name, sep, ext) = file.rpartition(DOT_CHAR)
        names.append(name)
		
    if (len(SOUNDS_LST) >= USE_GRID):
        sound_text = tkinter.Label(WINDOW, text="Sounds", font=HEAD_FONT, background=BG_COLOR, foreground=TXT_COLOR).grid(row=0, column=0, columnspan=2)
    else:
        sound_text = tkinter.Label(WINDOW, text="Sounds", font=HEAD_FONT, background=BG_COLOR, foreground=TXT_COLOR).pack()
		
    i = 0

    while i < len(SOUNDS_LST):
        ROW_OFFSET = i - (len(SOUNDS_LST) / 2) + 1
		
        if i < len(SOUNDS_LST) / 2 and len(SOUNDS_LST) >= USE_GRID:
            sound_button = tkinter.Button(WINDOW, text=names[i], command=lambda x=SOUNDS_LST[i]: play_sound(x), font=TXT_FONT, background=BG_COLOR, foreground=TXT_COLOR)
            sound_button.grid(column=0, row=i+1, sticky="nsew")
        elif len(SOUNDS_LST) >= USE_GRID:
            sound_button = tkinter.Button(WINDOW, text=names[i], command=lambda x=SOUNDS_LST[i]: play_sound(x), font=TXT_FONT, background=BG_COLOR, foreground=TXT_COLOR)
            sound_button.grid(column=1, row=int(ROW_OFFSET), sticky="nsew")
        else:
            sound_button = tkinter.Button(WINDOW, text=names[i], command=lambda x=SOUNDS_LST[i]: play_sound(x), font=TXT_FONT, background=BG_COLOR, foreground=TXT_COLOR)
            sound_button.pack()
			
        i = i+1
    return

MAX_SOUNDS = 24
SOUND_DIR = "sounds"
BG_COLOR = "#424242"
TXT_COLOR = "white"
FONT = "Calibri"
FONT_SIZE = 24
HEAD_SIZE = 32
TXT_FONT = (FONT, FONT_SIZE)
HEAD_FONT = (FONT, HEAD_SIZE)
WINDOW_TITLE = "Simple Soundboard v0.1"
SOUNDS_LST = load_sounds()
WINDOW = tkinter.Tk()
WINDOW.title(WINDOW_TITLE)
WINDOW.config(background=BG_COLOR)
init_sound_buttons(SOUNDS_LST)

WINDOW.mainloop()
