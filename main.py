from tkinter import *
import tkinter


root = Tk()

root.title ("Youtube Downloader")
root.minsize (200,200)
root.geometry ("300x300+50+50")
root.config (bg = "#404043")
root.eval ('tk::PlaceWindow . center')

link = Label (root, text = "Link eingeben", bg = "#ffffff", fg = "black")
link.pack(ipady = 20)
link.config (font = ("Font", 20), height = 1, width = 19)
link.place (relx = 0.5, rely = 0.5, anchor = CENTER)

link_frame = Frame(root, bg = "#6FAFE7")
link_frame.pack()
Label (link_frame, text = "Herunterladen", bg ="#ffffff", fg = "black").pack (side = "left", padx = 0)
link_frame.place (relx = 0.5, rely = 0.6, anchor = CENTER)

checkBox = tkinter.Checkbutton (text = "MP3")
checkBox.pack()
checkBox.place (relx = 0.5, rely = 0.4, anchor = CENTER)

root.mainloop()