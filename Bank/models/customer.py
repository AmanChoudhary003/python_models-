


class Customer:
    bank_name= "BankAB"
    def __init__(self, _id, name, email ):
        self._id= _id
        self.name= name
        self.email= email
        self.accounts= {}  
    
    def add_account(self, account):
        self.accounts[account.account_number]= account
    
    def show_accounts(self):
        total_accounts=""
        for arr in self.accounts:
            total_accounts+= str(arr)+"\n"
        return total_accounts
          

    def get_account_history(self, account_number):
        if account_number in self.accounts:
            acc= self.accounts[account_number]
            return f"Transaction History for {acc.account_number}:\n"+"\n".join(str(t) for t in acc.history)

    def __str__(self):
        return f"Customer_Id:{self._id} | Name: {self.name}"