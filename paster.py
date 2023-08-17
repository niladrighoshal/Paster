import re
from pynput.keyboard import Controller
from pynput.keyboard import Key
import tkinter as tk
import time
import keyboard as kb
import webbrowser
from pathlib import Path
from tkinter import filedialog
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import *
from tkinter import messagebox
from base_64_data import base64_strings

keyboard = Controller()


root = Tk()
root.title("Paster by Niladri Ghoshal")
root.geometry("695x400")
root.resizable(0, 0)
root.configure(bg="#FFFFFF")

photo = PhotoImage(data=base64_strings["icons.png"])

root.iconphoto(False, photo)

keyboard = Controller()

fontSmall = ('', 8)
cursor = "hand2"


def callback(event):
    webbrowser.open_new_tab(event)


def rTime():
    time.sleep(4)


def rTime1():
    time.sleep(1)


from pynput.keyboard import Key, Controller as KeyboardController

keyboard = KeyboardController()

from pynput.keyboard import Key, Controller as KeyboardController

keyboard = KeyboardController()

def paste():
    input1 = entry.get(1.0, tk.END + "-1c")

    # Split the input code into lines
    lines = input1.split("\n")

    # Type each line with SHIFT + TAB (reverse indentation)
    rTime()
    for line in lines:
        # Press the Home key to move the cursor to the beginning of the line
        keyboard.press(Key.home)
        keyboard.release(Key.home)

        if line.strip():  # Check if the line is not empty (to avoid pasting empty lines)
            keyboard.type(line + "\n")
        else:
            keyboard.type("\n")



def paste_in_the_entry():
    # Get the last copied text from the clipboard
    clipboard_text = root.clipboard_get()

    # Insert the clipboard_text into the entry field
    entry.delete(1.0, tk.END)  # Clear the existing content in the entry field
    entry.insert(tk.END, clipboard_text)


def insert_file():
    try:
        file_path = filedialog.askopenfilename(initialdir="./", title="Select a file",
                                            filetypes = [("Plain Text", "*.txt"),
                                                        ("CSV (Comma-Separated Values)", "*.csv"),
                                                        ("JSON (JavaScript Object Notation)", "*.json"),
                                                        ("XML (Extensible Markup Language)", "*.xml"),
                                                        ("HTML (Hypertext Markup Language)", "*.html"),
                                                        ("Markdown", "*.md"),
                                                        ("YAML (YAML Ain't Markup Language)", "*.yaml;*.yml"),
                                                        ("INI (Configuration File)", "*.ini"),
                                                        ("Log files", "*.log"),
                                                        ("Batch Script", "*.bat"),
                                                        ("All files", "*.*")])
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                entry.delete(1.0, tk.END)  # Clear the existing content in the entry field
                entry.insert(tk.END, content)
    
    except:
        messagebox.showerror('Error','Can not read text file in the file you uploaded. Please convert it to text format and try again.')


def paste1():
    input1 = entry.get(1.0, tk.END + "-1c")
    rTime1()
    keyboard.type(input1)


def linebyline():
    input1 = re.sub(r'\t', '', entry.get(1.0, tk.END + "-1c"))
    rTime()
    keyboard.type(input1)


def singleline():
    input1 = re.sub(r'\n', '', entry.get(1.0, tk.END + "-1c"))
    rTime()
    keyboard.type(input1)


def linebyline1():
    input1 = re.sub(r'\t', '', entry.get(1.0, tk.END + "-1c"))
    rTime1()
    keyboard.type(input1)


def singleline2():
    input1 = re.sub(r'\n', '', entry.get(1.0, tk.END + "-1c"))
    rTime1()
    keyboard.type(input1)




canvas = Canvas(
    root,
    bg="#ffffff",
    height=400,
    width=710,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
entry_image_1 = PhotoImage(data=base64_strings["entry_1.png"])
entry_bg_1 = canvas.create_image(
    300.5,
    154.0,
    image=entry_image_1
)
entry = Text(
    bd=0,
    bg="#D1F6FF",
    highlightthickness=0
)
entry.place(
    x=19.0,
    y=6.0,
    width=563.0,
    height=294.0
)

button_image_1 = PhotoImage(data=base64_strings["button_1.png"])
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=paste,  
    relief="flat",
    cursor='hand2'
)
button_1.place(
    x=165.0,
    y=323.0,
    width=140.0,
    height=35.0
)

kb.add_hotkey('shift+c', paste)
canvas.create_text(
    214.0,
    360.0,
    anchor="nw",
    text="SHIFT+C",
    fill="#000000",
    font=("Inter Regular", 10 * -1)
)


button_image_2 = PhotoImage(data=base64_strings["button_2.png"])
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=singleline,
    relief="flat",
    cursor='hand2'
)
button_2.place(
    x=320.0,
    y=323.0,
    width=140.0,
    height=35.0
)

kb.add_hotkey('shift+s', singleline2)
canvas.create_text(
    370.0,
    360.0,
    anchor="nw",
    text="SHIFT+S",
    fill="#000000",
    font=("Inter Regular", 10 * -1)
)

button_image_3 = PhotoImage(data=base64_strings["button_3.png"])
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=linebyline,
    relief="flat",
    cursor='hand2'
)
button_3.place(
    x=474.0,
    y=323.0,
    width=113.0,
    height=35.0
)

kb.add_hotkey('shift+m', linebyline1)
canvas.create_text(
    510.0,
    360.0,
    anchor="nw",
    text="SHIFT+M",
    fill="#000000",
    font=("Inter Regular", 10 * -1)
)




paste_here_img = PhotoImage(data=base64_strings["paste_here.png"])
paste_here = Button(
    image=paste_here_img,
    borderwidth=0,
    highlightthickness=0,
    command=paste_in_the_entry,
    relief="flat",
    cursor='hand2'
)
paste_here.place(
    x=600.0,
    y=15.0,
    width=87.0,
    height=219.0
)

kb.add_hotkey('ctrl+v', paste_in_the_entry)
canvas.create_text(
    620.0,
    235.0,
    anchor="nw",
    text="CTRL+V",
    fill="#000000",
    font=("Inter Regular", 10 * -1)
)


insert_txt = PhotoImage(data=base64_strings["insert.png"])
insert = Button(
    image=insert_txt,
    borderwidth=0,
    highlightthickness=0,
    command=insert_file,
    relief="flat",
    cursor='hand2'
)
insert.place(
    x=610.0,
    y=265.0,
    width=60.0,
    height=68.0
)

kb.add_hotkey('ctrl+i', insert_file)
canvas.create_text(
    620.0,
    335.0,
    anchor="nw",
    text="CTRL+I",
    fill="#000000",
    font=("Inter Regular", 10 * -1)
)

github_img = PhotoImage(data=base64_strings["github.png"])
github = Button(
    image=github_img,
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    bg="#ffffff",
    cursor='hand2'
)
github.place(
    x=12.0,
    y=323.0,
    width=35.0,
    height=35.0
)
github.bind("<Button>", lambda e: callback("https://github.com/niladrighoshal"))

lbl = Label(root, text="Github", fg='medium orchid', bg="white", highlightthickness=2, highlightbackground="royalblue1",font=('', 16, 'bold'),cursor='hand2')
lbl.place(x=50, y=324)
lbl.bind("<Button>", lambda e: callback("https://github.com/niladrighoshal"))


source_code = Label(root, text="Source Code?", fg='blue4', bg="white", font=('', 9, 'bold underline'),cursor='hand2')
source_code.place(x=10, y=378)
source_code.bind("<Button>", lambda e: callback("https://github.com/niladrighoshalsource_code"))


canvas.create_text(
    470.0,
    386.0,
    anchor="nw",
    text="Auto Text Pasting Software By Niladri Ghoshal",
    fill="#000000",
    font=("Poppins", 10 * -1)
)

root.attributes('-topmost', True)

root.mainloop()
