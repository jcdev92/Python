class Account:
    id          = int;
    name        = str;
    document    = str;
    password    = str;
    email       = str;

    def __init__(self, name, document):
        self.name = name
        self.document = document
        