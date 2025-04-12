from tkinter import *
import os
import ctypes
from PIL import Image, ImageTk

os.system('taskkill /IM explorer.exe /F')

window = Tk()
window.title('CustomExplorer')
window.overrideredirect(True)
window.wm_attributes('-topmost', 1)
window.lower()
window.config(cursor='@cursors/arrow.cur')
user32 = ctypes.windll.user32
window.geometry(f'{int((user32.GetSystemMetrics(0) / 640) * 640)}x{int((user32.GetSystemMetrics(1) / 480) * 480)}+0+0')

def get_wallpaper():
    currentWallpaper = os.getenv('APPDATA') + "\\Microsoft\\Windows\\Themes\\TranscodedWallpaper"
    return currentWallpaper

image = Image.open(get_wallpaper()).resize((int((user32.GetSystemMetrics(0) / 640) * 640), int((user32.GetSystemMetrics(1) / 480) * 480)))
image = ImageTk.PhotoImage(image)
image_label = Label(window, image=image)
image_label.place(x=-2, y=-2)

window.mainloop()
