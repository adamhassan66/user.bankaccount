

# WILL NOT WORK ON VS CODE, ONLY ON TERMINAL.
class BankAccount:

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(self.balance)
        # print (f"new balance{self.balance}")
        return self

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
            print(f"{self.balance} new balance")
        else:
            print("Insufficent funds! A $5 dollar fee is charged.")
            self.balance -= -5
            return self

    def display_account_info(self):
        print(self.balance)
        # print (f" new balance  ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance >= 0:
            self.balance += self.balance * self.int_rate
            # print (f"{self.balance} new balance")
        else:
            print("No positive balance to calculate intrest.")
        return self


user_1 = BankAccount(0.01, 200)
user_1.withdraw(100)


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    # other methods
    
    def make_deposit(self, amount):
        self.account.deposit(self,amount)
        return self

    def make_withdrawl(self, amount):
        return self

    def display_user_balance(self):
      self.account.display_account_info()
      return self

    def transfer_money(self, amount, user):
      self.account.transfer(amount, user)
      return self 

    # wick = User ("john", "johnwick@gmail.com").deposit(5000).transfer_money()

    # bill = User ("drake", "drakebill@gmail.com").deposit(10000).transfer_money()
