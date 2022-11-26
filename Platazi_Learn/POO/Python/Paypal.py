from Payment import Payment

class Paypal(Payment):
    email = str

    def __init__(self, id, amount, email):
        super.__init__(id, amount)
        self.email = email