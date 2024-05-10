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

            with open('database','r',newline='') as file:
                database = csv.reader(file)
                database_copy=[]
                for account in database:
                    database_copy.append(account)
            with open('database','w',newline='') as file:
                writer = csv.writer(file)
                names = self.__current_account.get_name()
                override = False
                for account in database_copy:
                    if account[0]==names[0] and account[1]==names[1] and account[2]==str(self.__current_account.get_pin()) and override==False:
                        #checking for any history
                        override=True
                        if not self.__current_account.get_history()==None:
                            hist_list = self.__current_account.get_history()
                            hist_list=[str(i) for i in hist_list]
                            history = ','.join(hist_list)
                            writer.writerow([names[0],names[1],self.__current_account.get_pin(),f'{self.__current_account.get_balance():.2f}',history])
                        else:
                            writer.writerow([names[0],names[1],self.__current_account.get_pin(),f'{self.__current_account.get_balance():.2f}'])

                    elif not (account[0]==names[0] and account[1]==names[1] and account[2]==str(self.__current_account.get_pin())):
                        writer.writerow(account)
                if self.__new_account == 'Created':
                    if not self.__current_account.get_history() == None:
                        hist_list = self.__current_account.get_history()
                        hist_list = [str(i) for i in hist_list]
                        history = ','.join(hist_list)
                        writer.writerow([names[0], names[1], self.__current_account.get_pin(),
                                         f'{self.__current_account.get_balance():.2f}', history])
                    else:
                        writer.writerow([names[0], names[1], self.__current_account.get_pin(),
                                         f'{self.__current_account.get_balance():.2f}'])

        def check_accounts(self)->bool:
            '''
            returns True if account entered is in the database
            :return:
            '''
            # no empty fields
            if ''==self.FNEntry.text().strip() or ''==self.LNEntry.text().strip() or ''==self.PINEntry.text().strip():
                raise ValueError
            #PIN must be numeric
            if not self.PINEntry.text().strip().isdigit():
                raise ValueError
            # names cant have numbers
            if not self.FNEntry.text().strip().isalpha() or not self.LNEntry.text().strip().isalpha():
                raise ValueError
            with open('database','r',newline='')as file:
                database=csv.reader(file)
                for account in database:
                    try:
                        if account[0]==self.FNEntry.text().strip() and account[1]==self.LNEntry.text().strip() and account[2]==self.PINEntry.text().strip():
                            self.__current_account=Account(fname=account[0],lname=account[1],pin=int(account[2]),balance=float(account[3]),history=(','.join(account[4:])))
                            hist_list=self.__current_account.get_history().split(',')
                            last=hist_list.pop(-1)
                            if last!='':
                                hist_list.append(last)
                            print(hist_list)
                            self.__current_account.set_history(hist_list)
                            return True
                    except IndexError:
                        return False
            return False

        def account_history_str(self)->str:
            history=self.__current_account.get_history()

            string='Most Recent:\n'
            recent_5=0
            try:
                history = [float(i) for i in history]
                for trans in range(1,len(history)+1):
                    if recent_5==5:
                        break
                    try:
                        recent_5+=1
                        string+='\t'+str(history[-trans])+'\n'
                    except IndexError:
                        break
            except TypeError:
                string+=''
            return string
        def account_info_str(self)->str:
            names=self.__current_account.get_name()
            return f'Name: {names[0].strip()} {names[1].strip()}\nBalance: ${self.__current_account.get_balance():.2f}'

        def update_screen(self)->None:
            '''
            updates screen
            :return:
            '''
            names = self.__current_account.get_name()
            self.LoginLabel.setText(f'Welcome {names[0]}, {names[1]}')
            self.HistDisplayLabel.setText(self.account_history_str())
            self.AccDisplayLabel.setText(self.account_info_str())
        def login(self)->None:
            '''
            logs into the account if account is in database
            :return:
            '''
            #need to make sure that input is valid
            try:
                self.__exist=self.check_accounts()
                if self.__exist==True or self.__new_account=='Created':
                    self.__new_account = False
                    self.update_screen()
                else:
                    if self.__new_account==True:
                        self.LoginLabel.setText('Enter Starting Balance into Desposit/WithDraw Field then press enter again.')
                        self.__new_account='Create'
                    elif self.__new_account=='Create':
                        self.__new_account = 'Created'
                        self.create_account()
                    else:
                        self.__new_account=True
                        self.LoginLabel.setText('Please make sure your information is entered correctly. Press Enter again to make a new account.')
            except ZeroDivisionError as e:
                self.__new_account='Create'
                self.LoginLabel.setText(
                    'Please enter a number into Deposit/Withdraw to set balance')
                print(e)
            except ValueError as e:
                self.LoginLabel.setText('Please enter valid information into the fields.\n (PIN must be numeric and no numbers in names)')
                print(e)
        def create_account(self)->None:
            '''
            creates a new account
            :return:
            '''
            try:
                if self.wdEntry.text().strip()=='':
                    raise ZeroDivisionError
                if float(self.wdEntry.text().strip())<0:
                    raise ZeroDivisionError
                self.__current_account=Account(fname=self.FNEntry.text().strip(),lname=self.LNEntry.text().strip(),pin=self.PINEntry.text().strip(),balance=float(self.wdEntry.text().strip()))
            except ValueError:
                raise ZeroDivisionError
            self.database_update()
            self.update_screen()

        def withdraw(self)->None:
            '''
            withdraws money from account balance
            :return:
            '''
            if self.__current_account==None:
                self.LoginLabel.setText('Login before Withdrawal')
            else:
                try:
                    amt=float(f'{float(self.wdEntry.text().strip()):.2f}')
                    if (self.__current_account.withdraw(amt))==True:
                        self.update_history(-amt)
                    else:
                        self.LoginLabel.setText('Please enter a number that is not more than you currently have or negative')
                except ValueError:
                    self.LoginLabel.setText('Please enter a none negative number to withdraw')

        def deposit(self)->None:
            '''
            puts money into the balance
            :return:
            '''
            if self.__current_account==None:
                self.LoginLabel.setText('Login before Depositing')
            else:
                try:
                    amt = float(f'{float(self.wdEntry.text().strip()):.2f}')
                    if (self.__current_account.deposit(amt)) == True:
                        self.update_history(amt)
                    else:
                        self.LoginLabel.setText('Please enter a number that is not negative')
                except ValueError:
                    self.LoginLabel.setText('Please enter a number')
        def update_history(self,val:float)->None:
            '''
            updates history
            :return:
            '''
            if self.__current_account.get_history()==None:
                self.__current_account.set_history([val])
            else:
                hist=self.__current_account.get_history()
                self.__current_account.set_history(hist+[val])

            self.update_screen()
            self.database_update()
        def __init__(self)->None:
            '''

            '''
            super().__init__()
            self.setupUi(self)
            self.__exist=False
            self.__current_account=None
            self.__new_account=False
            self.EnterButton.clicked.connect(lambda: self.login())
            self.WithdrawlButton.clicked.connect((lambda:self.withdraw()))
            self.DespoitButton.clicked.connect((lambda :self.deposit()))



