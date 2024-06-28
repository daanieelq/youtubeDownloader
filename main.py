import tkinter
from tkinter import *
from pytube import YouTube
from bs4 import BeautifulSoup
import requests
from tkinter import messagebox
def downloadVideoMp4():
    downloadingVideo = Label (text = "Video wird heruntergeladen", height = 1, width = 20)
    downloadingVideo.pack()
    downloadingVideo.place (relx = 0.5, rely = 0.7, anchor = CENTER)
    root.after(5000, lambda: downloadingVideo.destroy())

def downloadYoutubeVideo (url, path):
    try:
        yt = YouTube(url)
        video = yt.streams.filter (progressive = True, file_extension = "mp4").order_by("resolution").desc().first()
        video.download (output_path = path)
        messagebox.showinfo ("Erfolg", "Video wurde heruntergeladen")
    except Exception as error:
        messagebox.showerror("Fehler,", f"Ein Fehler ist aufgetreten: {error}")

def getUrl():
    url = textEingabe.get ("1.0", "end-1c").strip()
    if not url:
        messagebox.showerror ("Fehler", "Bitte einen gültigen URL eingeben")
        return None
    return url

def onDownloadButtonClick():
    url = getUrl()
    if url:
        downloadVideoMp4()
        downloadYoutubeVideo(url, "./")

def retrieve_input():
    input = textEingabe.get("1.0", "end-1c")
    return input



root = Tk()

root.title ("Youtube Downloader")
root.minsize (200,200)
root.geometry ("300x300+50+50")
root.config (bg = "#404043")
root.eval ('tk::PlaceWindow . center')

textEingabe = Text (master = root, height = 2, width = 25)
textEingabe.insert (tkinter.END, "Hier den Link einfügen: ")
textEingabe.place(relx = 0.5, rely = 0.5, anchor = CENTER)

downloadButton = tkinter.Button(root, text="Herunterladen", command = onDownloadButtonClick)
downloadButton.pack()
downloadButton.place (relx = 0.5, rely = 0.6, anchor = CENTER)

checkBox = tkinter.Checkbutton (text = "MP3")
checkBox.pack()
checkBox.place (relx = 0.5, rely = 0.4, anchor = CENTER)

root.mainloop()