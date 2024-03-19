class BankAccount(object):

    def __init__(self, account_id, name, pin, amount = 0):
        self.account_id = account_id
        self.name = name
        self.pin = pin
        self.balance = amount

        current_class = self.__class__
        

    def init(self):
        pass

    def deposit(self, amount):
        if (amount > 0):
            self.amount += amount
        else:
            raise Exception("Amount deposited cannot be negative")
        
    def withdraw(self, amount):
        if (amount < 0):
            if (amount >= self.balance):
                self.balance -= amount
                return amount
        else:
            raise Exception("Amount withdrawn cannot be negative")
        
    def authenticate(self, input):
        if (input != self.pin):
            raise Exception("Wrong pin")
        

    
