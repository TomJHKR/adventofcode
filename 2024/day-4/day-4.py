import os
import re 
import pprint

DIRECTIONS = [
    [(0, 1), (0, 2), (0, 3)],           # Right
    [(0, -1), (0, -2), (0, -3)],        # Left
    [(1, 0), (2, 0), (3, 0)],           # Down
    [(-1, 0), (-2, 0), (-3, 0)],        # Up
    [(1, 1), (2, 2), (3, 3)],           # Diagonal forward down
    [(-1, -1), (-2, -2), (-3, -3)],     # Diagonal backward up
    [(1, -1), (2, -2), (3, -3)],        # Diagonal forward up
    [(-1, 1), (-2, 2), (-3, 3)],        # Diagonal backward down
]

WORD = "XMAS"
WORD_LENGTH = len(WORD)

matrix = [list(sub) for sub in open("input.txt", "r").readlines()]
rows = len(matrix)
cols = len(matrix[0])

def is_valid(row, col):
    return 0 <= row < rows and 0 <= col < cols

def find_xmax():
    found = 0
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == WORD[0]:
                for direction in DIRECTIONS:
                    if all(
                            is_valid(row + dr, col + dc) and 
                            matrix[row + dr][col + dc] == WORD[i + 1]
                            for i, (dr,dc) in enumerate(direction)
                        ):
                        found +=1
    return found

total_found = find_xmax()
print(total_found)
