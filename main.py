import tkinter
from tkinter import *
from PIL import Image, ImageTk

hpBar = int(100)
stamBar = int(100)
items = int()
tools = int()
wood = int()
rock = int()
food = int()
wtime = int()
hammer = int()
hammerHP = int()
axe = int()
axeHP = int()
mine = int()
mineHP = int()
pick = int()
pickHP = int()
chois = int()
rcount = int()
homesc = Tk()
homesc.title("Выживание с МАДЖИШАНС РЕД")
homesc.geometry('800x800')
canvas = Canvas(homesc, height=800, width=800)
image = Image.open("F:\Vijivalka\Survival-game\main_screen.jpg")
photo = ImageTk.PhotoImage(image)
image = canvas.create_image(0, 0, anchor='nw', image=photo)
canvas.grid(row=1, column=0)


def inventory():
    inv = Tk()
    inv.title("Инвентарь")
    inv.geometry('800x800')
    invcanvas = Canvas(inv, height=800, width=800)
    invimage = Image.open("F:\Vijivalka\Survival-game\inventory.jpg")
    ImageTk.PhotoImage(invimage)
    invcanvas.create_image(0, 0, anchor='nw', image=invimage)
    invcanvas.grid(row=1, column=0)


def MainScreen():
    start_button.place_forget()
    Label(homesc, text='Главное меню').place(x=350, y=100)
    Button(homesc, text='Инвентарь', command=inventory).place(x=310, y=200)


start_button = Button(homesc, text='Начать игру', font=('Verdana', 24), command=MainScreen)
start_button.place(x=310, y=400)
homesc.mainloop()
