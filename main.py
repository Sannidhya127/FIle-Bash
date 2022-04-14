# copyright @github.com/Sannidhya127

import os  
import sys
import shutil
import time as t
import pathlib
import time
from colored import fg, bg, attr
from colored.colored import colored
import pyttsx3
import importlib
from datetime import date
from datetime import time
from datetime import datetime
import subprocess
import difflib
from difflib import SequenceMatcher, get_close_matches, Differ
from pprint import pprint
import re
import time
import plyer
from plyer import notification
from requests import delete

import win32api
import winreg as reg
from playsound import playsound
import plyer
import itertools
import threading
from plyer import notification
import win32ui
import win32con
import ctypes
import enum
import getpass
import sys
import admin
import traceback
import types
from subprocess import call
import win32api
import win32con
import win32event
import win32process
from win32com.shell.shell import ShellExecuteEx
from win32com.shell import shellcon
import logging
import math
import shutil
import multiprocessing

time = datetime.now()

logging.basicConfig(level=logging.DEBUG,
                    handlers=[logging.FileHandler(
                        f"debug.log", 'r+')],
                    format="%(asctime)s %(levelname)-6s - %(funcName)-8s - %(filename)s - %(lineno)-3d - %(message)s",
                    datefmt="[%Y-%m-%d] %H:%M:%S - ",
                    )

# if not admin.isUserAdmin():
#     admin.runAsAdmin()
# import win32com.shell.shell as shell
# ASADMIN = 'asadmin'

# if sys.argv[-1] != ASADMIN:
#     script = os.path.abspath(sys.argv[0])
#     params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
#     shell.ShellExecuteEx(
#         lpVerb='runas', lpFile=sys.executable, lpParameters=params)
#     sys.exit(0)
# print("I am root now.")

# subprocess.run("runas /user:C:\\Users\KAUSTAV\\Desktop\\File Bash\\main.py")
# os.chmod(‘spam.txt’, 0o7s77)


# def log_warn(file, func, text):
#     f = open(file, 'a')
#     time = datetime.now()
#     f.write("{time} : in function {func} : {text}")
#     f.close()


def isUserAdmin():

    if os.name == 'nt':
        import ctypes
        # WARNING: requires Windows XP SP2 or higher!
        try:
            logging.debug("User already admin")
            return ctypes.windll.shell32.IsUserAnAdmin()

            # log_warn("debug.log", "isUserAdmin", "User already admin")
        except:
            logging.warning("Admin check failed, assuming not an admin.")
            traceback.print_exc()
            print("Admin check failed, assuming not an admin.")

            return False
    elif os.name == 'posix':
        logging.info("Checked root for Posix.")

        # Check for root on Posix
        return os.getpid() == 0
    else:
        logging.error("Unsupported orperating system for the module")
        raise RuntimeError(
            "Unsupported operating system for this module: %s" % (os.name,))


def runAsAdmin(cmdLine=None, wait=True):

    if os.name != 'nt':
        raise RuntimeError("This function is only implemented on Windows.")

    python_exe = sys.executable

    if cmdLine is None:
        cmdLine = [python_exe] + sys.argv
    elif type(cmdLine) not in (types.TupleType, types.ListType):
        raise ValueError("cmdLine is not a sequence.")
    cmd = '"%s"' % (cmdLine[0],)
    # XXX TODO: isn't there a function or something we can call to massage command line params?
    params = " ".join(['"%s"' % (x,) for x in cmdLine[1:]])
    cmdDir = ''
    showCmd = win32con.SW_SHOWNORMAL
    #showCmd = win32con.SW_HIDE
    lpVerb = 'runas'  # causes UAC elevation prompt.

    # print "Running", cmd, params

    # ShellExecute() doesn't seem to allow us to fetch the PID or handle
    # of the process, so we can't get anything useful from it. Therefore
    # the more complex ShellExecuteEx() must be used.

    # procHandle = win32api.ShellExecute(0, lpVerb, cmd, params, cmdDir, showCmd)

    procInfo = ShellExecuteEx(nShow=showCmd,
                              fMask=shellcon.SEE_MASK_NOCLOSEPROCESS,
                              lpVerb=lpVerb,
                              lpFile=cmd,
                              lpParameters=params)

    if wait:
        procHandle = procInfo['hProcess']
        obj = win32event.WaitForSingleObject(procHandle, win32event.INFINITE)
        rc = win32process.GetExitCodeProcess(procHandle)
        # print "Process handle %s returned code %s" % (procHandle, rc)
    else:
        rc = None

    return rc


def test():
    rc = 0
    if not isUserAdmin():
        print("You're not an admin.", os.getpid(), "params: ", sys.argv)
        #rc = runAsAdmin(["c:\\Windows\\notepad.exe"])
        rc = runAsAdmin()
    else:
        print("You are an admin!", os.getpid(), "params: ", sys.argv)
        rc = 0
    x = input('Press Enter to exit.')
    return rc


class SW(enum.IntEnum):

    HIDE = 0
    MAXIMIZE = 3
    MINIMIZE = 6
    RESTORE = 9
    SHOW = 5
    SHOWDEFAULT = 10
    SHOWMAXIMIZED = 3
    SHOWMINIMIZED = 2
    SHOWMINNOACTIVE = 7
    SHOWNA = 8
    SHOWNOACTIVATE = 4
    SHOWNORMAL = 1


class ERROR(enum.IntEnum):

    ZERO = 0
    FILE_NOT_FOUND = 2
    PATH_NOT_FOUND = 3
    BAD_FORMAT = 11
    ACCESS_DENIED = 5
    ASSOC_INCOMPLETE = 27
    DDE_BUSY = 30
    DDE_FAIL = 29
    DDE_TIMEOUT = 28
    DLL_NOT_FOUND = 32
    NO_ASSOC = 31
    OOM = 8
    SHARE = 26


def main():
    print(" ")


def bootstrap():
    if ctypes.windll.shell32.IsUserAnAdmin():
        main()
    else:
        hinstance = ctypes.windll.shell32.ShellExecuteW(
            None, 'runas', sys.executable, sys.argv[0], None, SW.SHOWNORMAL
        )
        if hinstance <= 32:
            raise RuntimeError(ERROR(hinstance))


def AllFiles():
    '''
    lists all files in the directory
    '''
    listOfAll = os.listdir()
    for i in listOfAll:
        diri = os.path.isdir(i)
        if diri == True:
            logging.info("ls command successfully printed all files")
            print(f"{fg('blue')}\{i}{attr('reset')}\n")
        elif diri == False:
            logging.info("Succesfully printed all directories with ls")
            print(f"{i}\n")
        else:
            pass


def lsdirs():
    items = os.listdir()
    for i in items:
        dirs = os.path.isdir(i)
        if dirs == True:
            print(f"{fg('blue')}{i}\n{attr('reset')}")
        else:
            pass


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
        if docs[1] == ".wav" or docs[1] == ".flv" or docs[1] == ".mp3" or docs[1] == ".aiff" or docs[1] == ".mkv":
            print(docs[0]+docs[1])

def Suss():
    sussy_baka = '''       
                    ⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀ ⠀

            ⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀ ⠀

            ⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃

            ⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀ ⠀

            ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀

            ⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀

            ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀

            ⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀'''
    print(sussy_baka)



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
            logging.warning(
                f"Failed to delete file. Unexistent name {command[1]}")
            print(
                f"{fg('red_1')}fatal: No file mentioned{command[1]}{attr('reset')}")

        else:
            logging.info(f"Deleted {command[5::]} from the system")
            os.remove(command[5::])

    elif existion == False:
        logging.info(
            f"File {command[5::]} does not exist. Proceeding to further checks")
        if command[5::] == "" or command[5::] == " " or command[5::] == "  " or command[5::] == "   ":

            print(
                f"{fg('red_1')}fatal: could not find any file with the mentioned name {command[5::]}{attr('reset')}")

        else:

            print(
                f"{fg('red_1')}{command[5::]} does not exist{attr('reset')}")

    else:

        print("File Bash is facing issues while reading your disk.\nEmail us at filebash33@gmail.com for feedback")


def Delete(input):
    try:
        blank = ""
        Existence = os.path.exists(input[3::])
        if Existence == True:
            fileCheck = os.path.isfile(input[3::])
            folderCheck = os.path.isdir(input[3::])
            if input[3::] == blank:
                print("No file/folder name given")
            elif fileCheck== True and folderCheck == False:
                os.remove(input[3::])
            elif fileCheck == False and folderCheck ==  True:
                shutil.rmtree(input[3::])
            else:
                print("I see no name")
        else:
            print(f"{fg('red_1')}The given item does not exist{attr('reset')}")
    except Exception:
        print(f"{fg('red_1')}Unable to access file. Might be because it is encrypted{attr('reset')}")

def DelDir(input):
    '''
    Uses the command `deld` to delete a directory and its inner branches and leaves
    '''
    try:
        input.split(" ")
        existion = os.path.exists(input[5::])  # Checking if the path exists
        if existion == True:
            logging.info(f"deleted {input[5::]} from system")
            shutil.rmtree(input[5::])  # Deleting it
        elif existion == False:
            if input[5::] == "" or input[5::] == " " or input[5::] == "  " or input[5::] == "   ":
                logging.warning(f"No name found in command {input[5::]}")
                print(
                    f"{fg('red')}fatal: couldn't find any directory in command{attr('reset')}")
            else:
                logging.info(
                    f"Failed to find any directory with name: {input[5::]}")
                print(
                    f"{fg('red_1')}fatal : {input[5::]} does not exist{attr('reset')}")
        else:
            logging.error("The function crashed")
            print("File Bash is facing issues while reading your disk.\nEmail us at filebash33@gmail.com for reporting")
    except Exception:
        logging.error(f"Entered wrong info. Failed to load script")
        # win32ui.MessageBox(
        #     f"Function has crashed (reason might be because you have entered a name of a file instead of a directory)", "File error", win32con.MB_ICONERROR)
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
            logging.info(f"Opened file {input[4::]} in append mode")
            open((input[4::]), "a")

        elif existion == True:
            logging.info(
                f"Tracker has tracked that the mentioned file already exists. ReFileCreationError raised. File: {input[4::]}")
            print(
                f"{fg('sandy_brown')}fatal: {input[4::]} already exists{attr('reset')}")

        else:

            print("File Bash is facing issues while reading your disk.\nEmail us at filebash33@gmail.com for feedback")

    except Exception:

        print(
            f"{fg('red_1')}fatal: no name mentioned{attr('reset')}")



def FileRename(cmd):
    '''
    renames a file or a folder
    '''
    try:
        files = cmd.split(" ")

        # initial = files[1]

        just = os.path.exists(files[1])

        if just == True:

            os.rename(files[1], files[2])

        else:

            if files[1] == " " or files[1] == "  " or files[1] == "   " or files[1] == "    ":

                print(f"{fg('red_1')}fatal: No name mentioned{attr('reset')}")

            else:

                print(

                    f"{fg('red_1')}fatal: '{files[1]}': No such file in directory{attr('reset')}")

    except Exception:

        # print(
        #     f"{fg('red_1')}Failed to load file rename script. Exit code -1{attr('reset')}")

        print(f"{fg('red_1')}incomplete command{attr('reset')}")


def CreateDir(input):
    '''
    creates a directory. To create a directory tree type `crd dir1/dir2/........`
    '''
    breaker = input[4::]
    try:
        existion = os.path.exists(input[3::])
        if existion == False:
            os.makedirs(breaker)
        elif existion == True:
            print(f"{fg('red')}{input[4::]} already exists{attr('reset')}")
        else:
            print("File Bash is facing issues while reading your disk.\nEmail us at filebash33@gmail.com for feedback")
    except FileExistsError as e:
        # print(
        #     f"{fg('red_1')}File already exists{attr('reset')}")
        print(e)


def sys_info():
    os.system("sys_info.py")

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
    try:
        path = data[3::]
        os.chdir(path)
    except Exception:
        print(
            f"{fg('red_1')}fatal: System cannot find the specified path: '{path}'{attr('reset')}")


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
    for i in df:
        if i[0] == "+":
            print(f"{fg('green')}{i}{attr('reset')}")
        elif i[0] == "-":
            print(f"{fg('red_1')}{i}{attr('reset')}")
        else:
            print(i)


def About(command):
    if command == "about bash":
        print(f"{fg('yellow_1')}Welcome to File Bash!\nFile Bash is an interactive bash or terminal which not only helps you manage your files but helps you process tasks like powershell and Git commands.\nFile Bash was created by Sannidhya. This project started on the Tue Nov 17 2020.\nSince then it has been going through a lot of updates and bug fixes. You can get the source code of this bash in Github/Sannidhya127!\nSome Code Details of File Bash are listed below\n\tVersion ------------- NIL (Not Yet in Production)\n\tWritten In ------------- Python Programming Language\n\tCreated By ------------- Sannidhya Dasgupta\n\tProject Started On ------------- Tue Nov 17 2020\n\tExtra Assets ------------- BashApi (A smart terminal to interact and help File Bash grow)\n\nThank You for using File Bash! Visit our GitHub repo and contribute or download BashApi from our website now!{attr('reset')}")


def readFile(filename):
    try:
        name = filename[5::]
        ex = os.path.exists(name)
        if ex == True:
            try:

                fileIO = open(name, "r")
                data = fileIO.read()
                print(data)
            except UnicodeDecodeError:
                print(f"{fg('red_1')}UNICODe.characters.execeptionError(): Cannot decode UNICODE Characters. Binary reader required{attr('reset')}")
        else:
            print(
                f"{fg('red_1')}Fatal: incorrect path or '{name}' does not exist{attr('reset')}")
    except Exception:
        DirVal = os.path.isdir(name)
        if DirVal == True:
            print("I think you eneted a folder name.")
        else:
            print("Seems to be a read-only or executable file, better not try this")


def editFile(IO):
    print("OPENING FILE:")
    file = IO[6::]
    print(file)
    try:
        f = open(file, "r")
        t = f.read()
        text = t.splitlines()
        f.close()
    except Exception:
        print("failed to read file")
        # print(e)
    subprocess.run(f"notepad {file}")
    try:
        nf = open(file, "r")
        nt = nf.read()
        ntext = nt.splitlines()
        dif = Differ()
        df = list(dif.compare(text, ntext))
        for i in df:
            if i[0] == "+":
                print(f"{fg('green')}{i}{attr('reset')}")
            elif i[0] == "-":
                print(f"{fg('red_1')}{i}{attr('reset')}")
            else:
                pass
        print("Succesfully edited with exit code 0")
    except FileNotFoundError:
        print("Could not load file changes (file unexistent)")


def searchDir(query):
    srchstr = query[2::]
    AllofDir = os.listdir()
    for i in AllofDir:
        if i in srchstr:
            print(f"I found the following result(s):\n{i}")


def Notify(time):
    time = time.split(" ")
    seconds = time[1] * 60
    Title = time[2]
    Body = time[3]
    time.sleep(seconds)
    notification.notify(title=Title,
                            message=Body,
                            timeout=5
                            )

def hideItems(param):
    try:
        if "\\" in param:
            folder = param[7::]
            # print(folder)
            # call(["attrib", "+h", folder])
            os.system(f"attrib +h +s +r {folder}")
            print("Proooo tip: You might see the folder is not hidden on first sight. Refresh the folder and it's done")

            # hide \
        else:
            folder = param[5::]
            ExistF = os.path.exists(folder)
            if ExistF == True:
                print(f"Successfully hidden item {folder} with exit status 0")
                # call(["attrib", "+h", folder])
                os.system(f"attrib +h +s +r {folder}")
                print(
                    f"For issues type {fg('green_1')}'hdh'{attr('reset')} in the bash")
            else:
                print(f"{folder} does not exist")
    except Exception:
        print(f"{fg('red_1')}Failed hiding item. Exit code -1{attr('reset')}")


def unhide(param):
    name = param[4::]
    os.system(f"attrib -h -s -r {name}")


def bashGui():
    def GuiDelDir(cmd):
        os.mkdir(cmd[14::])
    cwd = os.getcwd()
    print(f"{fg('yellow_1')}Hello My Friend! Need some help :-) ?? Type help me and I will nbe there for you!!! Or else not :D")
    while True:
        print(f"{fg('magenta_1')}********************************{cwd}********************************{attr('reset')}")
        remote = input(f"{fg('green')}Here you go:{attr('reset')}")
        if "help me" in remote:
            print(f"{fg('indian_red_1d')}I knew you will need some help! here you go with the super easy sommands that I understand:\ni) list all (I list all the items in this folder)\tii)create folder 'foldername'\niii)create file 'filename'\tiv)rename 'fileOrFoldername'(I ask for the new name if you type this)\nv) delete 'fileorfoldername'\thome (I return to traditional terminal based File Bash)")
        elif remote == "list all":
            AllFiles()
        elif "create folder" in remote:
            GuiDelDir(remote)
        elif remote == "exit":
            return "exit"

    return 0


def EnvoirmentvariableDisplayer(command):
    pass


def Copy(paths):
    try:
        slitted = paths.split(" ")
        fileName = slitted[1]
        print(fileName)
        TargetLocation = slitted[2]
        print(TargetLocation)
        shutil.copy(fileName, TargetLocation)
    except Exception as e:
        print(e)


def AllProcess():
    # traverse the software list
    Data = subprocess.check_output(['wmic', 'process', 'list', 'brief'])
    a = str(Data)
    # try block
    #  arrange the string
    try:
        for i in range(len(a)):
            print(a.split("\\r\\r\\n")[i])
    except IndexError as e:
        print("All Done")

def killTask(process):
    PidProcess = process.split("\\")
    PidProcess[1] = int(PidProcess[1])
    os.kill(PidProcess[0], PidProcess[1])

def reloadProgram():
    os.system("reload.py")
    exit()
    # from colored import fg, bg, attr

def helpText():
    try:
        f = open("commands.txt", "r")
        txt = f.read()
        print(txt)
    except FileNotFoundError:
        print(f"{fg('red_1')}File Bash is unable to find commands.txt.\nThis might be the result of interruptions caused while installing file bash. We reccomend you updating file bash{attr('reset')}")


def BashApi():
    subprocess.run("python bashApi.py")

def ShutDown():
    os.system('shutdown -s')
# def HackerTheme():
#     name = input("En")

def InstallationCheck():
    files = os.listdir()
    if "reload.py" not in files:
        reloadFileCrt = open("reload.py", "w")
        reloadFileWriting = reloadFileCrt.write('''import os

os.system("main.py")''')
    elif "sys_info.py" not in files:
        sysInfoCrt = open("sys_info.py", "w")
        sysInfoWrite = sysInfoCrt.write('''from tabulate import tabulate
import GPUtil
import psutil
import platform
from datetime import datetime


def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


print("="*40, "System Information", "="*40)
uname = platform.uname()
print(f"System: {uname.system}")
print(f"Node Name: {uname.node}")
print(f"Release: {uname.release}")
print(f"Version: {uname.version}")
print(f"Machine: {uname.machine}")
print(f"Processor: {uname.processor}")

# Boot Time
print("="*40, "Boot Time", "="*40)
boot_time_timestamp = psutil.boot_time()
bt = datetime.fromtimestamp(boot_time_timestamp)
print(
    f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")

# let's print CPU information
print("="*40, "CPU Info", "="*40)
# number of cores
print("Physical cores:", psutil.cpu_count(logical=False))
print("Total cores:", psutil.cpu_count(logical=True))
# CPU frequencies
cpufreq = psutil.cpu_freq()
print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
print(f"Current Frequency: {cpufreq.current:.2f}Mhz")
# CPU usage
print("CPU Usage Per Core:")
for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
    print(f"Core {i}: {percentage}%")
print(f"Total CPU Usage: {psutil.cpu_percent()}%")

# Memory Information
print("="*40, "Memory Information", "="*40)
# get the memory details
svmem = psutil.virtual_memory()
print(f"Total: {get_size(svmem.total)}")
print(f"Available: {get_size(svmem.available)}")
print(f"Used: {get_size(svmem.used)}")
print(f"Percentage: {svmem.percent}%")
print("="*20, "SWAP", "="*20)
# get the swap memory details (if exists)
swap = psutil.swap_memory()
print(f"Total: {get_size(swap.total)}")
print(f"Free: {get_size(swap.free)}")
print(f"Used: {get_size(swap.used)}")
print(f"Percentage: {swap.percent}%")

# Disk Information
print("="*40, "Disk Information", "="*40)
print("Partitions and Usage:")
# get all disk partitions
partitions = psutil.disk_partitions()
for partition in partitions:
    print(f"=== Device: {partition.device} ===")
    print(f"  Mountpoint: {partition.mountpoint}")
    print(f"  File system type: {partition.fstype}")
    try:
        partition_usage = psutil.disk_usage(partition.mountpoint)
    except PermissionError:
        # this can be catched due to the disk that
        # isn't ready
        continue
    print(f"  Total Size: {get_size(partition_usage.total)}")
    print(f"  Used: {get_size(partition_usage.used)}")
    print(f"  Free: {get_size(partition_usage.free)}")
    print(f"  Percentage: {partition_usage.percent}%")
# get IO statistics since boot
disk_io = psutil.disk_io_counters()
print(f"Total read: {get_size(disk_io.read_bytes)}")
print(f"Total write: {get_size(disk_io.write_bytes)}")

# Network information
print("="*40, "Network Information", "="*40)
# get all network interfaces (virtual and physical)
if_addrs = psutil.net_if_addrs()
for interface_name, interface_addresses in if_addrs.items():
    for address in interface_addresses:
        print(f"=== Interface: {interface_name} ===")
        if str(address.family) == 'AddressFamily.AF_INET':
            print(f"  IP Address: {address.address}")
            print(f"  Netmask: {address.netmask}")
            print(f"  Broadcast IP: {address.broadcast}")
        elif str(address.family) == 'AddressFamily.AF_PACKET':
            print(f"  MAC Address: {address.address}")
            print(f"  Netmask: {address.netmask}")
            print(f"  Broadcast MAC: {address.broadcast}")
# get IO statistics since boot
net_io = psutil.net_io_counters()
print(f"Total Bytes Sent: {get_size(net_io.bytes_sent)}")
print(f"Total Bytes Received: {get_size(net_io.bytes_recv)}")


# GPU information
print("="*40, "GPU Details", "="*40)
gpus = GPUtil.getGPUs()
list_gpus = []
for gpu in gpus:
    # get the GPU id
    gpu_id = gpu.id
    # name of GPU
    gpu_name = gpu.name
    # get % percentage of GPU usage of that GPU
    gpu_load = f"{gpu.load*100}%"
    # get free memory in MB format
    gpu_free_memory = f"{gpu.memoryFree}MB"
    # get used memory
    gpu_used_memory = f"{gpu.memoryUsed}MB"
    # get total memory
    gpu_total_memory = f"{gpu.memoryTotal}MB"
    # get GPU temperature in Celsius
    gpu_temperature = f"{gpu.temperature} °C"
    gpu_uuid = gpu.uuid
    list_gpus.append((
        gpu_id, gpu_name, gpu_load, gpu_free_memory, gpu_used_memory,
        gpu_total_memory, gpu_temperature, gpu_uuid
    ))

print(tabulate(list_gpus, headers=("id", "name", "load", "free memory", "used memory", "total memory",
                                   "temperature", "uuid")))
''')

if __name__ == '__main__':
    current_user = getpass.getuser()
    bootstrap()
    try:
        # Get path of current working directory and python.exe
        cwd = f"C:\\Users\\{current_user}\\Desktop\\File Bash\\dist\\main.exe"
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
    
    while True:
        # print(os.stat("main.py"))
        #file_stat = os.stat("Bigwave.exe")
        #print(file_stat.st_size / (1024*1024))
        d = os.getcwd()
        # if color == False:
        comd = input(f"{fg('46')}{d}: {attr('reset')}")
        commands = []
        if comd == "bash --help":
            print(f"ls (list all files and directories)\n\nls --docs (list all test files)\n\nls --imgs (list all image files)\n\nls --aud (list all audio files)\n\nls --med(list all video files)\n\nls --progs (lists all program files)\n\ndelf filename (deletes a file)\n\ndeld foldername (deletes a folder)\n\nmv fileOrFolderName (renames a file or folder)\n\ncrf filename (creates a new file or directory)\n\ncrd foldername (this creates a directory)\n\ncd (prints the current working directory)\n\ncd --to (changes the current working directory)\n\nls --check (checks a given path for existence)\n\ncomp file1 file2 (compares the text of file2 with file1 and reports the differences)\n\nbash --q (quits file bash)\n\nFor More Queries Email us at filebash45@gmail.com")
        elif comd == "ls":
            AllFiles()
        elif comd == "^f":
            print("#WORKING")
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
        # elif comd == "admin --run":
        #     AdministratorPermits()
        elif comd[0:4] == "delf":
            DelFile(comd)
        elif comd[0:4] == "deld":
            DelDir(comd)
        elif comd == "sys --info":
            sys_info()
        elif comd[0:2] == "mv":
            FileRename(comd)
        elif comd[0:3] == "crf":
            CreateFile(comd)
        elif comd == "reload --colored":
            reloadProgram()
        elif comd == "install --check":
            InstallationCheck()
        elif comd[0:2] == "rm":
            Delete(comd)
        elif comd[0:2] == "sr":
            searchDir(comd)
            # notify
        elif comd[0::6] == "notify":
            Notify(comd)
            print("I hope you entered the time in minutes, any other time system like seconds or hours won't work")
        elif comd == "bash --sys 0":
            ShutDown()
        elif comd[0:3] == "crd":
            CreateDir(comd)
        elif comd == "process --uid":
            AllProcess()
        elif comd == "about bash":
            About(comd)
        elif comd[0:4] == "hide":
            hideItems(comd)
        elif comd == "cd":
            cwdPrint()
        elif comd == "udev":
            BashApi()
        elif comd[0:4] == "kill":
            killTask(comd[4::])
        elif comd[0:3] == "uhd":
            unhide(comd)
        elif comd[0:2] == "cd":
            cwdChange(comd)
        elif "cpy" in comd:
            Copy(comd)
        elif comd[0:5] == "write":
            editFile(comd)
        elif comd == "ls --check":
            checker()
        elif comd == "sussy" or comd == "sussy baka" or comd == "sus":
            Suss()
        elif comd == "ls --dir" or comd == "ls --dirs":
            lsdirs()
        elif comd == "rm -rf":
            subprocess.run(comd)
        # elif comd == "bash --ui==hacker":
        #     HackerUi()
        elif comd == "curt user":
            print(getpass.getuser())
        elif comd[0:3] == "pip":
            subprocess.run(comd)
        elif comd == "help" or comd == "Help" or comd == "bash --help" or comd == "help me":
            helpText()
        elif comd[0:4] == "read":
            readFile(comd)
        elif comd == "":
            pass
        elif comd == "good":
            print("Thanks :)")
        elif comd[0:3] == "git":
            subprocess.run(comd)
            print("\nIf the text colors run out after running this command, type reload --colored in the command line")
        elif comd[0:6] == "python":
            try:
                subprocess.run(comd)
            except Exception as e:
                # print("Failed to execute script main\n\tstdin<python>")
                print(e)
        elif comd[0:7] == "python1" or comd[0:7] == "python2":
            print(
                f"{fg('red_1')}Python versions prior to version 3.0 not supported by file bash{attr('reset')}")
        elif comd == "bash --q" or comd == "exit":
            print("Logout Bash")
            t.sleep(0.50)
            exit()
        else:
            items = get_close_matches(comd, commands, n=1, cutoff=0.5)
            # print(f"{fg('red_1')}fatal: Invalid Command '{comd}'{attr('reset')}")
            print(f"bash: no command found: '{comd}'")
            for i in items:
                data = i
                print(
                    f"{fg('red')}{attr('blink')}Did you mean:\n\t{data}\nUse bash --help for commands list{attr('reset')}")
                continue
