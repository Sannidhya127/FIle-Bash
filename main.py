import os
import sys
import shutil
import time as t
import pathlib
from colored import fg, bg, attr
import pyttsx3
from datetime import date
from datetime import time
from datetime import datetime
from watchdog.observers import Observer
import watchdog.events
from watchdog.events import PatternMatchingEventHandler
import subprocess
import difflib
from difflib import SequenceMatcher, get_close_matches, Differ
from pprint import pprint
import re
import win32con
import win32api
import winreg as reg
from playsound import playsound
import pyautogui
from tkinter import messagebox
import tkinter as tk
from tkinter import simpledialog
import PyQt5
import plyer
from plyer import notification
import win32ui
import win32con
# subprocess.run(
#     "runas /user:KAUSTAV\Desktop\File Bash\dist\main\main.exe")


def AllFiles():
    '''
    lists all files in the directory
    '''
    listOfAll = os.listdir()
    for i in listOfAll:
        print(f"{i}")

    # ! response = win32ui.MessageBox("Binary Files Detected", "Uncode Error", win32con.MB_ICONERROR)


def printDocs():
    '''
    Prints only documents from the directory
    '''
    listOfAll = os.listdir()
    for i in listOfAll:
        docs = os.path.splitext(i)
        if docs[1] == ".docs" or docs[1] == ".txt" or docs[1] == ".docxs":
            print(docs[0]+docs[1])


def printImg():
    '''
    Prints only images from the directory
    '''
    listOfAll = os.listdir()
    for i in listOfAll:
        docs = os.path.splitext(i)
        if docs[1] == ".jpg" or docs[1] == ".png" or docs[1] == ".jpeg":
            print(docs[0]+docs[1])


def printAud():
    '''
    Prints only audio files from the directory
    '''
    listOfAll = os.listdir()
    for i in listOfAll:
        docs = os.path.splitext(i)
        if docs[1] == ".wav" or docs[1] == ".flv" or docs[1] == ".mp3" or docs[1] == ".aiff":
            print(docs[0]+docs[1])


def printMed():
    '''
    Prints only video files from the directory
    '''
    listOfAll = os.listdir()
    for i in listOfAll:
        docs = os.path.splitext(i)
        if docs[1] == ".mp4" or docs[1] == ".webm" or docs[1] == ".gif" and docs[1] == ".wmv":
            print(docs[0]+docs[1])


def printProgs():
    '''
    Prints only program files from the directory
    '''
    listOfAll = os.listdir()
    for i in listOfAll:
        docs = os.path.splitext(i)
        if docs[1] == ".py" or docs[1] == ".c" or docs[1] == ".c++" and docs[1] == ".cpp" or docs[1] == ".exe" or docs[1] == ".rb" or docs[1] == ".r" or docs[1] == ".php" or docs[1] == ".js" or docs[1] == ".html" or docs[1] == ".java" or docs[1] == ".css":
            print(docs[0]+docs[1])


def DelFile(command):
    '''
    Deltes a file with the help of the commnad `delf` 
    '''
    command.split(" ")
    existion = os.path.exists(command[5::])
    if existion == True:
        if command[1] == "" or command[1] == " " or command[1] == "  " or command[1] == "   ":
            print(
                f"{fg('red_1')}fatal: could not find any file with the mentioned name {command[1]}{attr('reset')}")
        else:
            os.remove(command[5::])
    elif existion == False:
        if command[5::] == "" or command[5::] == " " or command[5::] == "  " or command[5::] == "   ":
            print(
                f"{fg('red_1')}fatal: could not find any file with the mentioned name {command[1]}{attr('reset')}")
        else:
            print(f"{fg('red_1')}{command[5::]} does not exist{attr('reset')}")
        # print(f"{command[1]}")
    else:
        print("File Bash is facing issues while reading your disk.\nEmail us at filebash33@gmail.com for feedback")
        # notification.notify(title="Succesfully Completed ls command",
        #                     message="The ls command was successfull",
        #                     timeout=5
        #                     )


def DelDir(input):
    '''
    Uses the command `deld` to delete a directory and its inner branches and leaves
    '''
    try:
        input.split(" ")
        existion = os.path.exists(input[5::])
        if existion == True:
            shutil.rmtree(input[5::])
        elif existion == False:
            if input[5::] == "" or input[5::] == " " or input[5::] == "  " or input[5::] == "   ":
                print(
                    f"{fg('red')}fatal: couldn't find any directory in command{attr('reset')}")
            else:
                print(
                    f"{fg('red_1')}fatal : {input[5::]} does not exist{attr('reset')}")
        else:
            print("File Bash is facing issues while reading your disk.\nEmail us at filebash33@gmail.com for feedback")
    except Exception:
        win32ui.MessageBox(
            f"Function has crashed (reason might be because you have entered a name of a file instead of a directory)", "File error", win32con.MB_ICONERROR)
        print(
            f"{fg('red')}fatal: Function has crashed (reason might be because you have entered a name of a file instead of a directory){attr('reset')}")


def CreateFile(input):
    '''
    uses command `crf` to create a new file. This function earlier had a hard coding of ls --crfile which when entered would ask the users for the file name and then create a file with the name and extension
    '''
    try:
        comd.split(".")
        existion = os.path.exists(input[4::])
        if existion == False:
            open((input[4::]), "a")
        elif existion == True:
            print(
                f"{fg('sandy_brown')}fatal: {input[4::]} already exists{attr('reset')}")
        else:
            print("File Bash is facing issues while reading your disk.\nEmail us at filebash33@gmail.com for feedback")
    except Exception:
        print(
            f"{fg('red_1')}fatal: no name mentioned{attr('reset')}")


def FileRename(input):
    '''
    renames a file or a folder
    '''
    file = input.split(" ")
    existion = os.path.exists(file[1])
    if existion == True:
        os.rename(file[1], file[2])
    elif existion == False:
        print(
            f'{fg("red_1")}fatal==="{attr("reset")}{fg("red")}{file[1]}": No Such file or directory{attr("reset")}')
        try:
            creatTh = input("Do you want to create it?[y/n]: ")
            if creatTh.lower() == "y":
                open(file[1], "a")
            elif creatTh.lower() == "n":
                print("Ok")
            else:
                print(
                    f"File Bash expects y or n as yes or no respectively. {creatTh} is not a command")
        except Exception:
            pass
    else:
        print("File Bash is facing issues while reading your disk.\nEmail us at filebash33@gmail.com for feedback")


def CreateDir(input):
    '''
    creates a directory. To create a directory tree type `crd dir1/dir2/........`
    '''
    breaker = input.split(" ")
    try:
        existion = os.path.exists(breaker[1])
        if existion == False:
            os.makedirs(breaker[1])
        elif existion == True:
            print(f"{fg('red')}{breaker[1]} already exists{attr('reset')}")
        else:
            print("File Bash is facing issues while reading your disk.\nEmail us at filebash33@gmail.com for feedback")
    except Exception:
        print(
            f"{fg('red_1')}Empty Index Error: Please enter a directory name.\nEg: crd testFolder{attr('reset')}")


def cwdPrint():
    '''
    Prints the current working directory 
    '''
    print(os.getcwd())
    return ""


def cwdChange(data):
    '''
    Changes the current working directory
    '''
    mainPathForCd = input("Enter path: ")
    pathExist = os.path.exists(mainPathForCd)
    if pathExist == True:
        os.chdir(mainPathForCd)
    elif pathExist == False:
        print(f'"{mainPathForCd}": No such file or directory')
    else:
        print("File Handler Crashed!")


def checker():

    path = input(
        "Enter the fiel or directory name, if in another folder enter full path or change cwd: ")
    boolTF = os.path.exists(path)
    if boolTF == True:
        print(f"{path} exists")
    elif boolTF == False:
        print(f"{path} does not exist")


def diffChecker(file):
    FileNames = file.split(" ")
    file1 = open(FileNames[1], "r")
    file2 = open(FileNames[2], "r")
    txt1 = file1.read().splitlines()
    txt2 = file2.read().splitlines()
    dif = Differ()
    df = list(dif.compare(txt1, txt2))
    # newLine = "\n"

    # pprint(df)
    for i in df:
        if i[0] == "+":
            print(f"{fg('green')}{i}{attr('reset')}")
        elif i[0] == "-":
            print(f"{fg('red_1')}{i}{attr('reset')}")
        else:
            print(i)


def bean():
    '''
    This function will have the code for maming a small programming langauge which have the following functions:
    `variables,
    Data Types,
    Comments,
    loops, if-else statements, print, run`
    '''
    pass


def add():
    pass


def status():
    pass


def About(command):
    if command == "about bash":
        print(f"{fg('yellow_1')}Welcome to File Bash!\nFile Bash is an interactive bash or terminal which not only helps you manage your files but helps you process tasks like powershell and Git commands.\nFile Bash was created by Sannidhya. This project started on the Tue Nov 17 2020.\nSince then it has been going through a lot of updates and bug fixes. You can get the source code of this bash in Github/Sannidhya127!\nSome Code Details of File Bash are listed below\n\tVersion ------------- NIL (Not Yet in Production)\n\tWritten In ------------- Python Programming Language\n\tCreated By ------------- Sannidhya Dasgupta\n\tProject Started On ------------- Tue Nov 17 2020\n\tExtra Assets ------------- BashApi (A smart terminal to interact and help File Bash grow)\n\nThank You for using File Bash! Visit our GitHub repo and contribute or download BashApi from our website now!{attr('reset')}")


if __name__ == '__main__':
    try:
        # Get path of current working directory and python.exe
        cwd = r"C:\Users\KAUSTAV\Desktop\File Bash\dist\main.exe"
        python_exe = sys.executable

        # optional hide python terminal in windows
        hidden_terminal = '\\'.join(
            python_exe.split('\\')[:-1])+"\\pythonw.exe"

        # Set the path of the context menu (right-click menu)
        # Change 'Organiser' to the name of your project
        key_path = r'Directory\\Background\\shell\\File Bash\\'

        # Create outer key
        key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, key_path)
        # Change 'Organise folder' to the function of your script
        reg.SetValue(key, '', reg.REG_SZ, '&File Bash here')

        # create inner key
        key1 = reg.CreateKey(key, r"command")
        # change 'file_organiser.py' to the name of your script
        reg.SetValue(key1, '', reg.REG_SZ, "" +
                     f"{cwd}")
        # reg.SetValue(key1, '', reg.REG_SZ, hidden_terminal + f' "{cwd}\\file_organiser.py"')  # use to to hide terminal
    except Exception:
        keyPathEx = os.path.exists(
            "Computer\HKEY_CLASSES_ROOT\Directory\Background\shell\File Bash")
        if keyPathEx == True:
            response = win32ui.MessageBox(
                "WinError 5. Access error. Could not access registry editor. Try running File Bash as asministrator", "WinError[5] Access Error", win32con.MB_ICONERROR)
        else:
            pass

    added = False
    commands = ["ls", "ls --docs", "ls --imgs", "ls --aud", "ls --med", "ls --progs", "delf filename", "deld foldername", "mv name1  name2'", "crf 'filename'", "crd 'foldername'", "cd",
                "cd --to", "ls --check", "git status", "git init", "git add --a", "git commit -m", "git log", "git log --oneline", "git push origin branch name", "comp 'filename1' 'filename2'", "bash --q"]
    while True:
        print(fg('green_1'), os.getcwd(), attr('reset'), end='')
        comd = input(": ")
        if comd == "bash --help":
            print(f"ls (list all files and directories)\n\nls --docs (list all test files)\n\nls --imgs (list all image files)\n\nls --aud (list all audio files)\n\nls --med(list all video files)\n\nls --progs (lists all program files)\n\ndelf filename (deletes a file)\n\ndeld foldername (deletes a folder)\n\nmv fileOrFolderName (renames a file or folder)\n\ncrf filename (creates a new file or directory)\n\ncrd foldername (this creates a directory)\n\ncd (prints the current working directory)\n\ncd --to (changes the current working directory)\n\nls --check (checks a given path for existence)\n\ncomp file1 file2 (compares the text of file2 with file1 and reports the differences)\n\nbash --q (quits file bash)\n\nFor More Queries Emil us at filebash45@gmail.com")
        elif comd == "ls":
            AllFiles()
        elif comd == "ls --docs":
            printDocs()
        elif comd == "ls --imgs":
            printImg()
        elif comd == "ls --aud":
            printAud()
        elif comd == "ls --med":
            printMed()
        elif comd == "ls --progs":
            printProgs()
        elif "delf" in comd:
            DelFile(comd)
        elif "deld" in comd:
            DelDir(comd)
        elif "mv" in comd:
            FileRename(comd)
        elif "crf" in comd:
            CreateFile(comd)
        elif "crd" in comd:
            CreateDir(comd)
        elif "about bash" in comd:
            About(comd)
        elif comd == "cd":
            cwdPrint()
        elif comd == "cd --to":
            cwdChange(comd)
        elif comd == "ls --check":
            checker()
        elif comd == "git status":
            subprocess.run("git status")
        elif comd == "git init":
            subprocess.run("git init")
        elif comd == "git add --a" or comd == "git add .":
            subprocess.run("git add --a")
        elif "git commit -m" in comd:
            subprocess.run(comd)
        elif comd == "git log":
            subprocess.run("git log")
        elif comd == "git log --oneline":
            subprocess.run("git log --oneline")
        elif "git push origin" in comd:
            subprocess.run(comd)
        elif "comp" in comd:
            diffChecker(comd)
        elif comd == "bean bash":
            bean()
        elif comd == "bash stat":
            status()
        elif comd == "bash --a":
            add()
        elif comd == "bash --q" or comd == "exit":
            print("Exit Bash")
            t.sleep(0.50)
            exit()
        else:
            items = get_close_matches(comd, commands, n=1, cutoff=0.5)
            print(fg('red_1'), f"Invalid command", attr('reset'))
            for i in items:
                data = i
                print(
                    f"{fg('red')}{attr('blink')}Did you mean:\n\t{data}\nUse bash --help for commands list{attr('reset')}")
                continue
