"""
** PART 1 **
RULE 1: MUST BE ASCENDING OR DESCENDING ORDER
RULE 2: ADJACENT NUMBERS MUST DIFFER BY AT LEAST 1 AND AT MOST 3

** PART 2 **
RULE 3: IF THERE IS ONE UNSAFE WE CAN REMOVE AND THE RESULT WILL NOW BE SAFE

test = [
    [7, 6, 4, 2, 1],  # TRUE (Safe without removal)
    [1, 2, 7, 8, 9],  # FALSE (Cannot be made safe)
    [9, 7, 6, 2, 1],  # FALSE (Cannot be made safe)
    [1, 3, 2, 4, 5],  # TRUE (Safe by removing the second level, 3)
    [8, 6, 4, 4, 1],  # TRUE (Safe by removing one of the 4s)
    [1, 3, 6, 7, 9]   # TRUE (Safe without removal)
]
"""

# ** PART 2 **
def is_ordered_and_valid(data: list[int]) -> bool:
    """
    Check if the data is valid without any removals.
    """
    ascending = data[0] < data[1]
    fault_counter = 0

    if len(data) < 2:
        return False

    for i in range(1, len(data)):
        diff = data[i] - data[i - 1]

        if not (1 <= abs(diff) <= 3):
            fault_counter += 1

        if ascending and diff <= 0:
            fault_counter += 1
        elif not ascending and diff >= 0:
            fault_counter += 1

    return fault_counter == 0


def can_be_made_safe(data: list[int]) -> bool:
    """
    Try removing one element at a time to see if the list can be made valid.
    """
    for i in range(len(data)):
        modified_data = data[:i] + data[i + 1:]

        if is_ordered_and_valid(modified_data):
            return True

    return False


def safety_test(report: list[list[int]]) -> int:
    """
    Check how many reports are safe either directly or by removing one element.
    """
    safe_count = 0

    for data in report:
        if is_ordered_and_valid(data):
            safe_count += 1
        elif can_be_made_safe(data):
            safe_count += 1

    return safe_count


clean_data = []
with open('red_nosed_reports_data') as file:
    for row in file:
        clean_data.append([int(num) for num in row.split()])


result = safety_test(clean_data)
print(result)


# ** PART 1 **
# def is_ordered_and_valid(data: list[int]) -> bool:
#     if len(data) < 2:
#         return False
#
#     ascending = data[0] < data[1]
#
#     for i in range(1, len(data)):
#         diff = data[i] - data[i - 1]
#
#         if not (1 <= abs(diff) <= 3):
#             return False
#
#         if ascending and diff <= 0:
#             return False
#         if not ascending and diff >= 0:
#             return False
#
#     return True
#
#
# def safety_test(report: list[list[int]]) -> int:
#     safe_count = 0
#     for data in report:
#         if is_ordered_and_valid(data):
#             safe_count += 1
#     return safe_count
#
#
# clean_data = []
# with open('red_nosed_reports_data') as file:
#     for row in file:
#         clean_data.append([int(num) for num in row.split()])
#
#
# result = safety_test(test)
# print(result)
