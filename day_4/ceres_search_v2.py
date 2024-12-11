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
    ['M', 'X', 'M', 'X', 'A', 'X', 'M', 'A', 'S', 'X']  # 9
]


def search_direction(data: list[list[str]], key_word: str, r_idx: int, c_idx: int, row_step: int, col_step: int) -> int:
    matches = 0
    row_length = len(data)
    col_length = len(data[0])

    end_row = r_idx + (len(key_word) - 1) * row_step
    end_col = c_idx + (len(key_word) - 1) * col_step

    if not (0 <= end_row < row_length and 0 <= end_col < col_length):
        return matches

    for i in range(1, len(key_word)):
        new_r_idx = r_idx + i * row_step
        new_c_idx = c_idx + i * col_step

        if data[new_r_idx][new_c_idx] != key_word[i]:
            return matches

    matches += 1

    return matches


total = 0

for row_idx, row in enumerate(grid):
    for col_idx, col in enumerate(row):
        if col == 'X':
            total += search_direction(grid, 'XMAS', row_idx, col_idx, 0, 1)  # Right
            total += search_direction(grid, 'XMAS', row_idx, col_idx, 0, -1)  # Left
            total += search_direction(grid, 'XMAS', row_idx, col_idx, 1, 0)  # Down
            total += search_direction(grid, 'XMAS', row_idx, col_idx, -1, 0)  # Up

            total += search_direction(grid, 'XMAS', row_idx, col_idx, 1, 1)  # Down Right
            total += search_direction(grid, 'XMAS', row_idx, col_idx, 1, -1)  # Down Left
            total += search_direction(grid, 'XMAS', row_idx, col_idx, -1, 1)  # Up Right
            total += search_direction(grid, 'XMAS', row_idx, col_idx, -1, -1)  # Up Left

print(total)
