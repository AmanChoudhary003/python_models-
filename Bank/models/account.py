from models.transaction import Transaction


class Account:
    def __init__(self, account_number, account_type, intial_balance=0):
        self.account_number= account_number
        self.account_type= account_type
        self.balance= intial_balance
        self.transaction=[]  #keep track of transaction
    
    def deposit(self, amount):
        if(amount<0): return False;
        self.balance+= amount
        self.transaction.append(Transaction("Deposit", amount))
        return True
    
    def withdrawal(self, amount):
        if(amount< 0): return False;
        self.balance-= amount
        self.transaction.append(Transaction("Withdrawal", amount))
        return True

    def show_transaction(self):
        total_transaction=""
        for arr in self.transaction:
            total_transaction+= str(arr)+"\n"
        return total_transaction


    def __str__(self):
        return f"Account: {self.account_number}| Type:{self.account_type} | Balance: {self.balance}"
    
