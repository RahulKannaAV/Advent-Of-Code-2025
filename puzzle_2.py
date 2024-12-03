import math

file_name = "input_2.txt"
all_rows = []

with open(file_name, 'r') as f:
    for line in f.readlines():
        line.replace('\n', '')
        row = list(map(int, line.split(" ")))
        all_rows.append(row)

def checkTrends(row):
    copy = row.copy()
    same_trend = 0
    inc_trend = 0
    max_inc = -math.inf
    dec_trend = 0
    max_dec = 0
    for i in range(len(copy)-1):

        difference = copy[i] - copy[i+1]
        if(difference < 0):
            inc_trend += 1
            max_inc = max(max_inc, -difference)
        elif(difference > 0):
            dec_trend += 1
            max_dec = max(max_dec, difference)
        else:
            same_trend += 1

        if((inc_trend > 0 and dec_trend > 0) or
            (inc_trend > 0 and same_trend > 0) or
            (same_trend > 0 and dec_trend > 0)):
            return False
    if((max_inc <= 3 and max_dec == 0) or (max_dec <= 3 and max_inc == -math.inf)):
        return True
    else:
        return False

"""safe_count = 0

for row in all_rows:
    status = checkTrends(row)

    if(status):
        safe_count += 1
print(safe_count)"""

# Part 2
def checkTrendsIgnoreOneBadLevel(row):
    copy = row.copy()
    same_trend = 0
    inc_trend = 0
    max_inc = -math.inf
    dec_trend = 0
    max_dec = 0

    bad_diffs = 0

    for i in range(len(copy)-1):
        difference = copy[i] - copy[i+1]
        if (abs(difference) > 3):
            bad_diffs += 1
        if(difference < 0):
            inc_trend += 1
            max_inc = max(max_inc, -difference)
        elif(difference > 0):
            dec_trend += 1
            max_dec = max(max_dec, difference)
        else:
            same_trend += 1
    # print(inc_trend, dec_trend, same_trend)
    if((inc_trend > 1 and dec_trend == 1) or
        (inc_trend > 1 and same_trend == 1) or
        (dec_trend > 1 and same_trend == 1)):
        return True

    if((max_inc <= 3 and max_dec == 0) or (max_dec <= 3 and max_inc == -math.inf)):
        return True
    else:
        return False

inputs = [[7, 6, 4, 2, 1],
          [1, 2, 7, 8, 9],
          [9, 7, 6, 2, 1],
          [1, 3, 2, 4, 5],
          [8, 6, 4, 4, 1],
          [1, 3, 6, 7, 9]]

actual_safe_count = 0
for row in inputs:
    status = checkTrendsIgnoreOneBadLevel(row)
    print(status)
    if(status):
        actual_safe_count += 1

print(actual_safe_count)