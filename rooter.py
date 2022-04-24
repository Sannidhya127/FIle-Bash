from main import *

def FullScan():
    pass


if __name__ == '__main__':
    while True:
        Intro = print("***************Rooter vAlpha0.0.2 ~ An extensive tool for testing File Bash***************")
        cwd = os.getcwd()
        option =  input(f"{fg('green_1')}{cwd}: {attr('reset')}")
        if option == "rooter -f --sc":
            FullScan()
        elif option == "exit":
            exit()