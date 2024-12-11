from D10.Chunk import Chunk

#with open('example.txt', 'r', encoding="utf-8") as f:
with open('input_1.txt', 'r', encoding="utf-8") as f:
    puzzleInput = f.read().split("\n")

charScore: dict() = {')': 3, ']': 57, '}': 1197, '>': 25137}


score: int = 0
print(puzzleInput)

for line in puzzleInput:
    chunk: Chunk = Chunk()
    for char in line:
        if not chunk.add_next_char(char):
            score += charScore[char]
            break
    print(chunk)

print(score)




