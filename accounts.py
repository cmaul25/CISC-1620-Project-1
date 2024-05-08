
class Account:
#a
    def __init__(self, fname:str, lname:str,pin:int,history:list,balance=0):
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
        if amount > 0 and amount < self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False
#d
    def get_balance(self):
        return self.__account_balance
#e
    def get_name(self):
        return self.__account_fname,self.__account_lname

#f
    def set_balance(self,value):
        if value>=0:
            self.__account_balance=value
        else:
            self.__account_balance=0
#g
    def set_name(self,value:tuple)->None:
        self.__account_name,self.__account_lname=value
#h
    def __str__(self):
        return (f"Account name {self.get_name()[0]} {self.get_name()[1]}, Account balance = {self.get_balance():.2f}, "
                f"Number of Transactions: {len(self.__account_history)}")
#2
class SavingAccount(Account):
# a+b
    MINIMUM=100
    RATE=0.02
#c
    def __init__(self,name):
        super().__init__(name,balance=SavingAccount.MINIMUM)
        self.__deposit_count=0
#d
    def apply_interest(self):
        if self.__deposit_count%5==0:
            interest=self.get_balance()*SavingAccount.RATE
            self.set_balance(interest+self.get_balance())
#e
    def deposit(self,amount):
        if super().deposit(amount):
            self.__deposit_count+=1
            self.apply_interest()
            return True
        else:
            return False
#f
    def withdraw(self,amount):
        if amount>self.get_balance()-SavingAccount.MINIMUM:
            return False
        else:
            super().withdraw(amount)
            return

#g
    def set_balance(self,value):
        if value<SavingAccount.MINIMUM:
            super().set_balance(SavingAccount.MINIMUM)
        else:
            super().set_balance(value)
#h
    def __str__(self):
        return f'SAVING ACCOUNT: {super().__str__()}'



if __name__=="__main__":
    jane=SavingAccount('Jane')
    jane.set_balance(120)
    print(jane.get_balance())

