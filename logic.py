from PyQt6.QtWidgets import *
from gui import *
from accounts import *
import csv

class Logic(QMainWindow, Ui_MainWindow):
        def check_accounts(self)->bool:
            '''
            returns True if account entered is in the database
            :return:
            '''
            # no empty fields
            if ''==self.FNEntry.text().strip() or ''==self.LNEntry.text().strip() or ''==self.PINEntry.text().strip():
                raise ValueError
            #PIN must be numeric
            int(self.PINEntry.text().strip())
            with open('database','r',newline='')as file:
                database=csv.reader(file)
                for account in database:
                    if account[0]==self.FNEntry.text().strip() and account[1]==self.LNEntry.text().strip() and account[2]==self.PINEntry.text().strip():
                        self.__current_account=Account(fname=account[0],lname=account[1],pin=int(account[2]),balance=account[3],history=account[4:])
                        print(self.__current_account)
                        return True
            return False


        def login(self)->None:
            '''
            logs into the account if account is in database
            :return:
            '''
            #need to make sure that input is valid
            try:
                exist=self.check_accounts()
                if exist==True:
                    self.LoginLabel.setText(f'Welcome {self.__current_account.get_balance[0]}, {self.__current_account.get_balance[1]}')
                    self.__new_account=False
                else:
                    if self.__new_account==True:
                        self.LoginLabel.setText('Enter Starting Balance into Desposit/WithDrawl Field then press enter again.')
                    else:
                        self.__new_account=True
                        self.LoginLabel.setText('Please make sure your information is entered correctly. Press Enter again to make a new account.')

            except:
                self.LoginLabel.setText('Please enter valid information into the fields.\n (PIN must be numeric)')

        def __init__(self)->None:
            '''

            '''
            super().__init__()
            self.setupUi(self)
            self.__current_account=None
            self.__new_account=False
            self.EnterButton.clicked.connect(lambda: self.login())





