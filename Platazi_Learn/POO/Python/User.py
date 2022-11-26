from Account import Account

class user(Account):
    def __init__(self, name, document, password, email):
        super.__init__(name, document, password, email)
