import smtplib
from email.message import EmailMessage


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


sendEmail("Welcome to File Bash!", "sannidhya127@gmail.com",
          "Welcome to File Bash. We are overwhelmed to have you with us Sanni Kumar.")
