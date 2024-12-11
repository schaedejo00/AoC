import numpy as np

from D10.Chunk import Chunk

#with open('example.txt', 'r', encoding="utf-8") as f:
with open('input_1.txt', 'r', encoding="utf-8") as f:
    puzzleInput = f.read().split("\n")

charScores: dict() = {')': 1, ']': 2, '}': 3, '>': 4}


scores:[int] = []
print(puzzleInput)

for line in puzzleInput:
    chunk: Chunk = Chunk()
    for char in line:
        if not chunk.add_next_char(char):
            break
    if chunk.is_corrupted:
        continue
    sequence = chunk.get_completion_sequence()
    score = 0
    for char in sequence:
        score = 5*score + charScores[char]

    scores.append(score)

scores.sort()
print(scores)
print(scores[int(len(scores)/2)], scores)




