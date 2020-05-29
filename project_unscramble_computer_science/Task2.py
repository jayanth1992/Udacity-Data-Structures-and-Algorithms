"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

call_time = {}

for i in calls:
    from_num_total_time = call_time.get(i[0], None)
    to_num_total_time = call_time.get(i[1], None)

    if from_num_total_time is None:
        call_time[i[0]] = int(i[3])
    else:
        call_time[i[0]] = from_num_total_time + int(i[3])

    if to_num_total_time is None:
        call_time[i[1]] = int(i[3])
    else:
        call_time[i[1]] = to_num_total_time + int(i[3])

max_time = 0
result = ''

for k,v in call_time.items():
    if v > max_time:
        max_time = v
        result = k


print(f"{result} spent the longest time, {max_time} seconds, on the phone during September 2016.")
