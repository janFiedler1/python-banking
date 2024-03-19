import sys,time,random
import Bank

class ATM(object):

    def __init__(self):
        pass

    def init(self):
        pass

    def promptAccountCreation(self):
        pass

    def session(self):
        self.slow_type("Welcome to Python Bank!\n")
        print("Select an option")
        option = input("1. Create an account    2. Login    3. Exit Session\n")
        match option:
            case "1":
                self.promptAccountCreation()
            case "2":
                pass
            case "3":
                print("good choice")

    def slow_type(self, t):
        typing_speed = 50 #wpm
        for l in t:
            sys.stdout.write(l)
            sys.stdout.flush()
            ##time.sleep(random.random()*10.0/typing_speed)
            time.sleep(0.1)



        

