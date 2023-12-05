import re

from utils import read_text_file

data = read_text_file("demo_p1.txt")



total = 0
for string in data:
    new_string = re.sub('\D', '', string)
    print(new_string)
    if len(new_string) > 1:
        total_digit = new_string[0] + new_string[-1]
        total = total + int(total_digit)
#
    else:
        duplicate_digit = new_string + new_string
        total = total + int(duplicate_digit)

print(total)