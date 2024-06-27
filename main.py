from tkinter import *


root = Tk()

root.title ("Youtube Downloader")
root.minsize (200,200)
root.geometry ("300x300+50+50")
root.config (bg = "#404043")

link = Label (root, text = "Link eingeben", bg = "#ffffff", fg = "black")
link.pack(ipady = 20)
link.config (font = ("Font", 10), height = 1, width = 25)

can = Canvas (root, bg = "red", height = 50, width = 50)
can.place (x = 100, y = 100, anchor = NW)

link_frame = Frame(root, bg = "#6FAFE7")
link_frame.pack()
Label (link_frame, text = "Herunterladen", bg ="#ffffff").pack (side = "left", padx = 0)

root.mainloop()