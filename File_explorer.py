# Python program to create 
# a file explorer in Tkinter
  
# import all components
# from the tkinter library
from tkinter import *
import os
from pathlib import Path
  
# import filedialog module
from tkinter import filedialog
  
# Function for opening the 
# file explorer window
def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select any MP3 Song",
                                          filetypes=(("Audio Files", ".mp3 .wav .ogg"),   ("All Files", "*.*")))
      
    # Change label contents
    #label_file_explorer.configure(text="File Opened: "+filename) 
    path = Path(filename)
    print(path)
    #print(os.path.abspath(path))
    cmd = str("python 2_app.py -t dl -m F:\Python\music_genre_16\custom_cnn_2d.h5 -s"+" "+str(path))
    os.system(cmd)
	

	
# Create the root window
window = Tk()
  
# Set window title
window.title("MGC")
  
# Set window size
window.geometry("1538x1028")
  
#Set window background color
window.config(background = "white")
  
# Create a File Explorer label
label_file_explorer = Label(window, anchor = CENTER, font = 14,
                            text = "Music Genre Classifier and Segregator Using CNN",
                            width = 150, height = 4, 
                            fg = "black")
  
      
button_explore = Button(window,
                        text = "Upload Song",
                        command = browseFiles) 
  
button_exit = Button(window, 
                     text = "Exit",
                     command = window.destroy) 
  
# Grid method is chosen for placing
# the widgets at respective positions 
# in a table like structure by
# specifying rows and columns
label_file_explorer.grid(column = 1, row = 1)
  
button_explore.place(x=630,y=250)
  
button_exit.place(x=650,y=350)
  
# Let the window wait for any events
window.mainloop()