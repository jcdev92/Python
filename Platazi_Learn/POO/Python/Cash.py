from Payment import Payment

class Cash(Payment):
    bills_amount = int

    def __init__(self, id, amount, bills_amount):
        super.__init__(id, amount)
        self.bills_amount = bills_amount
