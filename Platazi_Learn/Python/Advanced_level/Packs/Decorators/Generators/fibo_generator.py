from time import sleep

def fiboGen():
    a, b = 0, 1
    while a <=13:
        yield a
        a , b = b, a+b
    raise StopIteration

if __name__ == "__main__":
    fibonacci = fiboGen()
    for element in fibonacci:
        print(element)
        sleep(1)



# class fiboIter():
#
#    def __iter__(self):
#        self.n1 = 0
#        self.n2 = 1
#        self.counter = 0
#        return self
#    
#    def __next__(self, ):
#     
#        if self.counter == 0:
#            self.counter += 1
#            return self.n1
#     
#        if self.counter == 1:
#            self.counter += 1
#            return self.n2
#
##        else:                                              INFINITE ITERATION
##            self.aux = self.n1 + self.n2
##            # self.n1 = self.n2
##            # self.n2 = self.aux
##            self.n1, self.n2 = self.n2, self.aux              # swapping
##            self.counter += 1
##            return self.aux
#
#       elif self.counter <= 8:                            # LIMITED ITERATION
#           self.aux = self.n1 + self.n2
#           self.n1, self.n2 = self.n2, self.aux              # swapping
#           self.counter += 1
#           return self.aux
#
#       else:                                               # STOP ITERATION
#            raise StopIteration