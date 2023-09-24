import socket
from tkinter import *
from threading import Thread
import random

# PIL - python imaging library
# used to deal with uploading images and using/manipulating/saving them
from PIL import ImageTk, Image

SERVER = None
PORT = None
IP_ADDRESS = None

playerName = None
nameEntry = None
nameWindow = None
canvas1 = None
screen_width = None
screen_height = None

# creating a client server which helps client connect with main server
def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    PORT = 6000
    IP_ADDRESS = '127.0.0.1'

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

    askName()

# getting the name of the player
def askName():
    global playerName
    global nameEntry
    global nameWindow
    global canvas1
    global screen_width
    global screen_height

    nameWindow = Tk()
    nameWindow.title('Tambola')
    nameWindow.configure(width=500, height=500)
    # determining width and height of tkinter screen based on window screen dimensions
    screen_width = nameWindow.winfo_screenwidth()
    screen_height = nameWindow.winfo_screenheight()

    bg = ImageTk.PhotoImage(file = './assets/background.png')

    canvas1 = Canvas(nameWindow, width=800, height=600)
    canvas1.pack(fill='both', expand=True)

    # displaying the background image and text on canvas
    canvas1.create_image(0, 0, image=bg, anchor='nw')
    canvas1.create_text(screen_width/5, screen_height/8, text='Enter Name', font=('Chalkboard SE', 60), fill='black')

    nameEntry = Entry(nameWindow, width=15, justify='center', font=('Chalkboard SE', 30), bd=5, bg='white')
    nameEntry.place(x=screen_width/7, y=screen_height/5.5)

    button = Button(nameWindow, text='Continue', font=('Chalkboard SE', 30), width=11, command=saveName, height=2, bg='#757dbd', bd=3)
    button.place(x=screen_width/6, y=screen_height/4)

    nameWindow.resizable(False, False)
    nameWindow.mainloop()

# saving the player name and sending it to server
def saveName():
    global SERVER
    global playerName
    global nameWindow
    global nameEntry

    playerName = nameEntry.get()
    nameEntry.delete(0, END) # removing EVERYTHING in nameEntry box
    nameWindow.destroy() # destroying initial screen and moving on to next

    SERVER.send(playerName.encode())

setup()