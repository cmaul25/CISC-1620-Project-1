
class Account:
#a
    def __init__(self, fname:str, lname:str,pin:int,history=None,balance=0):
        self.__account_fname=fname
        self.__account_lname=lname
        self.__account_balance=balance
        self.__account_history=history
        self.__account_pin=pin

#b
    def deposit(self,amount):
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False
#c
    def withdraw(self,amount):
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False
#d
    def get_balance(self):
        return float(self.__account_balance)
#e
    def get_name(self):
        return (self.__account_fname,self.__account_lname)

    def get_pin(self):
        return self.__account_pin
    def get_history(self)->list:
        return self.__account_history
#f
    def set_balance(self,value):
        if value>=0:
            self.__account_balance=value
        else:
            self.__account_balance=0
#g
    def set_name(self,value:tuple)->None:
        self.__account_name,self.__account_lname=value
    def set_history(self,value:list)->None:
        self.__account_history=value
#h
    def __str__(self):
        return (f"Account name {self.get_name()[0]} {self.get_name()[1]}, Account balance = {self.get_balance():.2f}, "
                f"Number of Transactions: {len(self.__account_history)}")
#2
if __name__=="__main__":
    jane=Account('Jane','B',0000,[2,3,4],100)
    print(jane)

