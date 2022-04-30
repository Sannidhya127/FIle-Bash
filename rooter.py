from main import *
import datetime
import time


timeNow = datetime.datetime.now()

existion = os.path.exists("report-file-bash.log")
if existion == True:
    pass
else:
    logfile=open("report-file-bash.log", 'w')


# Disable print
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore print
def enablePrint():
    sys.stdout = sys.__stdout__



# Scan every function and write report to log file
def FullScan():
    print("Initialising File Bash Full Scan....")
    print("Scanning function: AllFiles()")
    logfile=open("report-file-bash.log", 'w')
    try:
        blockPrint()
        AllFiles()
        enablePrint()
        print("No issues with AllFiles() command")
        logfile.write(f"Function AllFiles() ran successfully at {timeNow}\n")

    except Exception as e:
        print(f"Issue found: {e}")
        logfile.write(f"Found an issue with AllFiles() function: {e}\n")

    print("Scanning Fucntion: lsdirs()")


    try: 
        blockPrint()
        lsdirs()
        enablePrint()
        print("lsdirs() ran without issues")
        logfile.write(f"Fucntion lsdirs() ran successfully at {timeNow}\n")
    except Exception as e:
        print(f"Issue found: {e}")
        logfile.write(f"Found an issue with lsdirs() function: {e}\n")
    
    print("Scanning fucntion: printDocs()")


    try:
        blockPrint()
        printDocs()
        enablePrint()
        print("No issues with printDocs() function")
        logfile.write(f"Function printDocs() ran successfully at {timeNow}\n")
    except Exception as e:
        print(f"Issue found: {e}")
        logfile.write(f"Found an issue with printDocs(): {e}\n")

    try:
        blockPrint()
        printImg()
        enablePrint()
        print("No issues with printImg() function")
        logfile.write(f"Function printImg() ran successfully at {timeNow}\n")
    except Exception as e:
        print(f"Issue found: {e}")
        logfile.write(f"Found an issue with printImg(): {e}\n")

    try:
        blockPrint()
        printAud()
        enablePrint()
        print("No issues with printAud() function")
        logfile.write(f"Function printAud() ran successfully at {timeNow}\n")
    except Exception as e:
        print(f"Issue found: {e}")
        logfile.write(f"Found an issue with printAud(): {e}\n")


    try:
        blockPrint()
        printMed()
        enablePrint()
        print("No issues with printMed() function")
        logfile.write(f"Function printMed() ran successfully at {timeNow}\n")
    except Exception as e:
        print(f"Issue found: {e}")
        logfile.write(f"Found an issue with printMed(): {e}\n")


    try:
        file = open("test.txt", 'x')
        print("\tdebug: created file 'test.txt'")
        file.close()
        # blockPrint()
        Delete("rm test.txt")
        print("\tdebug: deleted file 'text.txt'")
        # enablePrint()
        print("No issues with Delete() function")
        logfile.write(f"Function Delete() ran successfully at {timeNow}\n")
    except Exception as e:
        print(f"Issue found: {e}")
        logfile.write(f"Found an issue with Delete(): {e}\n")


    try:
        #API TEST
        file = open("test.txt", 'x')
        print("\tdebug: created file 'test.txt'")
        file.close()
        Delete("rm test.txt -GET")
        print("\tDebug: Deleted file 'test.txt' with succesfull api implementation")
        print("No issues with Delete() function")
        logfile.write(f"Function Delete() ran successfully at {timeNow}\n")
    except Exception as e:
        print(f"Issue found: {e}")
        logfile.write(f"Found an issue with Delete(): {e}\n")

if __name__ == '__main__':
    while True:
        cwd = os.getcwd()
        option =  input(f"{fg('green_1')}{cwd}: {attr('reset')}")
        if option == "rooter --sc 0":
            FullScan()
        elif option == "exit":
            exit()
        else:
            print(f"{fg('red_1')}What the heck on earth is {option} ?!?{attr('reset')}")