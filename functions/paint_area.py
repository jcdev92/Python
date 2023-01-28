import math
# The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

def main():
    print("please enter the height and width of the wall, to calculate the number of cans of paint needed:\n")
    test_h = int(input("Height of wall: "))
    test_w = int(input("Width of wall: "))
    coverage = 5
    paint_calc(height=test_h, width=test_w, cover=coverage)

def paint_calc(height, width, cover):
    number_of_cans = math.ceil((height * width) / cover)
    print(f"You'll need {number_of_cans} cans of paint.")




if __name__ == '__main__':
    main()