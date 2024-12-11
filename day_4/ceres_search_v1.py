# 18 matches
grid = [
['M', 'M', 'M', 'S', 'X', 'X', 'M', 'A', 'S', 'M'],  # 0
['M', 'S', 'A', 'M', 'X', 'M', 'S', 'M', 'S', 'A'],  # 1
['A', 'M', 'X', 'S', 'X', 'M', 'A', 'A', 'M', 'M'],  # 2
['M', 'S', 'A', 'M', 'A', 'S', 'M', 'S', 'M', 'X'],  # 3
['X', 'M', 'A', 'S', 'A', 'M', 'X', 'A', 'M', 'M'],  # 4
['X', 'X', 'A', 'M', 'M', 'X', 'X', 'A', 'M', 'A'],  # 5
['S', 'M', 'S', 'M', 'S', 'A', 'S', 'X', 'S', 'S'],  # 6
['S', 'A', 'X', 'A', 'M', 'A', 'S', 'A', 'A', 'A'],  # 7
['M', 'A', 'M', 'M', 'M', 'X', 'M', 'M', 'M', 'M'],  # 8
['M', 'X', 'M', 'X', 'A', 'X', 'M', 'A', 'S', 'X']   # 9
]

row_length = len(grid[0])
col_length = len(grid)

def search_right(data: list[list[str]], key_word: str, r_idx: int, c_idx: int) -> int:
    matches = 0

    if c_idx + 3 > col_length:
        return matches

    for i in range(1, len(key_word)):
        if data[r_idx][c_idx + i] != key_word[i]:
            return matches

    matches += 1
    print(f'({r_idx},{c_idx})')

    return matches


def search_left(data: list[list[str]], key_word: str, r_idx: int, c_idx: int) -> int:
    matches = 0

    if c_idx - 3 < 0:
        return matches

    for i in range(1, len(key_word)):
        if data[r_idx][c_idx - i] != key_word[i]:
            return matches

    matches += 1
    print(f'({r_idx},{c_idx})')

    return matches


def search_down(data: list[list[str]], key_word: str, r_idx: int, c_idx: int) -> int:
    matches = 0

    if r_idx + 3 > row_length:
        return matches

    for i in range(1, len(key_word)):
        if data[r_idx + i][c_idx] != key_word[i]:
            return matches

    matches += 1
    print(f'({r_idx},{c_idx})')

    return matches

def search_up(data: list[list[str]], key_word: str, r_idx: int, c_idx: int) -> int:
    matches = 0

    if r_idx - 3 < 0:
        return matches

    for i in range(1, len(key_word)):
        if data[r_idx - i][c_idx] != key_word[i]:
            return matches

    matches += 1
    print(f'({r_idx},{c_idx})')

    return matches


total = 0

for row_idx, row in enumerate(grid):
    for col_idx, col in enumerate(row):
        if col == 'X':
            total += search_right(grid, 'XMAS', row_idx, col_idx)
            total += search_left(grid, 'XMAS', row_idx, col_idx)
            total += search_down(grid, 'XMAS', row_idx, col_idx)
            total += search_up(grid, 'XMAS', row_idx, col_idx)
            print(total)

print(total)
