"""
RULE 1: MUST BE ASCENDING OR DESCENDING ORDER
RULE 2: ADJACENT NUMBERS MUST DIFFER BY AT LEAST 1 AND AT MOST 3

test = [
    [7, 6, 4, 2, 1],  # TRUE
    [1, 2, 7, 8, 9],  # FALSE
    [1, 3, 6, 7, 9],  # TRUE
    [1, 2, 3, 4, 4],  # FALSE
    [1, 2, 3, 4, 2]   # FALSE
]
"""

def is_ordered_and_valid(data: list[int]) -> bool:
    if len(data) < 2:  # A single element or empty list is not safe
        return False

    ascending = data[0] < data[1]  # Check if we expect ascending or descending order

    for i in range(1, len(data)):
        diff = data[i] - data[i - 1]

        # Rule 2: Check if the difference between adjacent numbers is valid
        if not (1 <= abs(diff) <= 3):
            return False

        # Rule 1: Check the order based on the first comparison
        if ascending and diff <= 0:
            return False
        if not ascending and diff >= 0:
            return False

    return True


# Main function to process the reports
def safety_test(report: list[list[int]]) -> int:
    safe_count = 0
    for data in report:
        if is_ordered_and_valid(data):
            safe_count += 1
    return safe_count


# Convert input file data into list of integers
clean_data = []
with open('red_nosed_reports_data') as file:
    for row in file:
        clean_data.append([int(num) for num in row.split()])


result = safety_test(clean_data)
print(result)
