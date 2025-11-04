class BankAccount:

    def __init__(self ,name , balance ):
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"{self.name} ning hisobiga {amount} so'm pul qo'shildi. hozirgi balans: {self.balance}so'm")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Yetarli mablag' yo'q.")
        else:
            self.balance -= amount
            print(f"{self.name} ning hisobidan {amount} so'm pul yechib olindi. hozirgi balans: {self.balance}so'm")
account = BankAccount("Ali Valiyev", 3000)

account.deposit(100)
account.withdraw(400)