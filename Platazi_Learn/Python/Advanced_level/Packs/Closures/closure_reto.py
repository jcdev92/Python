def make_divition_by(n):
    def repeater(number):
        assert type(number) == int, 'only integers are accepted to divide'
        return number / n
    return repeater

def run():
    divide_by_3 = make_divition_by(3)
    print(divide_by_3(18))
    divide_by_5 = make_divition_by(5)
    print(divide_by_5(100))
    divide_by_18 = make_divition_by(18)
    print(divide_by_18(54))

if __name__ == '__main__':
    run()
