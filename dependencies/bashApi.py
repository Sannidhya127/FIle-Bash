import smtplib
from email.message import EmailMessage
import os
import webbrowser
import colored
from colored import fg, bg, attr
from urllib.request import urlopen
import itertools
import threading
import time
import sys
sending = False


def sendEmail(sub, to, message):

    msg = EmailMessage()

    msg.set_content(message)
    msg['Subject'] = sub
    msg['From'] = "shubhradasgupta8@gmail.com"
    msg['To'] = to
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("shubhradasgupta8@gmail.com", "sanni@1234#")
    server.send_message(msg)
    server.quit()


def bashRedirect():
    srclink = "https://github.com/Sannidhya127/FIle-Bash---Truly-Legit-"
    webbrowser.open_new(srclink)


def stats():
    pass


def LogUser(name):
    f = open("user.txt", "a")
    f.write(f"User: {name}")


def LogUserEmail(email):
    f = open("user.txt", "a")
    f.write(f"Email: {email}")


def bugFixer():
    print(f"{fg('yellow_1')}Oh! We are so sorry that you found a bug in our system. We would be super helped if you report the bug to us. You can also fix the bug yourself by visiting File Bash's Github repository at https://github.com/Sannidhya127/FIle-Bash---Truly-Legit-{attr('reset')}")
    # name = input("Enter your name: ")
    fixes = input("Enter the details of the bug you found: ")
    if fixes != "quit":
        f = open("userName", "r")
        name = f.read()
        print("Thanks a lot! Your every word matters!!!!!\nWe are mailing to our system managers about this issue")
        sendEmail(f"{name} found a bug!", "shubhradasgupta8@gmail.com", fixes)
        print("Mail sent!")
    else:
        print("Action Aborted!")


def Reccomed():
    reccomendation = input("Please enter your reccomandation here: ")
    nameUserfile = open("userName", "r")
    nameUser = nameUserfile.read()
    # print(nameUser)
    # name = nameUser
    print("Sending email to administrator")
    sendEmail(f"{nameUser} has a reccomandation!",
              "shubhradasgupta8@gmail.com", reccomendation)
    print("Send email succesfully! We will for sure look after your reccomandation.\nA big thanks for helping file bash grow!")


def changeName():
    new = input("Enter new name: ")
    f = open("userName", "w")
    f.write(new)
    f.close()
    print(f"Succesfully Changed user name to {new}")


def changeMail():
    new = input("Enter new email: ")
    f = open("userEmail", "w")
    f.write(new)
    f.close()
    print(f"Succesfully Changed user email to {new}")


if __name__ == "__main__":
    while True:
        existion = os.path.exists("userName")
        if existion == True:
            print(fg('green_1'), os.getcwd(), attr('reset'), end='')
            comd = input(": ")
            if comd == "edit bash":
                bashRedirect()
            elif comd == "show stats":
                stats()
            elif comd == "bug":
                bugFixer()
            elif comd == "-b -reco":
                Reccomed()
            elif comd == "exit":
                exit()
            elif comd == "user.config.ename":
                changeName()
            elif comd == "user.config.eemail":
                changeMail()
            else:
                print(f"{fg('red_1')}Invalid Command{attr('reset')}")

        else:
            print(f"{fg('yellow_1')}You are not logged in to BashApi.\nPlease use the command user --config to use BashApi and help develop File Bash{attr('reset')}")
            print(f"{fg('green_1')}", os.getcwd(), f"{attr('reset')}", end='')
            comd = input(": ")
            if comd == "user --config":
                userName = input("Enter username: ")
                userEmail = input("Enter user email: ")
                f = open("userEmail", "w")
                l = open("userName", "w")
                l.write(f"{userName}")
                f.write(f"{userEmail}")
                f.close()
                l.close()
                while sending == True:
                    print("Loading:")
                    # animation = ["1%", "2%", "3%", "40%",
                    #              "50%", "64%", "70%", "80%", "99%", "100%"]
                    animation = [".", "..", "...", "....", ".....",
                                 "......", ".......", "........", ".........", ".........."]

                    for i in range(len(animation)):
                        time.sleep(0.2)
                        sys.stdout.write("\r" + animation[i % len(animation)])
                        sys.stdout.flush()

                    print("\n")

                sendEmail(f"Welcome To The Bash Family! {userName}", userEmail,
                          f"Welcome to File Bash {userName}. We are overwhelmed to have you with us. If you get this email it signifies that you are interested in making File Bash reach its super heights. We can't wait for your contributions to be included in this legit bash system.\nFor high level code changes please visit https://github.com/Sannidhya127/FIle-Bash---Truly-Legit-. You can open this link by typeing edit bash in the BashApi terminal. We await for you!!!")
                sending = True
                sendEmail(f"{userName} has logged in!", "shubhradasgupta8@gmail.com",
                          f"Congratulations! A new user with the name {userName} just logged in!")
                sending = False

            elif comd == "exit":
                exit()
            # if "bash --config.user" in comd:
            #     LogUser(comd)
            # elif "bash --config.email" in comd:
            #     LogUserEmail(comd)
            else:
                print(f"{fg('red_1')}fatal: Invalid Command '{comd}'{attr('reset')}")
