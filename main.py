from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QMessageBox
import sys


def oncheck(window):
    filename = window.emailfile.text()

    try:
        f = open(filename, 'r')
        successmsg("Success", "File Found and loaded!")
    except Exception as err:
        print(err)
        errormsg("File Could Not be Found!", str(err))


def successmsg(title, m):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Icon.Information)
    msg.setText(title)
    msg.setInformativeText(m)
    msg.setWindowTitle("Success")
    msg.exec()


def errormsg(title, text):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Icon.Critical)
    msg.setText(title)
    msg.setInformativeText(text)
    msg.setWindowTitle("Error")
    msg.exec()


def main():
    app = QtWidgets.QApplication(sys.argv)

    window = uic.loadUi('InboxIn.ui')
    window.show()

    window.checkbtn.clicked.connect(lambda: oncheck(window))

    app.exec()


if __name__ == "__main__":
    main()
