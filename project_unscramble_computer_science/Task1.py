"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

numbers = set()

# Adding all numbers in text csv to hash set
for i in texts:
    numbers.add(i[0])
    numbers.add(i[1])

for i in calls:
    numbers.add(i[0])
    numbers.add(i[1])

print(f"There are {len(numbers)} different telephone numbers in the records.")