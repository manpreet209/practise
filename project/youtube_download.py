from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('512x512')
root.resizable(0, 0)
root.title("TRAINING")
bg = PhotoImage(file = "unnamed.png")
canvas1 = Canvas(root, width=512,
                 height=512)

canvas1.pack(fill="both", expand=True)
canvas1.create_image(0, 0, image=bg,
                     anchor="nw")

Label(root, text='YOUTUBE VIDEO DOWNLOADER', font='arial 23 bold' ,fg= 'red',bg='black').place(x=5, y=5)

link = StringVar()

Label(root, text='Paste Link Here:', font='arial 15 bold',fg= 'red',bg='black').place(x=160, y=60)
link_enter = Entry(root,font= 'arial 12', width=55, textvariable=link).place(x=38, y=90)


def detail():
    url = YouTube(str(link.get()))
    Label(root, text=('Title: ', url.title), font='arial 15',fg='red',bg='black').place(x=20, y=240)
    Label(root, text=('view: ', url.views), font='arial 15',fg='red',bg='black').place(x=20, y=270)
    Label(root, text=('lenght: ', url.length), font='arial 15',fg='red',bg='black').place(x=20, y=300)
    Label(root, text=('rating: ', url.rating), font='arial 15',fg='red',bg='black').place(x=20, y=330)

Button(root, text='Details', bg='red', padx=2, command=detail).place(x=460, y=89)

def Downloader():
    url = YouTube(str(link.get()))
    video = url.streams.get_highest_resolution()
    video.download()
    Label(root, text='DONE', font='arial 15',fg='red',bg='black').place(x=100, y=210)

def Downloader1():
    url = YouTube(str(link.get()))
    video = url.streams.last()
    video.download()
    Label(root, text='DONE', font='arial 15',fg='red',bg='black').place(x=300, y=210)

Button(root, text='VIDEO', font='arial 15 bold', bg='red', padx=2, command=Downloader).place(x=100, y=150)
Button(root, text='AUDIO', font='arial 15 bold', bg='red', padx=2, command=Downloader1).place(x=300, y=150)

root.mainloop()

