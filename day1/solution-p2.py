import re

from utils import read_text_file

data = read_text_file("input.txt")


def return_digit(digit_string):
    digit_map = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    return digit_map.get(digit_string, digit_string)


def get_first_digit(digit_string):
    if len(digit_string) > 1:
        return digit_string[0]
    return digit_string


def get_last_digit(digit_string):
    if len(digit_string) > 1:
        return digit_string[-1]
    return digit_string


def add_to_total(numbered_string, final_total):
    if len(numbered_string) > 1 or (len(numbered_string) == 1 and len(numbered_string[0]) > 1):
        first_digit, last_digit = return_digit(numbered_string[0]), return_digit(numbered_string[-1])
        total_digit = get_first_digit(first_digit) + get_last_digit(last_digit)
        print("digit to add: " + total_digit)

        final_total = final_total + int(total_digit)
        print(f"sub total: {final_total}")
    else:
        # single digit
        duplicate_digit = return_digit(numbered_string[0]) + return_digit(numbered_string[0])
        print("digit to add: " + duplicate_digit)
        final_total = final_total + int(duplicate_digit)
        print(f"sub total: {final_total}")

    return final_total


total = 0
iteration = 0

for string in data:
    iteration = iteration + 1

    new_string = [match.group(1) for match in re.finditer(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d+))', string)]

    print(f"iteration: {iteration}")
    print(string)
    print(new_string)

    total = add_to_total(new_string, total)

print(total)
