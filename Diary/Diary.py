import os
from tkinter import *
import webbrowser


class DiaryEntry:

    def __init__(self, file_name, data_post, post_id, text_post):
        self.file_name = file_name
        self.localdir = 'C:\\Users\\kostk\\PythonProjects\\Diary'
        self.filepath = os.path.join(self.localdir, self.file_name)
        self.data = data_post
        self.id = post_id
        self.text = text_post

    def diary_details(self):
        print(f"Post was created {self.data}, have id: {self.id} and have this text: {self.text}.")


def main():
    diaryDict = {}


def open_file() -> None:
    webbrowser.open("diary.txt")


def read_file() -> None:
    text_file = open("diary.txt", "r")
    print(text_file.read())
    text_file.close()


def write_to_file() -> None:
    diary_entry = textbox.get()
    diary_entry = diary_entry + "\n"
    textbox.delete(0, END)
    text_file = open("diary.txt", "a")
    text_file.write(diary_entry)
    text_file.close()


def delete_last_line_in_file() -> None:
    with open("diary.txt", "r+") as fp:
        lines = fp.readlines()
        fp.seek(0)
        fp.truncate()
        fp.writelines(lines[:-1])


def delete_all_text_in_file() -> None:
    text_file = open("diary.txt", "r+")
    text_file.truncate()
    text_file.close()


def close() -> None:
    mGui.destroy()


mGui = Tk()

mGui.geometry("450x450")

mGui.title("My Diary")

menu_bar = Menu(mGui)

file_menu = Menu(menu_bar, tearoff=0)

file_menu.add_command(label="Open in Idle", command=read_file)
file_menu.add_command(label="Open in Notepad", command=open_file)
file_menu.add_command(label="Delete last line", command=delete_last_line_in_file)
file_menu.add_command(label="Delete all text", command=delete_all_text_in_file)
file_menu.add_command(label="Quit", command=close)

menu_bar.add_cascade(label="File", menu=file_menu)

mGui.config(menu=menu_bar)

diary = Label(mGui, text="Write your diary entry below")
diary.pack()
textbox = Entry(mGui, bd=5, width=80)
textbox.pack()
submit = Button(text="Submit", command=write_to_file)
submit.pack()

mGui.mainloop()
