import BankAccount

class Bank(object):

    def __init__(self, name):
        self.name = name
        self.accounts = []
        self.currentClientID = 1

        for cls in reversed(self.__class__.mro()):
            if hasattr(cls, 'init'):
                cls.init(self)
        

    def init(self):
        pass

    def info(self):
        print (self.accounts)

    def createUser(self, name, pin):
        self.accounts.append(BankAccount(self.currentClientID, name, pin))
        self.currentClientID += 1
