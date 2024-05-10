
class Account:
    '''
    account class that handles modifications in balance
    '''
    def __init__(self, fname:str, lname:str,pin:int,history=None,balance=0)->None:
        '''
        sets up instance variables for account
        :param fname: first name
        :param lname: last name
        :param pin: pin number
        :param history: account transaction history
        :param balance: current balance
        '''
        self.__account_fname=fname
        self.__account_lname=lname
        self.__account_balance=balance
        self.__account_history=history
        self.__account_pin=pin

#b
    def deposit(self,amount:float)->bool:
        '''
        deposits money into balance
        :param amount:
        :return:
        '''
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False
#c
    def withdraw(self,amount:float)->bool:
        '''
        removes money from balance
        :param amount:
        :return:
        '''
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False
#d
    def get_balance(self)->float:
        '''
        getter that returns account balance
        :return:
        '''
        return float(self.__account_balance)
#e
    def get_name(self)->tuple:
        '''
        getter that returns first and last name as a tuple
        :return:
        '''
        return (self.__account_fname,self.__account_lname)

    def get_pin(self)->int:
        '''
        getter that return pin
        :return:
        '''
        return self.__account_pin
    def get_history(self)->list:
        '''
        getter that return history
        :return:
        '''
        return self.__account_history
#f
    def set_balance(self,value:float)->None:
        '''
        sets balance
        :param value:
        :return:
        '''
        if value>=0:
            self.__account_balance=value
        else:
            self.__account_balance=0
    def set_history(self,value:list)->None:
        '''
        sets history
        :param value:
        :return:
        '''
        self.__account_history=value
#h
    def __str__(self)->str:
        '''
        returns a formatted string to get printed
        :return:
        '''
        return (f"Account name {self.get_name()[0]} {self.get_name()[1]}, Account balance = {self.get_balance():.2f}, "
                f"Number of Transactions: {len(self.__account_history)}")
#2
if __name__=="__main__":
    jane=Account('Jane','B',0000,[2,3,4],100)
    print(jane)

