import re



num_pattern = r"^[-+]?[0-9]+$"

pattern = r"mul\(\d+,\d+\)"
string = ""

all_matches = re.findall(pattern, string)
print(all_matches)

with open('input_3.txt', 'r') as f:
    for line in f.readlines():
        string += line


matches = re.findall(pattern=pattern, string=string)


result = 0

for match in matches:
    number_pattern = r"\d+"
    find_numbers = [int(num) for num in re.findall(number_pattern, match)]

    result += find_numbers[0] * find_numbers[1]

print("Without commands: ",result)

# PART TWO
pattern = r"mul\(\d+,\d+\)|don't\(\)|do\(\)"

instruction_matches = re.findall(pattern=pattern, string=string)
command = "do()"

def perform_multiplication(string):
    number_pattern = r"\d+"
    find_numbers = [int(num) for num in re.findall(number_pattern, string)]

    result = find_numbers[0] * find_numbers[1]
    return result


i = 0
total = 0
while(i<len(instruction_matches)):
    if(instruction_matches[i] == "do()" or instruction_matches[i] == "don't()"):
        command = instruction_matches[i]
        i += 1
        continue

    if(command == "do()"):
        total += perform_multiplication(instruction_matches[i])
    i += 1

print(F"With Commands: {total}")