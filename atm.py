import sys,time,random
from Bank import Bank

class ATM(object):

    def __init__(self):
        self.bank = Bank("Python")
        pass

    def init(self):
        pass

    def loggedInState(self):
        option = input("1. Withdraw    2. Deposit    3. Exit Session\n")
        match option:
            case "1":
                pass
            case "2":
                pass
            case "3":
                print("good choice")

    def promptAccountCreation(self):
        name = input("Name: ")
        pin = input("PIN: ")
        confirm = ""
        while confirm != pin:
            confirm = input("Confirm PIN: ")
        self.bank.createUser(name, pin)
        print("\nWelcome {}".format(name))

    def session(self):
        self.slow_type("Welcome to {} Bank!\n".format(self.bank.name))
        print("Select an option")
        while(True):
            option = input("1. Create an account    2. Login    3. Exit Session\n")
            match option:
                case "1":
                    self.promptAccountCreation()
                case "2":
                    pass
                case "3":
                    break

        print("\nGoodbye")

    def slow_type(self, t):
        typing_speed = 50 #wpm
        for l in t:
            sys.stdout.write(l)
            sys.stdout.flush()
            ##time.sleep(random.random()*10.0/typing_speed)
            time.sleep(0.05)



        

