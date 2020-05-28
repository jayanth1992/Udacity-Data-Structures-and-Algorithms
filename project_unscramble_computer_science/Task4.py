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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

calls_from_number = {x[0] for x in calls}
calls_to_number = {x[1] for x in calls}

texts_from_number = {x[0] for x in texts}
texts_to_number = {x[1] for x in texts}

result = set()

for i in calls_from_number:

    if i not in calls_to_number and i not in texts_from_number and i not in texts_to_number:
        result.add(i)

result = sorted(result)

for i in result:
    print(i)