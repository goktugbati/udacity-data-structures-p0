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
nonTelemarketers = set()

for text in texts:
    nonTelemarketers.add(text[0])
    nonTelemarketers.add(text[1])

for call in calls:
    nonTelemarketers.add(call[1])

callers = set()
for call in calls:
    callers.add(call[0])

possible_telemarketers = callers - nonTelemarketers
print("These numbers could be telemarketers: {}".format(str(sorted(possible_telemarketers))))
