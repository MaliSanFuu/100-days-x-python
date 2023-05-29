import math

def paint_calc(height, width, cover):
    number_of_cans = (height * width) / cover
    print(f'You need {math.ceil(number_of_cans)} for the wall to be painted')

test_height = int(input("Height of wall:\n"))
test_width = int(input("Width of wall:\n"))
cover = 5

paint_calc(height=test_height, width=test_width, cover=cover)
