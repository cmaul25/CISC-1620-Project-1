from PyQt6.QtWidgets import *
from gui import *
from accounts import *
import csv

class Logic(QMainWindow, Ui_MainWindow):
        def database_update(self)->None:
            '''
            finds the account in the database and updates it
            :return:
            '''
            with open('database','r+',newline='') as file:
                writer=csv.writer(file)
                database = csv.reader(file)
                for account in database:
                    names=self.__current_account.get_name()
                    if account[0]==names[0] and account[1]==names[1]:
                        #checking for any history
                        try:
                            hist_list = self.__current_account.get_history()
                            history = hist_list.join(',')
                        except:
                            history='None'
                        writer.writerow([names[0],names[1],self.__current_account.get_pin(),self.__current_account.get_balance(),history])
                    else:
                        try:
                            hist_list = self.__current_account.get_history()
                            history = hist_list.join(',')
                        except:
                            history = 'None'
                        writer.writerow([names[0],names[1],self.__current_account.get_pin(),self.__current_account.get_balance(),history])



        def check_accounts(self)->bool:
            '''
            returns True if account entered is in the database
            :return:
            '''
            # no empty fields
            if ''==self.FNEntry.text().strip() or ''==self.LNEntry.text().strip() or ''==self.PINEntry.text().strip():
                raise ValueError
            #PIN must be numeric
            if not self.PINEntry.text().strip().isalnum():
                raise ValueError
            with open('database','r',newline='')as file:
                database=csv.reader(file)
                for account in database:
                    if account[0]==self.FNEntry.text().strip() and account[1]==self.LNEntry.text().strip() and account[2]==self.PINEntry.text().strip():
                        self.__current_account=Account(fname=account[0],lname=account[1],pin=int(account[2]),balance=account[3],history=list(account[4:]))
                        print(self.__current_account)
                        print(self.__current_account.get_history())
                        return True
            return False

        def account_history_str(self)->str:
            history=self.__current_account.get_history()
            string='Most Recent:\n'
            recent_5=0
            for trans in range(1,len(history)+1):
                if recent_5==5:
                    break
                try:
                    recent_5+=1
                    string+='\t'+history[-trans]+'\n'
                except IndexError:
                    break

            return string

        def login(self)->None:
            '''
            logs into the account if account is in database
            :return:
            '''
            #need to make sure that input is valid
            try:
                exist=self.check_accounts()
                if exist==True:
                    names=self.__current_account.get_name()
                    self.LoginLabel.setText(f'Welcome {names[0]}, {names[1]}')
                    self.HistDisplayLabel.setText(self.account_history_str())
                    self.__new_account=False
                else:
                    if self.__new_account==True:
                        self.LoginLabel.setText('Enter Starting Balance into Desposit/WithDrawl Field then press enter again.')
                        self.__new_account='Create'
                    elif self.__new_account=='Create':
                        self.create_account()
                    else:
                        self.__new_account=True
                        self.LoginLabel.setText('Please make sure your information is entered correctly. Press Enter again to make a new account.')

            except ValueError:
                self.LoginLabel.setText('Please enter valid information into the fields.\n (PIN must be numeric)')
        def create_account(self)->None:
            '''
            creates a new account
            :return:
            '''
            self.__current_account=Account(fname=self.FNEntry.text(),lname=self.LNEntry.text(),pin=self.PINEntry.text(),history=[],balance=int(self.wdEntry.text()))
            self.database_update()
        def __init__(self)->None:
            '''

            '''
            super().__init__()
            self.setupUi(self)
            self.__current_account=None
            self.__new_account=False
            self.EnterButton.clicked.connect(lambda: self.login())





