from tkinter import *
import os
import ctypes
from PIL import Image, ImageTk
import keyboard

#os.system('taskkill /IM explorer.exe /F')

window = Tk()
window.title('CustomExplorer')
window.overrideredirect(True)
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

taskbar = Toplevel(window)
taskbar.geometry(f'{int((user32.GetSystemMetrics(0) / 640) * 640)}x{int((user32.GetSystemMetrics(1) / 480) * 18)}+0+{int((user32.GetSystemMetrics(1) / 480) * (480 - 17))}')
taskbar.wm_attributes('-topmost', 1)
taskbar.overrideredirect(True)
taskbar.config(cursor='@cursors/arrow.cur')
taskbar.config(bg='lightgrey')
line = Frame(taskbar, width=int((user32.GetSystemMetrics(0) / 640) * 640), height=int((user32.GetSystemMetrics(1) / 480) * 1.5))
line.config(bg='white')
line.place(x=0, y=0)
clockinfo = Button(taskbar, text='', width=int((user32.GetSystemMetrics(0) / 640) * 5))
clockinfo.config(relief=SUNKEN)
clockinfo.place(x=int((user32.GetSystemMetrics(0) / 640) * 600), y=int((user32.GetSystemMetrics(1) / 480) * (18 - 16)))
start_image = Image.open('start.png').resize((18, 18))
start_image = ImageTk.PhotoImage(start_image)
start = Button(taskbar, image=start_image, text='Start ', compound=LEFT, font='Arial 10 bold')
start.width, start.height = int((user32.GetSystemMetrics(0) / 640) * 3.5), int((user32.GetSystemMetrics(1) / 480) * 16)
start.config(cursor='@cursors/Cursor_15.cur')
start.place(x=int((user32.GetSystemMetrics(0) / 640) * 1.5), y=int((user32.GetSystemMetrics(1) / 480) * (18 - 16)))

keyboard.add_hotkey('windows', lambda: print('Open start menu'))

window.mainloop()
