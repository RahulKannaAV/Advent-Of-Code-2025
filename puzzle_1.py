import heapq
from collections import defaultdict

input_file = "input_1.txt"

first_list = []
second_list = []

freq_list_second = defaultdict(int)

with open(input_file, 'r') as f:
    for line in f.readlines():
        numbers = line.split('   ')
        numbers[-1] = numbers[-1].replace('\n', '')

        first_list.append(int(numbers[0]))
        second_list.append(int(numbers[1]))
        freq_list_second[numbers[-1]] += 1

similarity_score = 0
for num in first_list:
    similarity_score += (num * freq_list_second[str(num)])

heapq.heapify(first_list)
heapq.heapify(second_list)




print(similarity_score)
total_distance = 0

while(len(first_list) > 0):
    first_list_min = heapq.heappop(first_list)
    second_list_min = heapq.heappop(second_list)

    total_distance += abs(second_list_min - first_list_min)

print(total_distance)


