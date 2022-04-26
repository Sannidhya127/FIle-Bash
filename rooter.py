from main import *
import datetime
import time

timeNow = datetime.datetime.now()

existion = os.path.exists("report-file-bash.log")
if existion == True:
    pass
else:
    logfile=open("report-file-bash.log", 'w')




def FullScan():
    print("Initialising File Bash Full Scan....")
    print("Scanning function: AllFiles()")
    logfile=open("report-file-bash.log", 'w')
    try:
        AllFiles()
        print("No issues with AllFiles() command")
        logfile.write(f"Function AllFiles() ran successfully at {timeNow}\n")

    except Exception as e:
        print(f"Issue found: {e}")
        logfile.write(f"Found an issue with AllFiles() function: {e}\n")

    print("Scanning Fucntion: lsdirs()")


    try: 
        lsdirs()
        print("lsdirs() ran without issues")
        logfile.write(f"Fucntion lsdirs() ran successfully at {timeNow}\n")
    except Exception as e:
        print(f"Issue found: {e}")
        logfile.write(f"Found an issue with lsdirs() function: {e}\n")
    
    print("Scanning fucntion: printDocs()")


    try:
        printDocs()
        print("No issues with printDocs() function")
        logfile.write(f"Function printDocs() ran successfully at {timeNow}")
    except Exception as e:
        print(f"Issue found: {e}")
        logfile.write(f"Found an issue with printDocs(): {e}")

if __name__ == '__main__':
    while True:
        cwd = os.getcwd()
        option =  input(f"{fg('green_1')}{cwd}: {attr('reset')}")
        if option == "rooter --sc 0":
            FullScan()
        elif option == "exit":
            exit()