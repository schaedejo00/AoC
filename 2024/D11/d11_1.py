from collections import Counter, defaultdict
from AoCInputHelper import get_input

def blink(stones:dict[int, int]) -> dict[int, int]:
    new_stones:dict[int, int] = defaultdict(int)
    for stone in stones:
        if stone == 0:
            new_stones[1] += stones[stone]
        else:
            stone_str = str(stone)
            if len(stone_str)%2 == 0:
                left:int = int(stone_str[:len(stone_str)//2])
                right:int = int(stone_str[len(stone_str)//2:])
                new_stones[left] += stones[stone]
                new_stones[right] += stones[stone]
            else:
                new_stones[stone * 2024] += stones[stone]
    return new_stones

# prepare input
input_data: list[int] = [int(x) for x in get_input(2024, 11).split(' ')]
#input_data: list[int] = [int(x) for x in open('example.txt').read().split(' ')]
stones:dict[int, int] = Counter(input_data)
print(f"stones={stones}")

for i in range(0, 75):
    stones = blink(stones)
    print(f"i={i+1}, stones={sum(stones.values())}")