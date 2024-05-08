from PyQt6.QtWidgets import *
from gui import *
from accounts import *
import csv

class Logic(QMainWindow, Ui_MainWindow):
        def check_accounts(self)->bool:
            '''
            returns True if account entered is in account list
            :return:
            '''
            with open('database','r',newline='')as file:
                database=csv.reader(file)
                for account in database:
                    print(account[0])
                    print(account[1])
                    print(account[2])
                    print(account[3])
                    if account[0]==self.FNEntry.text() and account[1]==self.LNEntry.text() and account[2]==self.PINEntry.text():
                        self.__current_account=Account(fname=account[0],lname=account[1],pin=int(account[2]),balance=account[3],history=account[4:])
                        print(self.__current_account)
                        return True
                    else:
                        print('not working')


        def login(self)->None:
            '''
            logs into the account if account is in list
            :return:
            '''
            pass
        def __init__(self)->None:
            '''

            '''
            super().__init__()
            self.setupUi(self)
            self.__current_account=None
            self.EnterButton.clicked.connect(lambda: self.check_accounts())





