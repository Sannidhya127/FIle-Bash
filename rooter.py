from main import *
import datetime
import logging
import time

timeNow = datetime.datetime.now()

existion = os.path.exists("report-file-bash.log")
if existion == True:
    pass
else:
    logfile=open(f"report-file-bash.log", 'x')

logging.basicConfig(level=logging.DEBUG,
                    handlers=[logging.FileHandler("report-file-bash.log", 'r+')],format="%(asctime)s %(levelname)-6s - %(funcName)-8s - %(filename)s - %(lineno)-3d - %(message)s",datefmt="[%Y-%m-%d] %H:%M:%S - ",
                    )



def FullScan():
    print("Initialising File Bash Full Scan....")
    print("Scanning function: AllFiles()")
    try:
        AllFiles()
        print("No issues with ls command")
        logging.info("ls command ran without issues")
    except Exception as e:
        print(f"Issue found: {e}")
        logging.error(f"Found the following issue: {e}")


if __name__ == '__main__':
    while True:
        cwd = os.getcwd()
        option =  input(f"{fg('green_1')}{cwd}: {attr('reset')}")
        if option == "rooter --sc 0":
            FullScan()
        elif option == "exit":
            exit()