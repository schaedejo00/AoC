from collections import Counter, defaultdict
from AoCInputHelper import *



# prepare input
input_data: list[int] = get_grid(get_input(2024, 12))
#input_data: list[int] = get_grid(open('example.txt').read())

regions:list[set[chr]] = []

print(input_data)
