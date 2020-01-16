""" This script allows sounds to be mapped to buttons to make a sound board """
import tkinter
import glob
import os
from playsound import playsound
from pathlib import Path

def load_sounds():
    """ Load sound files and ensure there are files in the sounds folder """
    sounds = glob.glob(SOUND_DIR+FILE_TYPE)
    length = len(sounds)
	
    if length > 0 or length < MAX_SOUNDS:
        return sounds
    elif length >= MAX_SOUNDS:
	    raise Exception("Maximum number of files (" + MAX_SOUNDS + ") exceeded")
	
    raise Exception("No sound files loaded")

def play_sound(sound):
    """" Play a sound """
    playsound(sound)
	
def get_file_names():
    """ Gets names of sound files and remove exstensions """
    paths = os.listdir(SOUND_DIR)
    names = []
	
    for str in paths:
        (prefix, sep, suffix) = str.rpartition('.')
        names.append(prefix)
        
    return names
	
def init_sound_buttons(SOUNDS_LST, FILE_NAMES):
    """ loads sound files """
    i = 0

    while i < len(SOUNDS_LST):
        sound_button = tkinter.Button(WINDOW, text=FILE_NAMES[i], command=lambda x=SOUNDS_LST[i]: play_sound(x))
        sound_button.pack()
        i = i+1

    return

MAX_SOUNDS = 24
SOUND_DIR = "sounds"
FILE_TYPE = "/*.wav"
WINDOW_TITLE = "Simple Soundboard v0.1"
SOUNDS_LST = load_sounds()
FILE_NAMES = get_file_names()
WINDOW = tkinter.Tk()
WINDOW.title(WINDOW_TITLE)
init_sound_buttons(SOUNDS_LST, FILE_NAMES)

WINDOW.mainloop()
