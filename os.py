import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess
import os

def open_cmd():
    os.system("python3 cmd.py")

def open_game():
    subprocess.Popen(['python3', 'game.py'])

def open_file():
    subprocess.Popen(['python3', 'file.py'])

def open_notepad():
    subprocess.Popen(['python3', 'notepad.py'])

def open_web():
    subprocess.Popen(['python3', 'web.py'])

def open_calculator():
    os.system("python3 calculator.py")

def show_context_menu(event):
    context_menu.post(event.x_root, event.y_root)


root = tk.Tk()
root.title("My Desktop")
root.attributes("-fullscreen", True)


background_image = Image.open("860.jpg")
background_image = background_image.resize((10000, 1200), Image.LANCZOS)
background_photo = ImageTk.PhotoImage(background_image)

background_label = tk.Label(root, image=background_photo)
background_label.place(relwidth=1, relheight=1)


button_frame = tk.Frame(root, bg='white')
button_frame.pack(side=tk.BOTTOM, fill=tk.X)


notepad_button = tk.Button(button_frame, text="Text Editor", command=open_notepad)
notepad_button.pack(side=tk.LEFT, padx=10, pady=10)

calculator_button = tk.Button(button_frame, text="Calculator", command=open_calculator)
calculator_button.pack(side=tk.LEFT, padx=10, pady=10)

web_button = tk.Button(button_frame, text="Browser", command=open_web)
web_button.pack(side=tk.LEFT, padx=10, pady=10)

file_Button = tk.Button(button_frame, text="Explorer", command=open_file)
file_Button.pack(side=tk.LEFT, padx=10, pady=10)

game_button = tk.Button(button_frame, text="Game", command=open_game)
game_button.pack(side=tk.LEFT, padx=10, pady=10)

cmd_button = tk.Button(button_frame, text="Console", command=open_cmd)
cmd_button.pack(side=tk.LEFT, padx=10, pady=10)


context_menu = tk.Menu(root, tearoff=0)
context_menu.add_command(label="Text Editor", command=open_notepad)
context_menu.add_command(label="Calculator", command=open_calculator)
context_menu.add_command(label="Browser", command=open_web)
context_menu.add_command(label="Explorer", command=open_file)
context_menu.add_command(label="Game", command=open_game)
context_menu.add_command(label="Console", command=open_cmd)
context_menu.add_separator()
context_menu.add_command(label="Exit", command=root.quit)


root.bind("<Button-3>", show_context_menu)


root.mainloop()
