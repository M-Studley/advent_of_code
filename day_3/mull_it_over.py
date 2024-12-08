import re


def extract_data_from_file(file_name: str) -> list[str]:
    data = []
    with open(file_name) as file:
        for row in file:
            data.append(row)

    return data


def compile_results(regex_pattern: str, all_data: list[str]) -> int:
    total = 0
    for data in all_data:
        matches = re.findall(regex_pattern, data)
        for match in matches:
            x, y = map(int, match)
            product = x * y
            total += product

    return total


extracted_data = extract_data_from_file('mull_it_over_data.txt')

pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
result = compile_results(pattern, extracted_data)

print(result)
