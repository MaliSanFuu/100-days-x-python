import random

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]

treasure_map = [row1,row2,row3]

print(f'{row1}\n{row2}\n{row3}')

location = input("Where do want to put the map? Give the coordinates (eg. 1,2)")
coordinates = list(map(int, location.split(sep=",")))

_x = coordinates[0] - 1
_y = coordinates[1] - 1

treasure_map[_x][_y] = "X"

print(f'{row1}\n{row2}\n{row3}')

