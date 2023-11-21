from PyQt6 import QtWidgets, uic
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtWidgets import QMessageBox
import sys
import smtplib


# Checks the existance of a file
def oncheck(window):
    filename = window.emailfile.text()

    try:
        f = open(filename, 'r')
        successmsg("Success", "File Found and loaded!")
    except Exception as err:
        print(err)
        errormsg("File Could Not be Found!", str(err))


# Success Message Dialog Box
def successmsg(title, m):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Icon.Information)
    msg.setText(title)
    msg.setInformativeText(m)
    msg.setWindowTitle("Success")
    msg.exec()


# Error Msg Dialog box
def errormsg(title, text):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Icon.Critical)
    msg.setText(title)
    msg.setInformativeText(text)
    msg.setWindowTitle("Error")
    msg.exec()


# Main Entry Point for the code
def main():
    app = QtWidgets.QApplication(sys.argv)

    window = uic.loadUi('InboxIn.ui')
    window.setFixedSize(850, 850)
    Icon = QIcon("./lt.png")
    window.setWindowIcon(Icon)
    window.show()

    image_path = "./lt.png"  # Replace with the path to your image
    pixmap = QPixmap(image_path)
    window.Logo.setPixmap(pixmap)

    window.checkbtn.clicked.connect(lambda: oncheck(window))
    window.submibtn.clicked.connect(lambda: sender(window, window.sub.text(), window.emailtext.toPlainText()))

    app.exec()


# Function to handle smtp connection and send emails
def sender(window, sub, msg):
    try:
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        sender_email = 'inboxin40@gmail.com'
        sender_password = 'fgjl kkfg ioax ptxr'

        # Read recipient email addresses from a text file
        recipient_emails = []
        with open(window.emailfile.text(), 'r') as file:
            recipient_emails = [line.strip() for line in file]

        # Compose the email
        subject = sub
        message = msg

        # Connect to the SMTP server
        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(sender_email, sender_password)
        except Exception as e:
            print(f"Error: {e}")
            exit()

        # Send the email to recipients from the text file
        for recipient_email in recipient_emails:
            try:
                server.sendmail(sender_email, recipient_email, f'Subject: {subject}\n\n{message}')
                print(f'Email sent successfully to {recipient_email}!')
            except Exception as e:
                print(f"Error: {e}")

        # Quit the SMTP server
        server.quit()

        window.emailtext.setPlainText("")
        window.sub.setText("")

        successmsg("Successful", "Email Has Been Sent Successfully")

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()