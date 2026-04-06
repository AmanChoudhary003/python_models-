from models.account import Account;
from models.customer import Customer;

account= Account
customer= Customer


user1= customer("123", "Rahul", "rahul@gmail.com")
acc1= account(1111, "Saving", 5000)
acc2= account(1212, "Saving", 10000)

acc1.withdrawal(1000)
acc2.deposit(20000)



user1.add_account(acc1)
user1.add_account(acc2)

print(user1.show_accounts())
print(acc1.show_transaction())