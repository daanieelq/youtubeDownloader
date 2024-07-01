import tkinter as tk
from tkinter import messagebox
from pytube import YouTube
import os
import ffmpeg


def center_window(window):
    window.update_idletasks()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    window.geometry(f'{window_width}x{window_height}+{x}+{y}')

def clear_text(event):
    textEingabe.delete("1.0", tk.END)

def display_input():
    print("Input for Python:", var1.get())

def retrieve_input():
    return textEingabe.get("1.0", "end-1c")

def downloadVideo():
    downloadingVideo = tk.Label(text="Video wird heruntergeladen", height=1, width=20)
    downloadingVideo.pack()
    downloadingVideo.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
    root.after(5000, lambda: downloadingVideo.destroy())

def getUrl():
    url = retrieve_input().strip()
    if not url:
        messagebox.showerror("Fehler", "Bitte einen gültigen URL eingeben")
        return None
    return url

def onDownloadButtonClick():
    url = getUrl()
    if url:
        if var1.get() == 1:  # MP3-Option
            downloadVideo()
            downloadYoutubeVideoMp3(url, "./")
        else:  # MP4-Option
            downloadVideo()
            downloadYoutubeVideoMp4(url, "./")

def downloadYoutubeVideoMp4(url, path):
    try:
        yt = YouTube(url)
        video = yt.streams.filter(adaptive=True.filter(mime_type = 'video/mp4').first)
        video.download(output_path=path)
        messagebox.showinfo("Erfolg", "Video wurde heruntergeladen")
    except Exception as error:
        messagebox.showerror("Fehler", f"Ein Fehler ist aufgetreten: {error}")

    video_stream = ffmpeg.input('')

def downloadYoutubeVideoMp3(url, path):
    try:
        yt = YouTube(url)
        audio = yt.streams.filter(only_audio=True, file_extension="mp4").first()
        out_file = audio.download(output_path=path)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        messagebox.showinfo("Erfolg", "Video wurde heruntergeladen")
    except Exception as error:
        messagebox.showerror("Fehler", f"Ein Fehler ist aufgetreten: {error}")

root = tk.Tk()

root.title("Youtube Downloader")
root.minsize(200, 200)
root.geometry("300x300+50+50")
root.config(bg="#404043")
root.eval('tk::PlaceWindow . center')

textEingabe = tk.Text(master=root, height=2, width=25)
textEingabe.insert(tk.END, "Hier den Link einfügen: ")
textEingabe.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
textEingabe.bind("<Button-1>", clear_text)

downloadButton = tk.Button(root, text="Herunterladen", command=onDownloadButtonClick)
downloadButton.pack()
downloadButton.place(relx=0.5, rely=0.61, anchor=tk.CENTER)

var1 = tk.IntVar()
checkBox = tk.Checkbutton(root, text="MP3", variable=var1)
checkBox.pack()
checkBox.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

center_window(root)
root.mainloop()
