test = [
    ['.', 'M', '.', 'S', '.', '.', '.', '.', '.', '.'],
    ['.', '.', 'A', '.', '.', 'M', 'S', 'M', 'S', '.'],
    ['.', 'M', '.', 'S', '.', 'M', 'A', 'A', '.', '.'],
    ['.', '.', 'A', '.', 'A', 'S', 'M', 'S', 'M', '.'],
    ['.', 'M', '.', 'S', '.', 'M', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['S', '.', 'S', '.', 'S', '.', 'S', '.', 'S', '.'],
    ['.', 'A', '.', 'A', '.', 'A', '.', 'A', '.', '.'],
    ['M', '.', 'M', '.', 'M', '.', 'M', '.', 'M', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
]

"""
ms -> ms, ss -> mm, mm -> ss, sm -> sm
[(-1, -1), (-1, 1)], [(1, -1), (1, 1)]
"""


def extract_data_from_file(file_name: str) -> list[list[str]]:
    with open(file_name) as file:
        data = file.read().splitlines()

    matrix = [[char for char in row] for row in data]

    return matrix


# PART 2
def search_x_shape(data: list[list[str]], r_idx: int, c_idx: int) -> int:
    matches = 0
    row_length = len(data)
    col_length = len(data[0])

    top_directions = [(-1, -1), (-1, 1)]
    bottom_directions = [(1, -1), (1, 1)]

    for row_step, col_step in top_directions + bottom_directions:
        new_r_idx = r_idx + row_step
        new_c_idx = c_idx + col_step
        if not (0 <= new_r_idx < row_length and 0 <= new_c_idx < col_length):
            return matches

    top = [data[r_idx + row_step][c_idx + col_step] for row_step, col_step in top_directions]
    bottom = [data[r_idx + row_step][c_idx + col_step] for row_step, col_step in bottom_directions]

    valid_pairs = {
        ('M', 'S'): ('M', 'S'),
        ('S', 'M'): ('S', 'M'),
        ('M', 'M'): ('S', 'S'),
        ('S', 'S'): ('M', 'M')
    }

    top_pair = tuple(top)
    bottom_pair = tuple(bottom)

    if top_pair in valid_pairs and valid_pairs[top_pair] == bottom_pair:
        matches += 1

    return matches


grid = extract_data_from_file('ceres_search_data')

total = 0
for row_idx, row in enumerate(grid):
    for col_idx, col in enumerate(row):
        if col == 'A':
            total += search_x_shape(grid, row_idx, col_idx)

print(total)

# PART 1
# directions = {
#     'right': (0, 1),
#     'left': (0, -1),
#     'down': (1, 0),
#     'up': (-1, 0),
#     'down_right': (1, 1),
#     'down_left': (1, -1),
#     'up_right': (-1, 1),
#     'up_left': (-1, -1)
# }
#

# def search_all_directions(data: list[list[str]], key_word: str) -> int:
#     total_matches = 0
#     row_length = len(data)
#     col_length = len(data[0])
#
#     for r_idx, row in enumerate(data):
#         for c_idx, col in enumerate(row):
#             if col == 'X':
#                 for direction, (row_step, col_step) in directions.items():
#                     end_row = r_idx + (len(key_word) - 1) * row_step
#                     end_col = c_idx + (len(key_word) - 1) * col_step
#
#                     if not (0 <= end_row < row_length and 0 <= end_col < col_length):
#                         continue
#
#                     match = True
#                     for i in range(1, len(key_word)):
#                         new_r_idx = r_idx + i * row_step
#                         new_c_idx = c_idx + i * col_step
#
#                         if data[new_r_idx][new_c_idx] != key_word[i]:
#                             match = False
#                             break
#
#                     if match:
#                         total_matches += 1
#
#     return total_matches
#
#
# grid = extract_data_from_file('ceres_search_data')
#
# total = search_all_directions(grid, 'XMAS')
# print(total)
