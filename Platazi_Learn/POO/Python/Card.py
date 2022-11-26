from Payment import Payment

class Card(Payment):
    type_card = str
    number = int
    scty = int
    exp_date = int
    bank = str

    def __init__(self, id, amount, type_card, number, scty, exp_date, bank):
        super.__init__(id, amount)
        self.type_card = type_card
        self.number = number
        self.scty = scty
        self.exp_date = exp_date
        self.bank = bank