"""
PART 2: Completed using the assistance of ChatGPT.
"""

import re


def extract_data_from_file(file_name: str) -> str:
    """Reads the entire file into a single string."""
    with open(file_name) as file:
        return file.read()


def compile_results(data: str) -> int:
    """Compiles results based on `do()`, `don't()`, and `mul()` rules within a large string."""
    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"

    combined_pattern = f"{mul_pattern}|{do_pattern}|{dont_pattern}"

    matches = re.finditer(combined_pattern, data)

    mul_enabled = True
    total = 0

    for match in matches:
        if match.group() == "do()":
            mul_enabled = True
        elif match.group() == "don't()":
            mul_enabled = False
        elif mul_enabled:
            x, y = map(int, match.groups())
            total += x * y

    return total


data_string = extract_data_from_file('mull_it_over_data.txt')

result = compile_results(data_string)

print(result)


# PART 1
# def extract_data_from_file(file_name: str) -> list[str]:
#     data = []
#     with open(file_name) as file:
#         for row in file:
#             data.append(row)
#
#     return data
#
#
# def compile_results(regex_pattern: str, all_data: list[str]) -> int:
#     total = 0
#     for data in all_data:
#         matches = re.findall(regex_pattern, data)
#         for match in matches:
#             x, y = map(int, match)
#             product = x * y
#             total += product
#
#     return total
#
#
# extracted_data = extract_data_from_file('mull_it_over_data.txt')
#
# pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
# result = compile_results(pattern, extracted_data)
#
# print(result)
